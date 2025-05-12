from dataclasses import dataclass
from time import time
from typing import Optional

from app.enums.transaction_type_enum import TransactionType

@dataclass
class Transaction:
    type: TransactionType
    value: float
    current_balance: float
    timestamp: float

    def __post_init__(self):
       
        if self.value < 0:
            raise ValueError(f"Transaction value must be non-negative, got {self.value}")
        
        if self.timestamp < 0:
            raise ValueError(f"Timestamp must be a positive float, got {self.timestamp}")

    @classmethod
    def create(cls, type: TransactionType, value: float, current_balance: float, timestamp: Optional[float] = None):
       
        ts = timestamp if timestamp is not None else time() * 1000  # milliseconds
        return cls(type=type, value=value, current_balance=current_balance, timestamp=ts)