# Deep Agents Workshop — Interrupt 2026

A standalone notebook that walks through building a research agent from scratch using the [Deep Agents](https://github.com/langchain-ai/deepagents) framework.

## What You'll Learn

- Creating a basic Deep Agent with built-in filesystem and planning tools
- Adding custom tools (web search via Tavily)
- Understanding backends: StateBackend, FilesystemBackend, StoreBackend, CompositeBackend
- Delegating work to subagents for context isolation
- Writing custom middleware
- Human-in-the-loop approval for sensitive operations
- Long-term memory with path routing and per-user namespace scoping
- AGENTS.md for persistent agent identity
- Skills (SKILL.md) for on-demand capabilities with progressive disclosure

## Setup

**1. Clone the repo**
```zsh
git clone https://github.com/langchain-ai/interrupt26-deepagents.git
cd interrupt26-deepagents
```

**2. Install dependencies**
```zsh
uv sync
```

**2. Configure environment**
```zsh
cp .env.example .env
```
Fill in your API keys in `.env`. At minimum you need:
- `ANTHROPIC_API_KEY` (or swap to OpenAI/Gemini — see the model cell in the notebook)
- `TAVILY_API_KEY` — get one free at [tavily.com](https://tavily.com)

**3. Launch Jupyter**
```zsh
uv run jupyter notebook
```

Open `deep_agents_interrrup26.ipynb` and run the cells top to bottom.

## Model Providers

The notebook defaults to Anthropic. To switch, edit the model cell near the top — options for OpenAI and Google Gemini are included as comments.

## Notes

- Tested against `deepagents==0.5.3` and `langgraph==1.1.9`
- Backend factories use the current API (`StateBackend()`, `StoreBackend(store=...)`) — no runtime argument needed
