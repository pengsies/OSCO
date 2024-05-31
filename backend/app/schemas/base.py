from pydantic import BaseModel


class CustomBaseModel(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        regex_engine = 'python-re'
        arbitrary_types_allowed = True

    #@classmethod
    #def custom_validator(cls, value):
    #    # Example of a custom validator method
    #    if not value:
    #        raise ValueError("Value cannot be empty")
    #    return value
