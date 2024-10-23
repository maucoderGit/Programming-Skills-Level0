from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    _table_name: str = "user"

    id: int
    name: str
    username: str
    account_ids: Optional[set[int]] = None
    login_attemps: int = 0
    password: str
