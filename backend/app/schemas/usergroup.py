from pydantic import BaseModel

class UserGroupSchema(BaseModel):
    user_id: int
    group_id: int
    role_id: int

    class Config:
        orm_mode = True
