
from typing import List
from datetime import datetime


class Client:
    """
    Representa um cliente no sistema financeiro, com contas bancárias e investimentos.

    A classe `Client` armazena informações sobre o cliente, incluindo suas contas bancárias,
    investimentos realizados e métodos para adicionar contas e investimentos. Também fornece
    uma forma de calcular o patrimônio líquido total do cliente, considerando o saldo das contas
    e o valor atual dos investimentos.

    Atributos:
        name (str): O nome do cliente.
        accounts (List["Account"]): Uma lista de contas associadas ao cliente.
        investments (List["Investment"]): Uma lista de investimentos realizados pelo cliente.

    Métodos:
        add_account(account_name: str) -> "Account":
            Cria e adiciona uma nova conta ao cliente.

        add_investment(investment: "Investment"):
            Adiciona um investimento ao cliente.

        get_net_worth() -> float:
            Calcula o patrimônio líquido total do cliente, somando o saldo das contas e o valor atual dos investimentos.
    """

    def __init__(self, name: str):
        """
        Inicializa um novo cliente.

        Args:
            name (str): O nome do cliente.
        """

        self.name = name
        self.accounts = []
        self.investments = []
    
    def add_account(self, account_name: str) -> "Account": # type: ignore
        """
        Cria e adiciona uma nova conta ao cliente.

        Este método cria uma instância da classe `Account` e a adiciona à lista de contas do cliente.

        Args:
            account_name (str): O nome da conta que será criada e associada ao cliente.

        Returns:
            Account: A nova conta criada e associada ao cliente.
        """

        from finances.accounts import Account
        account = Account(name = account_name)
        self.accounts.append(account)
        return account
    
    def add_investment(self, investment: "Investment"): # type: ignore
        """
        Adiciona um investimento ao cliente.

        Este método adiciona um objeto da classe `Investment` à lista de investimentos do cliente.

        Args:
            investment (Investment): O investimento que será adicionado ao cliente.
        """

        self.investments.append(investment)

    def get_net_worth(self) -> float:
        """
        Calcula o patrimônio líquido total do cliente.

        O patrimônio líquido é calculado somando o saldo das contas e o valor atual dos investimentos
        do cliente. O valor de cada investimento é calculado com base na sua taxa de retorno e no tempo
        decorrido desde a sua compra.

        Returns:
            float: O patrimônio líquido total do cliente.
        """
        
        total_balance = sum(account.balance for account in self.accounts)
        total_investments = sum(investment.calculate_value() for investment in self.investments)
        return total_balance + total_investments
    