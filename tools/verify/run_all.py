#!/usr/bin/env python3

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VERIFY_DIR = ROOT / "tools" / "verify"
VERIFIERS_DIR = VERIFY_DIR / "verifiers"
MANIFEST_PATH = VERIFY_DIR / "verifier_manifest.json"

sys.path.insert(0, str(ROOT))


def load_verifier_modules():
    modules = []
    for path in sorted(VERIFIERS_DIR.glob("*.py")):
        if path.name.startswith("_") or path.name == "base_verifier.py":
            continue
        module_name = f"tools.verify.verifiers.verifier_{path.stem}"
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None or spec.loader is None:
            continue
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        modules.append(module)
    return modules


def get_verifier_classes(module):
    classes = []
    for name in dir(module):
        value = getattr(module, name)
        if isinstance(value, type) and value.__module__ == module.__name__:
            if name != "BaseVerifier" and name.endswith("Verifier"):
                classes.append(value)
    return classes


def load_manifest() -> set[str]:
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        return set(manifest["verifiers"])
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"[FAIL] verifier manifest: {exc}")
        return set()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Startup project verifiers.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--source-only", action="store_true")
    mode.add_argument("--runtime-only", action="store_true")
    return parser.parse_args()


def should_run(verifier, args: argparse.Namespace) -> bool:
    is_runtime = verifier.name.endswith("RuntimeVerifier")
    if args.source_only:
        return not is_runtime
    if args.runtime_only:
        return is_runtime
    return True


def main() -> int:
    args = parse_args()
    print("[verify] Starting Startup verification run")
    print(f"[verify] Repository root: {ROOT}")

    modules = load_verifier_modules()
    verifier_instances = []
    for module in modules:
        for verifier_cls in get_verifier_classes(module):
            verifier_instances.append(verifier_cls())

    manifest_names = load_manifest()
    discovered_names = {verifier.name for verifier in verifier_instances}
    missing_from_manifest = discovered_names - manifest_names
    missing_from_runner = manifest_names - discovered_names
    if missing_from_manifest or missing_from_runner:
        print("[FAIL] VerifierManifestVerifier: manifest and discovered verifiers differ")
        for name in sorted(missing_from_manifest):
            print(f"       - Missing manifest entry: {name}")
        for name in sorted(missing_from_runner):
            print(f"       - Missing discovered verifier: {name}")
        return 1

    selected = [verifier for verifier in verifier_instances if should_run(verifier, args)]
    if not selected:
        print("[verify] No verifiers selected.")
        return 1

    passed = 0
    failed = 0
    for verifier in selected:
        result = verifier.run(ROOT)
        if result.ok:
            passed += 1
            print(f"[PASS] {result.name}: {result.summary}")
        else:
            failed += 1
            print(f"[FAIL] {result.name}: {result.summary}")
            for message in result.details:
                print(f"       - {message}")

    print(f"[verify] Summary: {passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
