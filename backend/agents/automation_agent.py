from backend.models.state import AgentState

class AutomationAgent:
    """
    Automation Agent performs side-effects like sending emails,
    scheduling calendar events, or modifying files.
    """
    def __init__(self):
        pass

    def run(self, state: AgentState) -> AgentState:
        state["current_step"] = "Automation"
        state["logs"].append("Automation Agent is executing tools.")
        
        # Dummy automation
        state["logs"].append("Automation actions completed successfully.")
        
        # Move to next agent in plan
        plan = state.get("plan", [])
        if "automation" in plan:
            plan.remove("automation")
        
        if plan:
            state["next_agent"] = plan[0]
        else:
            state["next_agent"] = "end"
            
        return state
