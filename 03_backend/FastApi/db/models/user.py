from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    # id: str | None # python 3.10
    id: Optional[str] # python 3.9 # deta funciona hasta python 3.9
    username: str
    email: str