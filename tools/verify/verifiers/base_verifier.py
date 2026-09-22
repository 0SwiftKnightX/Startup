from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class VerificationResult:
    name: str
    ok: bool
    summary: str
    details: list[str] = field(default_factory=list)


class BaseVerifier:
    name: str = "BaseVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        raise NotImplementedError("Verifier subclasses must implement run().")

    def resolve(self, repo_root: Path, relative_path: str) -> Path:
        return (repo_root / relative_path).resolve()

    def require_file(self, repo_root: Path, relative_path: str, result_name: str, details: list[str]):
        path = self.resolve(repo_root, relative_path)
        if not path.exists():
            details.append(f"Missing required file: {relative_path}")
            return False
        return True

    def require_dir(self, repo_root: Path, relative_path: str, result_name: str, details: list[str]):
        path = self.resolve(repo_root, relative_path)
        if not path.is_dir():
            details.append(f"Missing required directory: {relative_path}")
            return False
        return True

    def require_text(self, repo_root: Path, relative_path: str, needle: str, result_name: str, details: list[str]):
        path = self.resolve(repo_root, relative_path)
        if not path.exists():
            details.append(f"Missing required file for text check: {relative_path}")
            return False
        try:
            content = path.read_text(encoding="utf-8")
        except Exception as exc:  # pragma: no cover - defensive path
            details.append(f"Could not read {relative_path}: {exc}")
            return False
        if needle not in content:
            details.append(f"Expected text not found in {relative_path}: {needle}")
            return False
        return True
