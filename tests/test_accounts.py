
import pytest
from finances.accounts import Account
from finances.transactions import Transaction
from finances.clients import Client

def test_account_creation():
    """
    Testa a criação de uma conta.

    Verifica se a conta é criada corretamente com o nome esperado,
    saldo inicial de 0.0 e sem transações.
    """

    account = Account(name = "Conta Corrente")
    assert account.name == "Conta Corrente"
    assert account.balance == 0.0
    assert len(account.transactions) == 0

def test_add_transaction():
    """
    Testa a adição de uma transação em uma conta.

    Verifica se a transação é adicionada corretamente à conta, se o saldo
    da conta é atualizado e se os valores da transação estão corretos.
    """

    account = Account(name = "Conta Corrente")
    transaction = account.add_transaction(amount = 1000, category = "Depósito", description = "Salário")
    assert len(account.transactions) == 1
    assert account.balance == 1000
    assert transaction.amount == 1000

def test_get_transactions():
    """
    Testa a busca de transações em uma conta com base em critérios.

    Verifica se a função `get_transactions` retorna corretamente as transações
    de acordo com a categoria fornecida.
    """
    
    account = Account(name = "Conta Corrente")
    account.add_transaction(amount = 1000, category = "Depósito", description = "Salário")
    account.add_transaction(amount = -200, category = "Retirada", description = "Saque")
    transactions = account.get_transactions(category = "Depósito")
    assert len(transactions) == 1
    assert transactions[0].amount == 1000
    assert transactions[0].category == "Depósito"
