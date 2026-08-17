from backend.models.state import AgentState

class DecisionAgent:
    """
    Decision Agent reviews the analysis, creates confidence scores,
    and formats the final decision/recommendation.
    """
    def __init__(self):
        pass

    def run(self, state: AgentState) -> AgentState:
        state["current_step"] = "Decision"
        state["logs"].append("Decision Agent is validating output and creating final decision.")
        
        # Dummy decision
        state["result"] = state.get("result", "") + "\nFinal Decision: Approved."
        state["status"] = "completed"
        state["logs"].append("Decision finalized.")
        
        # Move to next agent in plan
        plan = state.get("plan", [])
        if "decision" in plan:
            plan.remove("decision")
        
        if plan:
            state["next_agent"] = plan[0]
        else:
            state["next_agent"] = "end"
            
        return state
