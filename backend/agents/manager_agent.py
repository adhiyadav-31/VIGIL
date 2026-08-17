from typing import Dict, Any
from backend.models.state import AgentState

class ManagerAgent:
    """
    Manager Agent acts as the entry point and router for the Agentic workflow.
    It reads the state, identifies the task, and routes it to the PlannerAgent.
    """
    def __init__(self):
        pass

    def run(self, state: AgentState) -> AgentState:
        state["current_step"] = "Manager Analysis"
        state["logs"].append("Manager Agent started processing task.")
        
        # Simple routing logic: send to planner
        state["next_agent"] = "planner"
        state["status"] = "in_progress"
        state["logs"].append("Manager Agent delegated to Planner Agent.")
        
        return state
