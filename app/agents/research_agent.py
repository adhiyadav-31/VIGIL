from app.models.state import AgentState
from app.rag.retriever import Retriever

class ResearchAgent:
    """
    Research Agent queries the RAG system and internal knowledge base
    to gather relevant context for the task.
    """
    def __init__(self):
        self.retriever = Retriever()

    def run(self, state: AgentState) -> AgentState:
        state["current_step"] = "Research"
        state["logs"].append("Research Agent is gathering context.")
        
        query = state.get("user_query", "")
        if query:
            # Actually retrieve documents using the RAG module
            docs = self.retriever.retrieve(query=query, k=3)
            retrieved_info = []
            for doc in docs:
                for chunk in doc.chunks:
                    retrieved_info.append(f"[{doc.filename}] {chunk.text}")
                    
            state["context"]["retrieved_docs"] = retrieved_info
            state["logs"].append(f"Research completed. Found {len(retrieved_info)} relevant chunks.")
        else:
            state["logs"].append("No query provided for research.")
        
        # Move to next agent in plan
        plan = state.get("plan", [])
        if "research" in plan:
            plan.remove("research")
        
        if plan:
            state["next_agent"] = plan[0]
        else:
            state["next_agent"] = "end"
            
        return state
