from datetime import datetime

from pydantic import BaseModel

class EventCreate(BaseModel):
    name: str
    description: str | None = None
    start_time: datetime
    location: str

class EventResponse(BaseModel):
    id: int
    name: str
    description: str | None
    start_time: datetime
    location: str
    
    model_config = {
        "from_attributes": True
    }

class EventUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    start_time: datetime | None = None
    location: str | None = None