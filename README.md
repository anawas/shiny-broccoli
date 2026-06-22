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

## Adding plugins

### Claude

```
claude plugin install superpowers@claude-plugins-official --scope project
```

### Pi

```
pi install npm:pi-sdsc-vllm --local
```

### Codex

No support for local-only plugins. Plugins have to be installed at the user level.
Then they have to be disabled at the user level and re-enabled at the project level.
For best results it is best to add the plugin add command in an init script.

## Adding skills

### Claude

Skills can be added to `.claude/skills/`

### Pi

Skills can be added to `.pi/skills`

### Codex

Skills can be added to `.agents/skills`

