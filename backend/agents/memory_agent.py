from backend.models.state import AgentState

class MemoryAgent:
    """
    Memory Agent stores learnings, preferences, and task outcomes 
    to be used for future interactions.
    """
    def __init__(self):
        pass

    def run(self, state: AgentState) -> AgentState:
        state["current_step"] = "Memory"
        state["logs"].append("Memory Agent is storing task results.")
        
        import json
        import os

        # Dummy memory storage
        state["logs"].append("Results committed to memory.")
        
        # Load the latest check-in data to inject into state
        file_path = "data/checkins.json"
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    checkins = json.load(f)
                    if checkins:
                        latest = checkins[-1]
                        state["logs"].append(f"Loaded latest check-in data from {latest.get('timestamp')}")
                        state["context"] = state.get("context", "") + f"\n\nLatest Daily Check-in Data:\n{json.dumps(latest, indent=2)}\n"
            except Exception as e:
                state["logs"].append(f"Failed to load check-ins: {e}")
        
        # Move to next agent in plan
        plan = state.get("plan", [])
        if "memory" in plan:
            plan.remove("memory")
        
        if plan:
            state["next_agent"] = plan[0]
        else:
            state["next_agent"] = "end"
            
        return state
