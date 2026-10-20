# Installing and invoking MineShelt

MineShelt is a *skills directory*, not an executable and not a Minecraft mod.

## 1. Obtain the repository

~~~bash
git clone https://github.com/skaletun/MineShelt.git
~~~

The folder to install is **MineShelt/mineshelt/**. Its name deliberately matches the lowercase name declared in SKILL.md.

## 2. Install in your agent

- Claude Code project: copy the mineshelt directory to PROJECT/.claude/skills/mineshelt/.
- Codex project: copy it to PROJECT/.agents/skills/mineshelt/.
- Other Agent Skills implementations: copy it to that tool's configured skills directory; confirm that the host recognizes skills and reads SKILL.md.
- When no skill discovery exists, explicitly instruct the agent to read mineshelt/SKILL.md and follow its reference links. This is a fallback, not automatic activation.

For example, from a Linux/macOS shell opened in the **target Minecraft mod project**:

~~~bash
mkdir -p .agents/skills
git clone https://github.com/skaletun/MineShelt.git /tmp/mineshelt-source
cp -R /tmp/mineshelt-source/mineshelt .agents/skills/mineshelt
~~~

For Windows PowerShell from the target project directory:

~~~powershell
git clone https://github.com/skaletun/MineShelt.git "$env:TEMP\MineShelt"
New-Item -ItemType Directory -Force .agents\skills | Out-Null
Copy-Item -Recurse -Force "$env:TEMP\MineShelt\mineshelt" ".agents\skills\mineshelt"
~~~

Do not copy the repository root as the skill directory: the Agent Skills name-matching convention expects the directory named mineshelt.

## 3. Supply the building environment

An agent can realize a building only through tools it genuinely has: source-control access to a mod, a Minecraft world interface, available WorldEdit-like tools, or another tool with placement access. The skill supplies judgment; it supplies **no game connection**. Specify or let the agent inspect:

- Java or Bedrock edition and Minecraft version;
- vanilla/modded availability and block registry;
- loader (NeoForge/Fabric/Forge) if modifying a Java mod;
- whether the task is in-world construction, a reusable authored structure asset, or worldgen integration;
- target site/biome, dimensions, protected area, expected visual references;
- test/screenshot capabilities.

If gameplay access is unavailable, request a **build-ready authored specification**, not fictional evidence of construction. For expert palette/landscape work, make screenshot access, Minecraft version, resource packs and terrain coordinates available where possible. References from external builders can be researched through browser/image search, but the skill does not ship redistributed copyrighted images or other builders' schematic assets.

## 4. Invoke

~~~text
Use MineShelt to act as a professional Minecraft builder. Inspect the
existing mod first. Design and implement a coastal lighthouse at the
specified site: a strong silhouette, honest support, restrained palette,
usable navigation and detailed surrounding terrain. Review screenshots
from all sides and refine before calling it complete.
~~~

Use Russian, English, or the project's language. The skill follows the user's communication language.

## 5. Recognizing successful use

A strong invocation results in an articulated design direction, version-safe block selection, an implementable construction method, a build or authored asset (when tools allow), screenshots/game checks when available, revisions responding to actual defects, and a clear accounting of verified versus unverified items.

## 6. Updates

Pull the latest repository and replace the installed mineshelt directory. Review the changelog in Git history before changing stable project constraints.
