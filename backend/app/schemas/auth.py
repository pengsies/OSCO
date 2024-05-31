from pydantic import EmailStr, constr
from typing import Optional
from base import CustomBaseModel
from datetime import datetime

# Validators
valid_username = constr(min_length=4, max_length=20, regex="^[a-zA-Z0-9]+$")
valid_password = constr(min_length=8, max_length=20, regex="^(?=.*[A-Z])(?=.*[!@#$%^&*]).+$")

# Schemas
class AccountRegisterSchema(CustomBaseModel):
    username: valid_username
    student_id: str
    email: EmailStr
    password: valid_password
    repeat_password: valid_password
    created_at: Optional[datetime] = None


class AccountCreateSchema(CustomBaseModel):
    username: valid_username  # type: ignore
    password: str

class AccountUpdatePasswordSchema(CustomBaseModel):
    before_password: Optional[valid_password]
    password: Optional[valid_password]
    repeat_password: Optional[valid_password]
    updated_at: Optional[datetime] = None

class AccountSchema(AccountRegisterSchema):
    user_id: Optional[int]
    repeat_password: Optional[str]

class AccountUpdateEmailSchema(CustomBaseModel):
    new_email: EmailStr
    updated_at: Optional[datetime] = None

class AccountCredentialsSchema(CustomBaseModel):
    username: str
    email: EmailStr
    password: str
    user_id: int
    student_id: str

class CurrentUserSchema(CustomBaseModel):
    user_id: int
    username: str
    email: str
    role: str
    verified: bool

class CurrentUserWithJWTSchema(CustomBaseModel):
    data: CurrentUserSchema
    access_token: str
    token_type: str
    exp: int
