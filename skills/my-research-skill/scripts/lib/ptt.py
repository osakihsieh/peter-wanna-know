"""PTT search via web-search backends (Brave, Serper, etc.).

Uses site:ptt.cc to discover relevant discussions from the last 30 days.
"""

from __future__ import annotations
from typing import Any, Dict, List, Tuple

from . import grounding, log

def _log(msg: str):
    log.source_log("PTT", msg)

def search_ptt(
    topic: str,
    date_range: Tuple[str, str],
    config: Dict[str, Any],
    depth: str = "default",
    web_backend: str = "auto",
) -> List[Dict[str, Any]]:
    """Search PTT via web search with site:ptt.cc filter."""
    query = f"site:ptt.cc {topic}"
    _log(f"Searching PTT for '{topic}' via {web_backend} backend")
    
    # We use grounding.web_search but customize the results
    items, _ = grounding.web_search(query, date_range, config, backend=web_backend)
    
    # Re-map IDs and labels
    for i, item in enumerate(items):
        item["id"] = f"PTT{i+1}"
        item["why_relevant"] = f"PTT discussion: {topic}"
        item["source_domain"] = "ptt.cc"
        
    return items
