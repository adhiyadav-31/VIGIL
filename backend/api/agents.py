"""
API endpoint for the AI Decision Board.
GET  /api/agents       -> returns the list of specialist agents for the UI
POST /api/agents/run   -> streams the LangGraph orchestrator execution via SSE
"""
import json
import uuid
from typing import AsyncGenerator

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

router = APIRouter(prefix="/api/agents", tags=["agents"])


class AgentRunRequest(BaseModel):
    user_query: str
    business_id: str = "default"


# ── The 8 specialist agents that power the AI Decision Board ──
AGENT_CARDS = [
    {"name": "Finance Agent",   "color": "#1FAE6E", "icon": "₹", "status": "Active", "confidence": 91,
     "recommendation": "Delay machinery purchase by one quarter",
     "reasoning": "Current debt-service ratio leaves limited buffer for new fixed costs.", "risk": "Moderate"},
    {"name": "Risk Agent",      "color": "#E14B4B", "icon": "⚠", "status": "Active", "confidence": 95,
     "recommendation": "Escalate distress risk monitoring to daily",
     "reasoning": "Risk score crossed the 30% moderate threshold this week.", "risk": "High"},
    {"name": "Competitor Agent", "color": "#E68A1C", "icon": "◎", "status": "Active", "confidence": 74,
     "recommendation": "Benchmark pricing against local peers",
     "reasoning": "Peer revenue median is 12% higher at similar scale.", "risk": "Low"},
    {"name": "Scheme Agent",    "color": "#B45309", "icon": "🏛", "status": "Active", "confidence": 85,
     "recommendation": "Apply for MSME Credit Guarantee Scheme",
     "reasoning": "Business profile matches 4 of 5 eligibility criteria.", "risk": "Low"},
    {"name": "Recovery Agent",  "color": "#7C5CE0", "icon": "↻", "status": "Active", "confidence": 82,
     "recommendation": "Execute 30-day cash stabilization plan",
     "reasoning": "Receivables recovery this week could add up to 18 days of runway.", "risk": "Moderate"},
    {"name": "Growth Agent",    "color": "#0EA5A0", "icon": "↗", "status": "Active", "confidence": 68,
     "recommendation": "Pilot a small export shipment",
     "reasoning": "Market opportunity score for exports rose 14 points this month.", "risk": "Low"},
    {"name": "CEO Agent",       "color": "#2952E3", "icon": "◆", "status": "Active", "confidence": 88,
     "recommendation": "Prioritize receivables recovery before new hiring",
     "reasoning": "Cash runway is the binding constraint this quarter.", "risk": "Moderate"},
    {"name": "Operations Agent","color": "#3DDCEE", "icon": "⚙", "status": "Active", "confidence": 82,
     "recommendation": "Diversify supplier base for top 3 SKUs",
     "reasoning": "Single-supplier dependency has caused 2 delays in 30 days.", "risk": "Moderate"},
]


@router.get("")
async def get_agents():
    """Returns the list of specialist agents for the frontend AI Decision Board."""
    return {"items": AGENT_CARDS}


@router.post("/run")
async def run_agent_board(request: AgentRunRequest):
    """
    Execute the real LangGraph orchestrator and stream each node's output
    back to the client in real-time using Server-Sent Events (SSE).

    The graph runs:  finance -> risk -> competitor -> schemes -> recovery -> growth -> ceo
    """
    from backend.agents.orchestrator import build_graph, AgentState

    graph = build_graph()

    initial_state: AgentState = {
        "business_id": request.business_id,
        "user_query": request.user_query,
        "business_profile": {},
        "plan": [],
        "retrieved_documents": [],
        "specialist_outputs": {},
        "final_recommendation": {},
        "memory_written": False,
    }

    async def event_generator() -> AsyncGenerator[str, None]:
        try:
            # LangGraph async graph requires .astream() instead of sync .stream()
            async for step_output in graph.astream(initial_state):
                for node_name, state in step_output.items():
                    # Extract the specialist output for this node
                    specialist = state.get("specialist_outputs", {}).get(node_name, {})
                    final_rec = state.get("final_recommendation", {})

                    payload = {
                        "node": node_name,
                        "agent": specialist.get("agent", node_name.title() + " Agent"),
                        "status": "completed",
                        "specialist_output": specialist,
                    }

                    # If this is the CEO node, include the final recommendation
                    if node_name == "ceo" and final_rec:
                        payload["final_recommendation"] = final_rec

                    yield f"data: {json.dumps(payload, default=str)}\n\n"

            yield f"data: {json.dumps({'status': 'completed', 'message': 'All agents finished.'})}\n\n"
        except Exception as e:
            logger.exception("Agent graph execution failed")
            yield f"data: {json.dumps({'status': 'error', 'message': str(e)})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
