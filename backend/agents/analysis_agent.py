from backend.models.state import AgentState

class AnalysisAgent:
    """
    Analysis Agent processes data, performs statistical analysis,
    and handles specific domain logic like MSME lending or fraud.
    """
    def __init__(self):
        pass

    def run(self, state: AgentState) -> AgentState:
        state["current_step"] = "Analysis"
        state["logs"].append("Analysis Agent is processing the data.")
        
        # Dummy analysis
        state["result"] = "Initial analysis complete."
        state["logs"].append("Analysis completed.")
        
        # Move to next agent in plan
        plan = state.get("plan", [])
        if "analysis" in plan:
            plan.remove("analysis")
        
        if plan:
            state["next_agent"] = plan[0]
        else:
            state["next_agent"] = "end"
            
        return state
