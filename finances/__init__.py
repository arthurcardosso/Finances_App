"""
Este módulo exporta as principais classes e funções do pacote financeiro.

O objetivo deste módulo é fornecer acesso simplificado aos componentes principais
do sistema financeiro, incluindo classes para transações, contas, investimentos, 
clientes, e funções para gerar relatórios financeiros e projeções de valores futuros.

Importa e disponibiliza as seguintes classes e funções:

Classes:
    - Transaction: Representa uma transação financeira, com atributos como valor,
      categoria e descrição.
    - Account: Representa uma conta bancária do cliente, com métodos para
      registrar transações e consultar o saldo.
    - Investment: Representa um investimento financeiro, com métodos para calcular
      o valor atual e projetar o valor futuro.
    - Client: Representa um cliente, incluindo suas contas e investimentos, e fornece
      métodos para calcular seu patrimônio líquido.

Funções:
    - generate_report: Gera um relatório financeiro completo para o cliente, incluindo
      informações sobre contas e investimentos.
    - future_value_report: Gera um relatório de projeção de rendimentos futuros para
      os investimentos do cliente com base em uma data fornecida.

A lista `__all__` define quais nomes são exportados quando o módulo é importado. 
Isso controla o comportamento da importação do módulo, facilitando o acesso aos 
componentes principais do sistema financeiro.

Exemplo de uso:
    from finances import Transaction, Account, Investment, Client, generate_report
    # Agora é possível acessar diretamente as classes e funções definidas acima.
"""

from .transactions import Transaction
from .accounts import Account
from .investments import Investment
from .clients import Client
from .functions import generate_report, future_value_report

__all__ = [
    "Transaction",
    "Account",
    "Investment",
    "Client",
    "generate_report",
    "future_value_report"
]
