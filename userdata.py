from pydantic import BaseModel


class UserData(BaseModel):
    data: list[int]