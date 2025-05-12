from enum import Enum

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
  
    def __str__(self):
        return self.value