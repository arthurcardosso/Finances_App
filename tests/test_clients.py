
import pytest
from datetime import datetime
from finances.clients import Client
from finances.accounts import Account
from finances.investments import Investment

def test_client_creation():
    """
    Testa a criação de um cliente.

    Verifica se um cliente é criado corretamente com o nome fornecido,
    e se ele não possui contas ou investimentos inicialmente.
    """

    client = Client(name = "Arthur Cardoso")
    assert client.name == "Arthur Cardoso"
    assert len(client.accounts) == 0
    assert len(client.investments) == 0

def test_add_account():
    """
    Testa a adição de uma conta a um cliente.

    Verifica se a conta é adicionada corretamente ao cliente e se a
    conta criada tem o nome correto.
    """

    client = Client(name = "Arthur Cardoso")
    account = client.add_account("Conta Corrente")
    assert len(client.accounts) == 1
    assert account.name == "Conta Corrente"

def test_add_investiment():
    """
    Testa a adição de um investimento a um cliente.

    Verifica se o investimento é adicionado corretamente à lista de
    investimentos do cliente e se as informações do investimento estão
    corretas.
    """

    client = Client(name = "Arthur Cardoso")
    investment = Investment(type = "Ações", initial_amount = 10000, date_purchased = datetime(2024,12,7), rate_of_return = 0.02)
    client.add_investment(investment)
    assert len(client.investments) == 1
    assert investment.type == "Ações"

def test_get_net_worth():
    """
    Testa o cálculo do patrimônio líquido de um cliente.

    Verifica se o patrimônio líquido do cliente é calculado corretamente,
    levando em conta os saldos das contas e o valor dos investimentos,
    utilizando o método `get_net_worth`.
    """

    client = Client(name = "Arthur Cardoso")
    account1 = client.add_account("Conta Corrente")
    account1.add_transaction(amount = 5000, category = "Depósito", description = "Salário")
    account2 = client.add_account("Poupança")
    account2.add_transaction(amount = 3000, category = "Depósito", description = "Economias")
    investment = Investment(
        type = "Ações", 
        initial_amount = 10000, 
        date_purchased = datetime(2024, 12, 7), 
        rate_of_return = 0.02
    )
    client.add_investment(investment)
    expected_investment_value = investment.calculate_value()
    account1_balance = account1.balance
    account2_balance = account2.balance
    expected_net_worth = account1_balance + account2_balance + expected_investment_value
    assert pytest.approx(client.get_net_worth(), 0.01) == expected_net_worth
