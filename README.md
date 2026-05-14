# Deep Agents Workshop — Interrupt 2026

A workshop on building a research agent from scratch with the [Deep Agents](https://github.com/langchain-ai/deepagents) framework. The repo ships both an **interactive notebook** that walks through the concepts step by step and a **standalone agent** wired up for LangSmith Studio.

## What You'll Learn

- Creating a basic Deep Agent with built-in filesystem and planning tools
- Adding custom tools (web search via Tavily)
- Understanding backends (`StateBackend`, `FilesystemBackend`, `StoreBackend`, `CompositeBackend`)
- Delegating work to subagents for context isolation
- Human-in-the-loop approval for sensitive operations
- Long-term memory with `/memories/*` routing across threads
- AGENTS.md for persistent agent identity (always loaded)
- Skills (SKILL.md) for on-demand capabilities via progressive disclosure

## Setup

**1. Clone the repo**

```zsh
git clone https://github.com/langchain-samples/interrupt26-deepagents.git
cd interrupt26-deepagents
```

**2. Install dependencies**
Install the [uv package manager](https://docs.astral.sh/uv/getting-started/installation/) if it is not already installed.

```zsh
uv sync
```

**3. Configure environment**

```zsh
cp .env.example .env
```

Fill in your API keys in `.env`. At minimum:

- `OPENAI_API_KEY` (default models: `gpt-5.4` main agent, `gpt-5.4-mini` subagent — or swap providers in `utils/models.py`)
- `TAVILY_API_KEY` - free at [tavily.com](https://tavily.com)

Optional but recommended:

- `LANGSMITH_API_KEY` + `LANGSMITH_TRACING=true` for full trace observability

If anything looks off (wrong Python, missing keys, env-var conflicts), run the bundled diagnostic:

```zsh
uv run python env_utils.py
```

## Run it

### A. Walk through the notebook

```zsh
uv run jupyter lab
```

Open `deep_agent.ipynb` and run the cells top to bottom. The 8 parts each take ~30s to a couple of minutes to execute.

### B. Run the agent in LangSmith Studio

The repo ships a production-shaped agent at `agent/agent.py`, wired up via `langgraph.json`. Start the local LangGraph API + Studio with one command:

```zsh
uv run langgraph dev
```

You'll see something like:

```
- 🚀 API:        http://127.0.0.1:2024
- 🎨 Studio UI:  https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

Open the Studio URL in a browser. The **Deep Agent** graph appears in the sidebar. From there you can:

- Chat with the agent and watch each tool call land in real time
- Inspect intermediate state, the virtual filesystem, and the agent's todo list
- Step through threads, fork them, and edit messages mid-conversation
- See `/memories/*` files persist across threads — `langgraph dev` provides the checkpointer + store automatically

When you're ready to deploy, `langgraph.json` is already shaped for [LangSmith Deployments](https://docs.langchain.com/langgraph-platform/cloud) — you can use our `langgraph-cli` to deploy your agent directly from your terminal using `uv run langgraph deploy`

## Model providers

The default model is OpenAI (`gpt-5.4` for the main agent, `gpt-5.4-mini` for the research subagent in Part 4). To switch, edit `utils/models.py` — commented-out sections are included for Anthropic, Azure OpenAI, AWS Bedrock, and Google Vertex AI (Gemini). For non-default providers, install the matching extra:

```zsh
uv sync --extra azure     # Azure OpenAI
uv sync --extra bedrock   # AWS Bedrock
uv sync --extra google    # Google Vertex AI
```
