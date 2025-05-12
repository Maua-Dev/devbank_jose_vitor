from src.app.entities.account import Account

def test_account_creation():
    account = Account(
        name="Alice",
        agency="1234",
        account="12345-6",
        current_balance=1000.0
    )

    assert account.name == "Alice"
    assert account.agency == "1234"
    assert account.account == "12345-6"
    assert account.current_balance == 1000.0

