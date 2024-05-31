from pydantic import BaseModel, EmailStr, constr
from typing import Optional, List
from usergroup import UserGroupSchema
from attendance import AttendanceSchema

class UserCreateSchema(BaseModel):
    username: constr(min_length=4, max_length=20, regex="^[a-zA-Z0-9]+$")
    email: EmailStr
    password: constr(min_length=8, max_length=20, regex="^(?=.*[A-Z])(?=.*[!@#$%^&*]).+$")

class UserUpdateSchema(BaseModel):
    username: Optional[constr(min_length=4, max_length=20, regex="^[a-zA-Z0-9]+$")]
    email: Optional[EmailStr]
    password: Optional[constr(min_length=8, max_length=20, regex="^(?=.*[A-Z])(?=.*[!@#$%^&*]).+$")]

class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    groups: List[UserGroupSchema] = []
    attendances: List[AttendanceSchema] = []

    class Config:
        orm_mode = True
