from enum import Enum
from typing import Optional

from pydantic import BaseModel


class TransactionType(Enum):
    deposit = "DEPOSIT"
    withdraw = "WITHDRAW"
    transference = "TRANSFERENCE"


class Transaction(BaseModel):
    _table_name: str = "account_transaction"

    id: int
    name: str

    user_id: int
    account_id: int

    amount: float
    transaction_type: TransactionType
