from abc import ABC, abstractmethod
from typing import Optional
from app.entities.account import Account

class AccountRepositoryInterface(ABC):

    @abstractmethod
    def get_account(self, account_number: str) -> Optional[Account]:
        pass

    @abstractmethod
    def save_account(self, account: Account) -> None:
        pass