from abc import ABC, abstractmethod
from typing import List
from app.entities.transaction import Transaction

class TransactionRepositoryInterface(ABC):

    @abstractmethod
    def get_transactions(self, account_number: str) -> List[Transaction]:
        pass

    @abstractmethod
    def save_transaction(self, account_number: str, transaction: Transaction) -> None:
        pass
