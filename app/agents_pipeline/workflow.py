from langgraph.graph import StateGraph, END
from app.models.state import AgentState
from app.agents.manager_agent import ManagerAgent
from app.agents.planner_agent import PlannerAgent
from app.agents.research_agent import ResearchAgent
from app.agents.analysis_agent import AnalysisAgent
from app.agents.automation_agent import AutomationAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.memory_agent import MemoryAgent

def build_workflow():
    workflow = StateGraph(AgentState)

    manager = ManagerAgent()
    planner = PlannerAgent()
    research = ResearchAgent()
    analysis = AnalysisAgent()
    automation = AutomationAgent()
    decision = DecisionAgent()
    memory = MemoryAgent()

    # Define nodes
    workflow.add_node("manager", manager.run)
    workflow.add_node("planner", planner.run)
    workflow.add_node("research", research.run)
    workflow.add_node("analysis", analysis.run)
    workflow.add_node("automation", automation.run)
    workflow.add_node("decision", decision.run)
    workflow.add_node("memory", memory.run)

    # Set entry point
    workflow.set_entry_point("manager")

    # Define simple routing logic
    def route(state: AgentState):
        next_agent = state.get("next_agent")
        if not next_agent or next_agent == "end":
            return END
        return next_agent

    # Add conditional edges
    agents = ["manager", "planner", "research", "analysis", "automation", "decision", "memory"]
    for agent in agents:
        workflow.add_conditional_edges(
            agent,
            route,
            {
                "manager": "manager",
                "planner": "planner",
                "research": "research",
                "analysis": "analysis",
                "automation": "automation",
                "decision": "decision",
                "memory": "memory",
                END: END
            }
        )

    return workflow.compile()
