from typing import TypedDict, Annotated, List, Dict, Any

class AgentState(TypedDict):
    task_id: str
    user_query: str
    context: Dict[str, Any]
    plan: List[str]
    result: str
    status: str
    logs: List[str]
    next_agent: str
    current_step: str
    error: str
