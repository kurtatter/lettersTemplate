from pydantic import BaseModel

from typing import List


class UserData(BaseModel):
    fullname: str
    city: str
    gift: int


class LetterData(BaseModel):
    users: List[UserData]
