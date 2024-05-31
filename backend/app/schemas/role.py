from enum import Enum
from base import CustomBaseModel as BaseModel

class RoleEnum(str, Enum):
    MEMBER = "1"
    MODERATOR = "2"
    ADMIN = "3"
    PAGEADMIN = "4"
    SYSADMIN = "5"


class RoleSchema(BaseModel):
    role_id: int
    role_name: RoleEnum

    class Config:
        orm_mode = True
