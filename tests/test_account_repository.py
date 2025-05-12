from src.app.entities.account import Account
from src.app.repo.account_repository_mock import AccountRepositoryMock

def test_save_and_get_account():
    # Criação de uma conta para teste
    account = Account(
        name="Alice",
        agency="1234",
        account="12345-6",
        current_balance=1000.0
    )
    
    # Criação do repositório mock
    repo = AccountRepositoryMock()

    # Salvando a conta
    repo.save_account(account)

    # Recuperando a conta
    retrieved_account = repo.get_account("12345-6")

    # Verificando se a conta recuperada é a mesma
    assert retrieved_account is not None
    assert retrieved_account.name == "Alice"
    assert retrieved_account.agency == "1234"
    assert retrieved_account.account == "12345-6"
    assert retrieved_account.current_balance == 1000.0
