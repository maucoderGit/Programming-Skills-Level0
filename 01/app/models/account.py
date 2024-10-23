from pydantic import BaseModel

from typing import Optional


class Account(BaseModel):
    _table_name: str = "account"

    id: int
    name: str
    
    user_id: int
    amount: float