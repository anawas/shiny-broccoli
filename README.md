# Using Coding Agents in Renku

The way to install an agent in Renku is to use an environment build from code.
In the repo that is used to build your image add a `project.toml` file.

See the `project.toml` file for example.

Currently we support pi, claude and codex.

## Picking up custom configurations

We will also pick up agent-specific configurations from the repository.
This by reading the specific folders that contain custom configuration for each agent:
- Claude: `.claude` folder with custom configuration
- Pi: `.pi` folder with custom configuration
- Codex: `.codex` file with custom configuration

When we find any of the folders we will include them in your Renku session.
This should allow you to install skills and/or plugins.

NOTE: Out-of-the box support for skills in `codex` is currently not available. 
We currently do not pick up the `.agents` folder that is expected by `codex`.
You can bypass this limitation by adding an init script that will copy the skills
from another location into `.agents/skills` so that `codex` can see the skills.