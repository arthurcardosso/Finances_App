
import pytest
from datetime import datetime
from finances.functions import generate_report, future_value_report
from finances.clients import Client
from finances.accounts import Account
from finances.investments import Investment

def test_generate_report():
    """
    Testa a geração do relatório financeiro de um cliente.

    Verifica se o relatório gerado inclui o nome do cliente, informações
    sobre a conta e sobre os investimentos do cliente, garantindo que o
    relatório contenha as seções e dados corretos.
    """

    client = Client(name = "Arthur Cardoso")
    account = client.add_account("Conta Corrente")
    account.add_transaction(amount = 1000, category = "Depósito", description = "Salário")
    investment = Investment(type = "Ações", initial_amount = 10000, date_purchased = datetime(2024, 12, 7), rate_of_return = 0.02, client = client)
    client.add_investment(investment)
    report = generate_report(client)
    assert "Relatório Financeiro de Arthur Cardoso" in report
    assert "Conta Corrente" in report
    assert "Investimento" in report

def test_future_value_report():
    """
    Testa a geração do relatório de projeção de rendimentos futuros de um cliente.

    Verifica se o relatório gerado contém a projeção de valor futuro de
    um investimento específico, incluindo informações como o tipo de
    investimento e o valor projetado para a data informada.
    """
    
    client = Client(name = "Arthur Cardoso")
    investment = Investment(type = "Ações", initial_amount = 10000, date_purchased = datetime(2024, 12, 7), rate_of_return = 0.02, client = client)
    client.add_investment(investment)
    report = future_value_report(client, datetime(2025, 12, 7))
    assert "Projeção de Rendimentos Futuros" in report
    assert "Ações" in report
