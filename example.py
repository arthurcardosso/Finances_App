"""Exemplo de Uso do Pacote

Este script demonstra as funcionalidades de um aplicativo de finanças pessoais. Ele realiza as seguintes operações:

1. Cria um cliente fictício chamado "Arthur Cardoso".
2. Adiciona duas contas bancárias ao cliente ("Conta Corrente" e "Poupança") e realiza transações em ambas.
3. Adiciona um investimento com uma taxa de retorno mensal e uma data de compra simulada.
4. Gera e exibe relatórios financeiros:
   - Relatório financeiro atual com informações detalhadas sobre contas e investimentos.
   - Relatório de projeção de valores futuros para uma data futura especificada.

Classes Utilizadas:
    - Client: Representa o cliente e suas finanças pessoais.
    - Investment: Representa um investimento financeiro associado ao cliente.

Funções Importadas:
    - generate_report(client): Gera um relatório financeiro detalhado para o cliente.
    - future_value_report(client, date): Gera um relatório de projeção de valores futuros para os investimentos do cliente.

Exemplo de Uso:
    Execute o script para:
    - Criar um cliente e suas contas/investimentos.
    - Gerar e exibir relatórios detalhados sobre o estado financeiro atual e futuro.

Módulos Necessários:
    - datetime: Para gerenciar datas de transações e investimentos.
    - timedelta: Para calcular períodos em dias, meses e anos.
    - finances.clients: Contém a classe Client.
    - finances.investments: Contém a classe Investment.
    - finances.functions: Contém as funções de geração de relatórios.

Output:
    O script exibe dois relatórios no terminal:
    1. Relatório financeiro atual.
    2. Projeção de valores futuros para uma data específica.
"""

from datetime import datetime, timedelta
from finances.clients import Client
from finances.investments import Investment
from finances.functions import generate_report, future_value_report

client = Client(name = "Arthur Cardoso")

main_account = client.add_account("Conta Corrente")
main_account.add_transaction(amount = 5000, category = "Depósito", description = "Depósito inicial")
main_account.add_transaction(amount = -1500, category = "Despesas", description = "Pagamento de contas")

savings_account = client.add_account("Poupança")
savings_account.add_transaction(amount = 3000, category = "Depósito", description = "Transferência para poupança")

investment_date = datetime.now() - timedelta(days=365)  
investment = Investment(
    type = "Fundo Imobiliário",
    initial_amount = 10000,
    date_purchased = investment_date,
    rate_of_return = 0.01,  
    client = client
)
client.add_investment(investment)

print("_" * 65)
print("\n╔════════════════════════════════════════════════════════════════╗")
print("║                     Relatório Financeiro                       ║")
print("╚════════════════════════════════════════════════════════════════╝\n")
print(generate_report(client))

future_date = datetime.now() + timedelta(days=365) 
print("\n╔════════════════════════════════════════════════════════════════╗")
print("║                   Relatório de Valor Futuro                    ║")
print("╚════════════════════════════════════════════════════════════════╝\n")
print(future_value_report(client, future_date))
print("_" * 65)
