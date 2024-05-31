from datetime import datetime
from typing import Optional
from base import CustomBaseModel as BaseModel

class EventCreateSchema(BaseModel):
    name: str
    description: Optional[str]
    datetime: datetime
    location: Optional[str]
    group_id: int
    duration: Optional[int]  # Duration in minutes

class EventUpdateSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    datetime: Optional[datetime]
    location: Optional[str]
    duration: Optional[int]

class EventSchema(BaseModel):
    id: int
    name: str
    description: Optional[str]
    datetime: datetime
    location: Optional[str]
    group_id: int
    duration: Optional[int]

    class Config:
        orm_mode = True
