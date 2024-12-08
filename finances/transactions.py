
from datetime import datetime
from typing import Optional


class Transaction:
    """
    Representa uma transação financeira registrada em uma conta bancária.

    A classe `Transaction` é usada para armazenar informações sobre uma transação financeira,
    incluindo o valor da transação, a data em que foi realizada, a categoria da transação 
    (por exemplo, depósito, retirada) e uma descrição adicional.

    Atributos:
        amount (float): O valor da transação. Pode ser positivo (exemplo: depósito) ou negativo (exemplo: retirada).
        date (datetime): A data e hora da transação. Se não for fornecida, será usada a data e hora atual.
        category (str): A categoria da transação, como 'Depósito', 'Retirada', etc.
        description (str): Uma descrição adicional sobre a transação.

    Métodos:
        __str__() -> str:
            Retorna uma representação em string da transação, incluindo a descrição, valor e categoria.

        update(**atributtes):
            Atualiza os atributos da transação com os novos valores fornecidos no argumento.
    """

    def __init__(self, amount: float, date: Optional[datetime] = None, category: str = "", description: str = ""):
        """
        Inicializa uma nova transação financeira.

        Args:
            amount (float): O valor da transação. Pode ser positivo (depósito) ou negativo (retirada).
            date (Optional[datetime], opcional): A data da transação. Se não fornecida, a data e hora atual será usada.
            category (str, opcional): A categoria da transação (exemplo: 'Depósito', 'Retirada').
            description (str, opcional): Descrição adicional sobre a transação.
        """

        self.amount = amount
        self.date = date or datetime.now()
        self.category = category
        self.description = description
        self.date = date if date else datetime.now()
    
    def __str__(self) -> str:
        """
        Retorna uma representação em string da transação.

        A string resultante inclui a descrição, valor e categoria da transação.

        Returns:
            str: Representação em string da transação no formato:
                "Transação: [descrição] | R$ [valor] | [categoria]"
        """
        
        return f"Transação: {self.description} | R$ {self.amount:.2f} | {self.category}"
    
    def update(self, **atributtes):
        """
        Atualiza os atributos da transação com os novos valores fornecidos.

        Este método permite modificar os atributos da transação. Ele verifica se o atributo
        fornecido existe e, em caso afirmativo, o atualiza com o novo valor.

        Args:
            **atributtes: Pares de chave-valor que representam os atributos e seus novos valores.

        Exemplo:
            Para atualizar a categoria e descrição de uma transação:
            transaction.update(category='Transferência', description='Pagamento de fatura')
        """
        
        for attr, value in atributtes.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
