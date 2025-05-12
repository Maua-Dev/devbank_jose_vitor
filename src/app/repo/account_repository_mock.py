from typing import Optional
from app.entities.account import Account
from app.repo.account_repository_interface import AccountRepositoryInterface

class AccountRepositoryMock(AccountRepositoryInterface):
    def __init__(self):
        self._accounts: dict[str, Account] = {}

    def get_account(self, account_number: str) -> Optional[Account]:
        return self._accounts.get(account_number)

    def save_account(self, account: Account) -> None:
        self._accounts[account.account] = account