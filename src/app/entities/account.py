from dataclasses import dataclass

@dataclass
class Account:
    name: str
    agency: str
    account: str
    current_balance: float

    def __post_init__(self):
        if not (self.agency.isdigit() and len(self.agency) == 4):
            raise ValueError(f"Agency must be 4 digits, got '{self.agency}'")
        parts = self.account.split('-')
        if len(parts) != 2 or not (parts[0].isdigit() and len(parts[0]) == 5 and parts[1].isdigit() and len(parts[1]) == 1):
            raise ValueError(f"Account must follow format 'XXXXX-X', got '{self.account}'")