from pydantic import BaseModel, ConfigDict


class AbstractSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
