from pydantic import BaseModel
from datetime import datetime

class AttendanceSchema(BaseModel):
    user_id: int
    group_id: int
    event_id: int
    attendance_date: datetime
    attendance_time: datetime

    class Config:
        orm_mode = True
