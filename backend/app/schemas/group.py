from typing import Optional
from base import CustomBaseModel as BaseModel

class GroupCreateSchema(BaseModel):
    name: str
    description: Optional[str]

class GroupUpdateSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]

class GroupSchema(BaseModel):
    id: int
    name: str
    description: Optional[str]

    class Config:
        orm_mode = True
