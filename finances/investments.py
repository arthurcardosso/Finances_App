
from datetime import datetime


class Investment:
    """
    Representa um investimento feito por um cliente em um determinado tipo de ativo.

    A classe `Investment` armazena as informações relacionadas a um investimento realizado por um cliente,
    incluindo o tipo do investimento, o valor inicial investido, a data da compra, a taxa de retorno anual 
    e o cliente que fez o investimento. Também oferece métodos para calcular o valor atual do investimento
    e para realizar a venda do investimento.

    Atributos:
        type (str): O tipo do investimento (por exemplo, 'Fundo Imobiliário', 'Ação', etc.).
        initial_amount (float): O valor inicial investido.
        date_purchased (datetime): A data em que o investimento foi realizado.
        rate_of_return (float): A taxa de retorno anual do investimento, representada como um valor decimal (por exemplo, 0.05 para 5%).
        client (str): O nome do cliente que fez o investimento.

    Métodos:
        calculate_value() -> float:
            Calcula o valor atual do investimento com base na taxa de retorno e no tempo decorrido desde a compra.

        sell(account: "Account"):
            Vende o investimento, creditando o valor obtido na venda na conta do cliente.
    """

    def __init__(self, type: str, initial_amount: float, date_purchased: datetime, rate_of_return: float, client = "Client"):
        """
        Inicializa um novo investimento para um cliente.

        Args:
            type (str): O tipo de investimento (exemplo: 'Fundo Imobiliário', 'Ação', etc.).
            initial_amount (float): O valor inicial investido.
            date_purchased (datetime): A data em que o investimento foi realizado.
            rate_of_return (float): A taxa de retorno anual do investimento. Exemplo: 0.05 para 5% ao ano.
            client (str, opcional): O nome do cliente que fez o investimento. Por padrão, é "Client".
        """

        self.type = type
        self.initial_amount = initial_amount
        self.date_purchased = date_purchased
        self.rate_of_return = rate_of_return
        self.client = client

    def calculate_value(self) -> float:
        """
        Calcula o valor atual do investimento.

        O valor é calculado com base no tempo decorrido desde a compra do investimento,
        levando em consideração a taxa de retorno anual. A fórmula utilizada para o cálculo
        é: valor_final = valor_investido * (1 + taxa_de_retorno) ^ meses_decorridos.

        Returns:
            float: O valor atual do investimento após o período decorrido desde a compra.
        """

        months = (datetime.now() - self.date_purchased).days // 30
        return self.initial_amount * ((1 + self.rate_of_return) ** months)

    def sell(self, account: "Account"): # type: ignore
        """
        Realiza a venda do investimento e credita o valor obtido na conta do cliente.

        Este método calcula o valor atual do investimento e cria uma transação de venda, 
        creditando o valor obtido na conta do cliente fornecida como argumento.

        Args:
            account (Account): A conta do cliente onde o valor da venda será creditado.
        """
        
        from finances.accounts import Account
        value = self.calculate_value()
        account.add_transaction(amount = value, category = "Investment Sale", description = f"Venda de {self.type}")
    