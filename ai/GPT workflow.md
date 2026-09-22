<!-- MOVED: This GPT Workflow was originally created at the repository root as `GPT workflow.md`, then incorrectly placed in `aiLook/GPT workflow.md`. It has now been moved to `ai/GPT workflow.md`, which is the intended AI workflow location. -->

# GPT Workflow

## Meta Quest 3S AI-Assisted Development Integration

### Purpose

Startup will retain Godot + OpenXR + GitHub Actions as its primary application build architecture while adding Meta's current Meta VR tooling as the device-side development, deployment, debugging, and AI-agent integration layer.

This integration is intended to strengthen the existing workflow without introducing an unnecessary dependency on Android Studio.

### Architecture

```
GitHub Repository
      |
      v
GitHub Actions
      |
      v
Godot 4.7.2
      |
      v
Android / OpenXR Quest 3S APK
      |
      v
Meta VR CLI (metavr)
      |
      +--> Quest device management
      +--> APK installation / launch / stop
      +--> logs
      +--> screenshots
      +--> file operations
      +--> shell / ADB passthrough
      +--> performance traces
      +--> Meta documentation search
      +--> Meta 3D asset search
      +--> Store-related tooling
      |
      v
Meta VR MCP Server
      |
      v
AI coding agent
(Codex / GitHub Copilot CLI / other MCP-compatible agents)
```

Meta documents `metavr` as a single tool with both a terminal CLI and an MCP server. Both interfaces expose the same underlying Meta VR functionality. The MCP interface allows an AI coding agent to operate Quest development workflows through discovered tools.

Reference:
- Meta VR CLI overview: https://developers.meta.com/horizon/essentials/metavr-overview/
- Meta VR CLI installation: https://developers.meta.com/horizon/essentials/metavr-install/
- Meta AI tooling overview: https://developers.meta.com/horizon/essentials/ai-tooling-overview/
- Meta Quest Agentic Tools: https://github.com/meta-quest/agentic-tools

### Android Studio Requirement

Android Studio is NOT a required part of the Meta VR CLI + MCP architecture.

Meta provides `metavr` as a standalone CLI and MCP server. Meta's documentation identifies Android Studio as one optional surface that can bundle or expose the CLI, rather than a prerequisite for using the CLI itself.

For Startup:

- Do not migrate the project from Godot to Android Studio.
- Do not add Android Studio solely to obtain Meta VR CLI functionality.
- Prefer the standalone `metavr` installation and MCP integration.
- Continue using Godot 4.7.2 and GitHub Actions for the existing Godot Android build pipeline.
- Use Meta VR CLI/MCP for Quest-side device and development operations.
- Introduce additional Android tooling only when a verified project requirement makes it necessary.

### Project-Local MCP

Meta supports a project-local MCP configuration:

```bash
npx -y metavr mcp install project
```

This should be preferred for Startup when practical because the Meta VR tooling configuration remains associated with the repository/project rather than relying exclusively on a global agent configuration.

For Codex, Meta also documents:

```bash
npx -y metavr mcp install codex
```

For GitHub Copilot CLI, the Meta Quest Agentic Tools repository documents:

```bash
copilot plugin marketplace add meta-quest/agentic-tools
copilot plugin install meta-vr@meta-quest
```

The same repository provides the `metavr-cli` skill and additional Meta Quest/Horizon OS agent skills.

### Meta Quest Agentic Tooling Scope

The integration should account for the currently documented Meta VR tooling surface, not merely APK installation.

Relevant capabilities include:

1. Device discovery and connection
2. Device status and information
3. USB and Wi-Fi device workflows
4. APK installation
5. Application launch / stop / inspection
6. Application data management
7. Device file push / pull / listing
8. Device logs
9. Shell commands
10. ADB passthrough where required
11. Screenshot capture
12. UI interaction / automation where supported
13. Performance tracing and analysis
14. Meta documentation and API search
15. Meta 3D asset search
16. Developer-tool/environment diagnostics
17. Horizon OS / Quest-specific development skills
18. AI-agent access through MCP
19. Project-local MCP configuration
20. Future Meta VR tooling exposed by subsequent `metavr` releases, after verification

Do not implement or document unsupported capabilities as if they are already validated for Startup. Distinguish Meta-documented capability from Startup-verified capability.

### Agent Responsibilities

AI agents working on Startup should understand the separation between:

**Build layer**
- GitHub
- GitHub Actions
- Godot 4.7.2
- Android export
- OpenXR
- OpenXR Vendors
- Quest 3S APK

**Device layer**
- Meta VR CLI (`metavr`)
- Quest 3S device connection
- installation
- launch
- logs
- screenshots
- performance traces
- device inspection

**Agent layer**
- Codex
- GitHub Copilot CLI
- MCP-compatible coding agents
- Meta Quest Agentic Tools skills

The Meta VR agent integration must not replace the existing Godot architecture. It supplements the build and validation workflow.

### Physical Device Constraint

A GitHub Actions runner does not automatically have access to a physical Quest 3S located with the developer.

Before claiming an end-to-end automated Quest workflow, verify the actual host/device connection path:

```
AI agent
   |
MCP
   |
metavr host
   |
USB or supported network connection
   |
Quest 3S
```

Do not assume that an Android phone, GitHub Actions runner, or arbitrary cloud runner can serve as the physical `metavr` host without verification.

### Verification Policy

Before changing the repository architecture because of Meta tooling:

- Verify the current Meta documentation.
- Verify the installed `metavr` version and supported commands.
- Verify the agent/MCP configuration.
- Verify Quest 3S connectivity.
- Verify the generated APK on the actual target device.
- Record successful physical-device evidence separately from desktop/headless evidence.

Do not claim that a Quest deployment works merely because the APK builds.

---

# Copilot Implementation Prompt

Use the following prompt with GitHub Copilot when adapting Startup to the Meta VR tooling integration.

```text
@GitHub Copilot

STARTUP — META VR CLI / MCP INTEGRATION

Repository:
0SwiftKnightX/Startup

OBJECTIVE

Adapt the project's AI-assisted development workflow to incorporate Meta's current Meta VR tooling for Quest 3S development.

Meta now provides Meta VR CLI (metavr) as a standalone command-line tool and MCP server. The MCP server allows compatible AI coding agents to operate the same Meta VR capabilities through tools.

Official references:

- https://developers.meta.com/horizon/essentials/metavr-overview/
- https://developers.meta.com/horizon/essentials/metavr-install/
- https://developers.meta.com/horizon/essentials/ai-tooling-overview/
- https://github.com/meta-quest/agentic-tools

IMPORTANT ARCHITECTURE RULE

Do NOT migrate Startup from Godot to Android Studio.

Do NOT add Android Studio merely to obtain Meta VR functionality.

Meta VR CLI is independently available through the standalone CLI and MCP interfaces. Android Studio is an optional tooling surface, not a prerequisite for this integration.

KEEP:

- Godot 4.7.2
- OpenXR
- OpenXR Vendors
- existing Quest 3S Android export preset
- existing GitHub Actions Android build workflow
- existing repository architecture

ADD / DOCUMENT:

- Meta VR CLI (metavr)
- Meta VR MCP server
- project-local MCP configuration where appropriate
- Meta Quest Agentic Tools / metavr-cli skill guidance
- Codex integration guidance
- GitHub Copilot CLI integration guidance
- Quest device deployment/debugging workflow
- physical-device verification requirements

RESEARCH FIRST

Before modifying files:

1. Read the current Meta VR CLI documentation.
2. Read the current meta-quest/agentic-tools repository documentation.
3. Inspect the existing Startup AI workflow documentation.
4. Inspect README.md.
5. Inspect CHANGELOG.md.
6. Inspect the existing Android Quest 3S workflow.
7. Determine the smallest professional documentation/configuration change required.
8. Do not duplicate an existing configuration.
9. Do not introduce Android Studio, Gradle, or other Android tooling unless the repository has a verified technical requirement for it.

MCP CONFIGURATION

Document the project-local option:

npx -y metavr mcp install project

Also document the Codex option when relevant:

npx -y metavr mcp install codex

For GitHub Copilot CLI, document Meta's current Agentic Tools installation path:

copilot plugin marketplace add meta-quest/agentic-tools
copilot plugin install meta-vr@meta-quest

Do not claim that these commands have been executed unless you actually execute and verify them.

METAVR CAPABILITIES TO DOCUMENT

Include the relevant Meta-documented capabilities:

- device discovery
- device connection
- device information/status
- USB/Wi-Fi workflows
- APK installation
- application launch
- application stop
- application inspection
- device file operations
- logs
- shell commands
- ADB passthrough where required
- screenshots
- UI automation where supported
- performance traces
- documentation/API search
- Meta 3D asset search
- developer environment diagnostics
- MCP access for AI coding agents

VERIFICATION BOUNDARY

Clearly distinguish:

A. Meta-documented capabilities
B. Startup configuration
C. Startup-tested capabilities
D. Physical Quest 3S evidence

Do not mark a feature as verified simply because Meta documents that the feature exists.

PHYSICAL QUEST REQUIREMENT

The GitHub Actions runner cannot automatically control a physical Quest 3S unless a separately verified device-access path exists.

Do not invent a cloud-to-Quest connection.

Document the required architecture as:

AI coding agent
    -> MCP
    -> metavr host
    -> USB or supported network connection
    -> Quest 3S

If the host/device path is not yet available, document it as pending rather than pretending it is complete.

DOCUMENTATION REQUIREMENTS

Update the appropriate GPT workflow documentation professionally.

Update README.md appropriately if the project workflow now includes Meta VR CLI/MCP.

Update CHANGELOG.md with a concise entry describing the Meta VR tooling integration/documentation.

Preserve the existing documentation style and Keep a Changelog structure.

Do not rewrite unrelated README or changelog sections.

CHANGELOG RULE

The changelog must accurately state what was actually changed.

Do not state that physical Quest 3S deployment, MCP connectivity, or metavr execution was verified unless it was actually tested.

If only documentation/configuration was added, say so.

README RULE

The README should clearly communicate:

- Godot remains the application/build engine.
- Quest 3S remains the target.
- Meta VR CLI/MCP is the device/agent tooling layer.
- Android Studio is optional and is not required for this integration.
- physical Quest validation remains separate from cloud/headless build validation.

QUALITY RULES

- Make the smallest correct changes.
- Do not modify unrelated project files.
- Do not create failing tests.
- Do not create placeholder implementations merely to satisfy this task.
- Do not claim successful deployment without evidence.
- Do not duplicate existing documentation.
- Follow existing repository naming and documentation conventions.
- Keep documentation technically precise.
- Use current Meta documentation as the authority for Meta-specific tooling.
- After making changes, inspect the resulting files for consistency and broken links.
- Report exactly what changed and what remains unverified.

FINAL REPORT

After implementation, report:

1. Files changed.
2. Meta VR tooling added/documented.
3. MCP configuration added/documented.
4. README changes.
5. CHANGELOG changes.
6. Tests/checks actually performed.
7. Physical Quest 3S steps that remain unverified.
8. Any dependency or environment requirement that still needs to be supplied.
```

## Maintenance Rule

Whenever Meta changes `metavr`, its MCP interface, or the Meta Quest Agentic Tools repository, update this workflow only after verifying the current official documentation.

The repository should treat Meta VR tooling as an evolving external development toolchain, not as a permanent hard-coded assumption.
