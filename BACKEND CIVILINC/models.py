from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Project(BaseModel):
    id: Optional[int] = None
    title: str
    department: str
    status: str # e.g., "planned", "in-progress", "completed", "on-hold"
    budget: float
    start_date: date
    end_date: date
    description: Optional[str] = None
    assigned_engineers: List[str] = []

class Complaint(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    status: str # e.g., "pending", "in-progress", "resolved"
    date: date
    category: str
    assigned_officer: Optional[str] = None 