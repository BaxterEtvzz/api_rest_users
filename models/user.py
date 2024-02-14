from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: Optional[str]
    name: str
    role: str
    created_at: datetime = datetime.now()
