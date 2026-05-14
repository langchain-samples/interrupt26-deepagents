"""
Standalone deep research agent.

Production-shaped port of the final notebook agent (Part 7 in deep_agent.ipynb):
- AGENTS.md is read from disk and always loaded into the system prompt
- Skills under ./skills/ are loaded on demand (progressive disclosure)
- /memories/* persists across threads via StoreBackend
- All other files live on disk in this project (sandboxed via virtual_mode=True)

Run directly (from the repo root):
    python agent/agent.py

Or import the compiled agent:
    from agent.agent import deep_agent
    result = deep_agent.invoke({"messages": [...]}, config={...})

This module exports `deep_agent` so it can be wired into `langgraph.json`
for `langgraph dev` and LangSmith Deployments.
"""

import sys
from pathlib import Path

# Make `utils.models` importable regardless of where this script is launched
# from. utils/ is a sibling of this agent/ folder.
AGENT_DIR = Path(__file__).parent
REPO_ROOT = AGENT_DIR.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from langchain.tools import tool
from tavily import TavilyClient
from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.memory import InMemoryStore

from deepagents import create_deep_agent
from deepagents.backends import (
    CompositeBackend,
    FilesystemBackend,
    StoreBackend,
)

from utils.models import model


# ---- Tools ----------------------------------------------------------------
tavily_client = TavilyClient()


@tool(parse_docstring=True)
def tavily_search(query: str) -> str:
    """Search the web for information on a given query.

    Args:
        query: Search query to execute
    """
    results = tavily_client.search(query, max_results=3, topic="general")
    chunks = [
        f"## {r['title']}\n**URL:** {r['url']}\n\n{r.get('content', '')}\n\n---\n"
        for r in results.get("results", [])
    ]
    return f"Found {len(chunks)} result(s) for '{query}':\n\n{''.join(chunks)}"


# ---- Backend --------------------------------------------------------------
# Default: real disk in this project (sandboxed). AGENTS.md and skills/* are
# loaded straight from disk via this backend.
# Route: /memories/* → StoreBackend for cross-thread persistence.
fs_backend = FilesystemBackend(root_dir=str(AGENT_DIR), virtual_mode=True)
backend = CompositeBackend(
    default=fs_backend,
    routes={"/memories/": StoreBackend()},
)


# ---- Agent ----------------------------------------------------------------

deep_agent = create_deep_agent(
    model=model,
    tools=[tavily_search],
    system_prompt="You are an expert research assistant.",
    memory=["./AGENTS.md"],  # always loaded into the system prompt
    skills=["./skills/"],  # loaded on demand via progressive disclosure
    backend=backend,
)
