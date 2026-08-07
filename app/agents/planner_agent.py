from typing import Dict, Any
from app.models.state import AgentState

class PlannerAgent:
    """
    Planner Agent is responsible for taking the user query and context,
    and generating a step-by-step execution plan for the other agents.
    """
    def __init__(self):
        pass

    def run(self, state: AgentState) -> AgentState:
        state["current_step"] = "Planning"
        state["logs"].append("Planner Agent is creating an execution plan.")
        
        # Simple dummy plan logic for now
        query = state.get("user_query", "").lower()
        plan = []
        
        if "analyze" in query or "fraud" in query:
            plan = ["research", "analysis", "decision"]
        else:
            plan = ["research", "analysis"]
            
        state["plan"] = plan
        state["logs"].append(f"Generated plan: {plan}")
        
        # Route to the first step in the plan
        if plan:
            state["next_agent"] = plan[0]
        else:
            state["next_agent"] = "end"
            
        return state
