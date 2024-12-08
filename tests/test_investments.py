
import pytest
from datetime import datetime
from finances.investments import Investment
from finances.clients import Client
from finances.accounts import Account

def test_investment_creation():
    """
    Testa a criação de um investimento.

    Verifica se a criação de um investimento está funcionando corretamente,
    assegurando que os atributos como tipo, valor inicial, taxa de retorno,
    data de compra e cliente estejam sendo atribuídos corretamente.
    """

    client = Client(name = "Arthur Cardoso")
    investment = Investment(type = "Ações", initial_amount = 10000.00, date_purchased = datetime(2024, 12, 7), rate_of_return = 0.02, client = client)
    assert investment.type == "Ações"
    assert investment.initial_amount == 10000.00
    assert investment.rate_of_return == 0.02
    assert isinstance(investment.date_purchased, datetime)
    assert investment.client == client

def test_investment_calculate_value():
    """
    Testa o cálculo do valor de um investimento.

    Verifica se o valor calculado para o investimento está correto.
    Este teste assume que o valor inicial do investimento não mudou.
    O cálculo do valor pode ser alterado no futuro e este teste será útil
    para verificar se a lógica do cálculo está correta.
    """
    
    client = Client(name = "Arthur Cardoso")
    investment = Investment(type = "Ações", initial_amount = 10000.00, date_purchased = datetime(2024, 12, 7), rate_of_return = 0.02, client = client)
    value = investment.calculate_value()
    assert value == 10000.00
