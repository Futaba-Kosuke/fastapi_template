from typing import Any, Final, TypedDict
from pydantic import BaseModel


class HelloWorldModel(BaseModel):
    Hello: str

