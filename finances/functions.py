
from datetime import datetime
from typing import List
from finances.clients import Client


def generate_report(client: Client) -> str:
    """
    Gera um relatório financeiro detalhado para o cliente.

    Este relatório inclui informações sobre as contas bancárias do cliente, 
    seus investimentos e o patrimônio líquido total. Para cada conta, são exibidos 
    o saldo e o número de transações. Para cada investimento, são fornecidos o 
    valor inicial, o valor atual, a taxa de retorno e o tipo de investimento.

    Args:
        client (Client): O cliente para o qual o relatório financeiro será gerado.

    Returns:
        str: O relatório financeiro gerado como uma string formatada.
    """

    report = []
    report.append("═" * 38)
    report.append(f"Relatório Financeiro de {client.name}")
    report.append("═" * 38)
    report.append("\nContas:")
    report.append("")

    for account in client.accounts:
        report.append(f"  Conta: {account.name}")
        report.append(f"  Saldo: R$ {account.balance:.2f}")
        report.append(f"  Transações: {len(account.transactions)}")
    
    report.append("\nInvestimentos:")
    report.append("")
    total_investments = 0
    for investment in client.investments:
        current_value = investment.calculate_value()
        total_investments += current_value
        report.append(f"  Investimento: {investment.type}")
        report.append(f"  Valor Inicial: R$ {investment.initial_amount:.2f}")
        report.append(f"  Valor Atual: R$ {current_value:.2f}")
        report.append(f"  Taxa de Retorno: {investment.rate_of_return * 100:.2f}% ao mês")
    
    net_worth = client.get_net_worth()
    report.append("\nResumo Geral:")
    report.append("")
    report.append(f"  Total em Contas: R$ {sum(account.balance for account in client.accounts):.2f}")
    report.append(f"  Total em Investimentos: R$ {total_investments:.2f}")
    report.append(f"  Patrimônio Líquido: R$ {net_worth:.2f}")
    report.append("")

    return "\n".join(report)

def future_value_report(client: Client, date: datetime) -> str:
    """
    Gera um relatório de projeção de rendimentos futuros para os investimentos do cliente.

    Este relatório calcula o valor projetado de cada investimento no cliente, 
    com base na taxa de retorno mensal e no tempo decorrido desde a compra, até 
    a data fornecida na projeção. Ele também inclui o valor inicial de cada investimento 
    e a taxa de retorno associada.

    Args:
        client (Client): O cliente para o qual o relatório de projeção de rendimentos será gerado.
        date (datetime): A data até a qual os rendimentos dos investimentos serão projetados.

    Returns:
        str: O relatório de projeção de rendimentos futuros gerado como uma string formatada.
    """
    
    report = []
    report.append("═" * 51)
    report.append(f"Projeção de Rendimentos Futuros para {client.name}")
    report.append("═" * 51)
    report.append("")
    report.append(f"Data da Projeção: {date.strftime('%d/%m/%Y')}")
    report.append("\nInvestimentos Futuramente Avaliados:")
    report.append("")
    
    for investment in client.investments:
        months = (date - investment.date_purchased).days // 30
        projected_value = investment.initial_amount * ((1 + investment.rate_of_return) ** months)
        report.append(f"  Investimento: {investment.type}")
        report.append(f"  Valor Inicial: R$ {investment.initial_amount:.2f}")
        report.append(f"  Valor Projetado em {date.strftime('%d/%m/%Y')}: R$ {projected_value:.2f}")
        report.append(f"  Taxa de Retorno: {investment.rate_of_return * 100:.0f}% ao mês")

    report.append("")
    return "\n".join(report)
