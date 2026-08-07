"""
Daily Check-in submission. Feeds the Memory Agent / Analysis Agent with
fresh operational signals between full analyses.
"""
from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel, Field
import json
import os
from datetime import datetime

router = APIRouter(prefix="/api/checkin", tags=["checkin"])


class CheckinPayload(BaseModel):
    sales: float = Field(0.0, description="Sales today in INR")
    complaints: int = Field(0, description="Customer complaints count")
    delays: str = Field("None", description="Supplier delays reported")
    inventory: str = Field("None", description="Inventory status")
    attendance: float = Field(100.0, description="Employee attendance percentage")
    expenses: float = Field(0.0, description="Unexpected expenses in INR")
    competitors: str = Field("No", description="New competitors noticed")
    marketchange: Optional[str] = None
    feedback: Optional[str] = None
    notes: Optional[str] = None
    status: str = "submitted"


@router.post("")
@router.post("/")
@router.get("")
async def submit_checkin(payload: CheckinPayload = None, business_id: str = "default"):
    if payload is None:
        payload = CheckinPayload()

    os.makedirs("data", exist_ok=True)
    file_path = "data/checkins.json"
    
    checkins = []
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                checkins = json.load(f)
        except Exception:
            pass
            
    record = payload.model_dump()
    record["business_id"] = business_id
    record["timestamp"] = datetime.now().isoformat()
    checkins.append(record)
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(checkins, f, indent=2)

    # invalidate dashboard cache for this business_id
    try:
        from app.core.cache import invalidate_prefix
        invalidate_prefix(f"dashboard:{business_id}")
    except Exception:
        pass
    
    return {
        "ok": True,
        "status": payload.status,
        "submitted_at": record["timestamp"],
        "total_checkins": len(checkins),
        "message": "Daily check-in recorded successfully.",
    }

