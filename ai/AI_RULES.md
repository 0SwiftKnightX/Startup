# AI Rules and Regulations

## Purpose

These rules govern AI-assisted work in this repository. They apply to GPT,
GitHub Copilot, Gemini, and any other automated coding agent.

## Required Behavior

1. Read the root README and relevant documents in `docs/` before changing code.
2. State the local hypothesis, affected code path, and cheapest useful check
   before making a substantive change.
3. Preserve user changes and never use destructive Git commands without explicit
   approval.
4. Make the smallest change that solves the identified problem.
5. Prefer repository conventions and existing Godot/XR abstractions.
6. Never claim a test, device run, or validation result that was not performed.
7. Distinguish static inspection, headless CI, PCVR, and physical Quest evidence.
8. Record important changes in the appropriate worklog and update the changelog
   when repository structure or user-facing behavior changes.
9. Use exact UTC timestamps for signed worklog and audit entries.
10. Keep secrets, credentials, tokens, and private user data out of the repo.

## Validation Rules

- Run a focused executable check after the first substantive edit when one is
  available.
- Run at least one post-edit executable validation before completion.
- Treat warnings separately from failures, but do not hide failures.
- Physical Quest validation requires a real headset test and recorded evidence.

## Documentation Rules

- Current truth belongs in `README.md` or the relevant `docs/` file.
- Historical records belong in `docs/HISTORICAL_GPT_LOG.md` or
  `docs/AUDIT_ARCHIVE.md`.
- Active agent activity belongs in the corresponding `*_WORKLOG.md` file.
- Corrections are appended to historical records; old evidence is not silently
  rewritten.

## Identity and Signatures

An agent must sign worklog or audit entries with its actual tool identity. Do not
invent a human identity, claim another agent's work, or imply physical testing
was performed by the agent.
