
from datetime import datetime
from typing import List, Optional


class Account:
    """
    Representa uma conta bancária de um cliente.

    A classe `Account` permite armazenar e gerenciar o saldo de uma conta bancária,
    além de registrar transações financeiras associadas a essa conta. As transações podem
    incluir depósitos, retiradas e outras operações categorizadas, e a classe permite
    consultar transações em um intervalo de datas específico ou por categoria.

    Atributos:
        name (str): O nome da conta bancária.
        balance (float): O saldo atual da conta, começando em 0.0.
        transactions (List[Transaction]): Uma lista de transações realizadas na conta.
        client (Optional[Client]): O cliente associado a essa conta. Pode ser `None`.

    Métodos:
        add_transaction(amount: float, category: str, description: str = "") -> Transaction:
            Registra uma nova transação na conta, atualizando o saldo da conta.
        
        get_transactions(
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None,
            category: Optional[str] = None
        ) -> List[Transaction]:
            Retorna uma lista de transações que atendem aos critérios de data e categoria
            fornecidos.
    """

    def __init__(self, name: str, client: Optional["Client"] = None): # type: ignore
        """
        Inicializa uma nova conta bancária.

        Args:
            name (str): O nome da conta bancária.
            client (Optional[Client]): O cliente associado a essa conta (opcional).
        """

        self.name = name
        self.balance = 0.0
        self.transactions: List["Transaction"] = [] # type: ignore
        self.client = client 

    def add_transaction(self, amount: float, category: str, description: str = "") -> "Transaction": # type: ignore
        """
        Adiciona uma transação à conta e atualiza o saldo.

        Args:
            amount (float): O valor da transação. Pode ser positivo (depósito) ou negativo (retirada).
            category (str): A categoria da transação (exemplo: 'Depósito', 'Retirada').
            description (str, opcional): Descrição adicional sobre a transação.

        Returns:
            Transaction: A transação registrada.
        """

        from finances.transactions import Transaction
        transaction = Transaction(amount = amount, category = category, description = description, date = datetime.now())
        self.transactions.append(transaction)
        self.balance += amount
        return transaction

    def get_transactions(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, category: Optional[str] = None) -> List["Transaction"]: # type: ignore
        """
        Retorna uma lista de transações filtradas por data e/ou categoria.

        Args:
            start_date (Optional[datetime]): Data inicial para filtrar transações (opcional).
            end_date (Optional[datetime]): Data final para filtrar transações (opcional).
            category (Optional[str]): Categoria das transações para filtrar (opcional).

        Returns:
            List[Transaction]: Lista de transações que atendem aos critérios fornecidos.
        """
        
        return [ 
            t for t in self.transactions
            if (start_date is None or t.date >= start_date) and
               (end_date is None or t.date <= end_date) and
               (category is None or t.category == category)
        ]
    