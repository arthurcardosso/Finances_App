
import pytest
from datetime import datetime
from finances.transactions import Transaction

def test_transaction_creation():
    """
    Testa a criação de uma transação.

    Verifica se a transação é criada corretamente com os atributos fornecidos,
    incluindo o valor, categoria, descrição e data, sendo que a data é registrada
    automaticamente no momento da criação da transação.
    """

    transaction = Transaction(amount = 1000.00, category = "Salário", description = "Pagamento da Bolsa NES")
    assert transaction.amount == 1000.00
    assert transaction.category == "Salário"
    assert transaction.description == "Pagamento da Bolsa NES"
    assert isinstance(transaction.date, datetime)

def test_transaction_str():
    """
    Testa a representação em string de uma transação.

    Verifica se a representação da transação retorna a string esperada no formato:
    'Transação: <descrição> | R$ <valor> | <categoria>'.
    """

    transaction = Transaction(amount = 1000.00, category = "Salário", description = "Pagamento da Bolsa NES")
    assert str(transaction) == "Transação: Pagamento da Bolsa NES | R$ 1000.00 | Salário"

def test_transaction_update():
    """
    Testa a atualização dos atributos de uma transação.

    Verifica se os atributos de uma transação podem ser atualizados corretamente
    usando o método `update`, alterando valores como o montante e a descrição.
    """
    
    transaction = Transaction(amount = 1000.00, category = "Salário")
    transaction.update(amount = 1500.00, description = "Pagamento da Nova Bolsa NES")
    assert transaction.amount == 1500.00
    assert transaction.description == "Pagamento da Nova Bolsa NES"
