<div align="right">Project Handoff Protocol — Version 1.0</div>

# Project Startup Handoff Template — Version 1.0

## Purpose

This template is the formal handoff protocol for an AI entering or continuing the
Startup project.

**Startup is the game/XR project. The Standalone AI is a separate project.**

The Project Bible governs durable project intent. This template governs the transfer
of project context between AI sessions. Individual handoffs are saved separately
under:

`Project Bible/Handoffs/`

## 1. Handoff Metadata

Every handoff file must begin with:

- **Date:** YYYY-MM-DD
- **Time:** HH:MM:SS and timezone/UTC offset
- **Title:** concise description of the handoff
- **Signed by:** AI name / agent name
- **Handoff Template Version:** Version X.Y

Recommended filename:

`Project Startup Handoff - YYYY-MM-DD - HHMM - Short Title.md`

Rules:

- Use a stable, human-readable title.
- Preserve the date and time of the actual handoff.
- Preserve the signing AI's name exactly as used for the handoff.
- Do not overwrite an older handoff.
- Every completed handoff receives its own file.
- A new protocol version receives a new template file rather than silently replacing an old template.

## 2. Version Placement

The protocol version appears twice.

### Top

Place the protocol version at the top-right of the document:

`<div align="right">Project Handoff Protocol — Version 1.0</div>`

The top indicator identifies which template/protocol governs the document.

### Bottom

Place the same version indicator at the bottom-right:

`<div align="right">Handoff Protocol Version 1.0</div>`

The bottom indicator makes the version visible when reviewing the end of a handoff.

The top and bottom version indicators must match.

## 3. Entry Rule

The incoming AI must:

1. Read the Project Bible.
2. Read this Handoff Template.
3. Read the applicable most-recent handoff record(s).
4. Inspect the current repository state.
5. Audit the AI/tool/plugin environment separately.
6. Produce a read-only Startup Entry Audit.
7. Present findings and available work avenues.
8. Obtain user authorization for the requested work.
9. Only then modify the repository.

No repository modification is authorized merely because an AI has entered the project.

## 4. Required Boundary

Do not merge Startup with the Standalone AI.

Do not transfer the Standalone AI's memory architecture, application architecture,
or identity into Startup without explicit owner authorization for a specific integration.

## 5. Required Startup Entry Audit

Before implementation, summarize:

### Repository
- Current branch
- Current HEAD
- Recent meaningful activity
- Working-tree/repository state where available

### Project
- What is implemented
- What is partial
- What is missing
- What is unknown
- What is broken
- What is duplicated
- What is planned

### Code / Integration Findings
- Parse or syntax failures
- Scene/script mismatches
- Contract mismatches
- Broken references
- Unresolved verifier failures
- CI/build problems
- Dependency mismatches
- Existing failure states

### Verification
- What is statically verified
- What is CI verified
- What is runtime verified
- What is Quest verified
- What remains unverified

### Recent Activity
- What the previous project work was
- What changed
- What remains unfinished
- What evidence supports the current state

### Interesting Findings
Record meaningful discoveries, suspicious inconsistencies, reusable systems,
architecture opportunities, or important missing pieces without turning observations
into unsupported conclusions.

## 6. AI Environment Audit

Keep project state and AI-environment state separate.

Audit:

**Features → Tools → Plugins/Apps → Plugin Definitions → Functions →
Function Definitions → Skills → Skill Definitions → Connection →
Account Connection → Authorization → Actual Verification**

Do not treat:

- tool exposure as plugin connection;
- plugin existence as authorization;
- function metadata as successful execution;
- skill existence as skill verification.

For every important capability record:

- Definition
- Installed/exposed state
- Connection state
- Authorization state
- Functions
- Skills
- Required user action
- Actual exercise result
- Verification result
- Limitations

## 7. Work Avenues

After the entry audit, present independent work avenues such as:

- XR foundation
- Gameplay
- Vehicles
- World/environment
- NPCs/creatures
- Inventory/items/economy
- AI/spatial systems
- Persistence
- Verification/CI
- Performance/Quest
- Infrastructure
- Research
- Custom scope

The AI should inform the owner of the available avenues rather than silently choosing
the project direction.

## 8. Authorization Handshake

Once the owner chooses a work area:

1. State the selected scope.
2. Summarize relevant current state.
3. Identify dependencies.
4. Identify unresolved blockers.
5. Identify intended files/systems.
6. State what will not be changed.
7. Ask for authorization when required.
8. Modify only the authorized scope.
9. Verify the result.
10. Record the completed work and remaining work.

## 9. Operating Sequence

**HANDOFF → AUDIT → UNDERSTAND → VERIFY → CONTINUE**

Expanded:

**PRESERVE → INSPECT → UNDERSTAND → PLAN → MODIFY → VERIFY**

## 10. Evidence Rule

Never equate code existence with working functionality.

Use:

- DESIGN
- IMPLEMENTED
- STATIC VERIFIED
- CI VERIFIED
- RUNTIME VERIFIED
- QUEST VERIFIED
- PRODUCTION VERIFIED

Use precise status labels:

- IMPLEMENTED — verified by [evidence]
- IMPLEMENTED — static only
- PARTIAL
- PLANNED
- UNKNOWN
- FAILED
- BLOCKED
- UNVERIFIED

## 11. Change Governance

Unless explicitly authorized, do not independently:

- delete files;
- rename files;
- restructure the repository;
- replace architecture;
- add/remove major dependencies;
- change Godot or XR versions;
- change Android export architecture;
- change CI architecture;
- weaken or remove verification;
- bypass failed validation;
- claim physical Quest functionality without physical evidence.

## 12. Handoff Record

Every completed handoff must be preserved as its own file in:

`Project Bible/Handoffs/`

A handoff record should contain:

1. Date
2. Time
3. Title
4. Signing AI name
5. Template/protocol version
6. Repository/project identity
7. Purpose of the handoff
8. Relevant state transferred
9. Findings or unresolved issues
10. Work completed, if any
11. Verification state
12. Remaining work
13. Authorization/ownership notes
14. Next handoff or continuation state

Do not overwrite historical handoffs.

## 13. Template Versioning

Version progression:

- Version 1.0 — initial protocol
- Version 1.1 — additive/refinement change
- Version 1.2 — additional refinement
- Version 2.0 — major protocol change

When a protocol changes:

1. Preserve all older template files.
2. Create a new versioned template file.
3. Update references that should point to the new active template.
4. Do not rewrite historical handoffs to pretend they used the newer protocol.
5. Record the protocol change in the project documentation/change history.

A handoff must identify the exact template version used.

## 14. Project Bible Relationship

The Project Bible and Handoff system are associated as a pair:

**Project Bible**
→ defines durable project rules and intent.

**Handoff Template**
→ defines how AI context is transferred.

**Handoff Records**
→ preserve individual transfers over time.

Current project state may also appear in worklogs, changelogs, audit files,
conversation logs, validation reports, and other evidence. The handoff does not
attempt to duplicate the entire project state.

## 15. Completion Rule

A handoff is complete only when the incoming/outgoing AI has clearly identified:

- what project is being entered;
- what project is excluded;
- what repository is authoritative;
- what the current state is;
- what was recently worked on;
- what remains unresolved;
- what is verified;
- what is unknown;
- what the user wants to work on;
- what scope is authorized;
- what must not be changed;
- what happens next.

<div align="right">Handoff Protocol Version 1.0</div>
