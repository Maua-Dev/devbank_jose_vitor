from typing import List
from app.entities.transaction import Transaction
from app.repo.transaction_repository_interface import TransactionRepositoryInterface

class TransactionRepositoryMock(TransactionRepositoryInterface):
    def __init__(self):
        self._transactions: dict[str, List[Transaction]] = {}

    def get_transactions(self, account_number: str) -> List[Transaction]:
        return self._transactions.get(account_number, [])

    def save_transaction(self, account_number: str, transaction: Transaction) -> None:
        if account_number not in self._transactions:
            self._transactions[account_number] = []
        self._transactions[account_number].append(transaction)