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


## Agent Working Identity

- Every AI entering Startup assigns itself a working name before substantive work.
- The AI must not inherit or impersonate the signer of the handoff it reads.
- Check recent handoffs/worklogs for collisions before signing.
- If the chosen name already exists, use a distinct suffix such as #2 or #3.
- Record the working name and project function in worklogs, audits, and handoffs.
- Record exact UTC time plus America/New_York Eastern Time with EDT/EST and UTC offset.

## Reference and Code Reuse

- Public visibility is not automatic permission to copy code or assets.
- Inspect the source license and any path-specific notices before reuse.
- Preserve required copyright/license/attribution notices.
- Record source, path, commit/release, license, and reused scope when material is actually copied.
- If licensing or permission is unclear, do not copy the material.
- Prefer proven compatible implementations when legally reusable, rather than unnecessary reinvention.
