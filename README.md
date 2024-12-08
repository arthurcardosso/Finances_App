
# Finances App - Aplicativo de Finanças Pessoais 💰📊

Finances App é um aplicativo de backend para gerenciamento de finanças pessoais que permite gerenciar contas bancárias, acompanhar investimentos, rastrear receitas e despesas entre outras funções que oferecem funcionalidades como categorização de transações, geração de relatórios financeiros e projeções futuras de rendimentos para você. Este é o projeto é ideal para quem deseja organizar suas finanças e avaliar oportunidades de investimento de maneira prática e intuitiva.

## Índice do Projeto

- *Descrição do Projeto*
- *Componentes do Projeto*
- *Instalação*
- *Uso*
- *Estrutura do Pacote*
- *Funcionalidades*
- *Dependências*
- *Licença*
- *Contato*
- *Agradecimentos*

## Descrição do Projeto

Esse pacote contém uma implementação simples de um aplicativo programado em backend. A Aplicação é uma solução para gerenciar contas bancárias, rastrear investimentos e gerar relatórios financeiros detalhados. O projeto foi desenvolvido com foco em simplicidade e flexibilidade, permitindo o acompanhamento financeiro pessoal e projeções futuras para investimentos.

## Componentes do Projeto

- **Cliente**: Representa o usuário e suas finanças.
- **Contas Bancárias**: Permite gerenciar saldos e registrar transações.
- **Transações**: Registro detalhado de transações realizadas nas contas, incluindo categoria e descrição.
- **Investimentos**: Controle de investimentos com cálculo de retorno atual e futuro.
- **Relatórios Financeiros**: Relatórios claros e detalhados com informações sobre o estado financeiro atual e projeções.

## Instalação

### 1. Clone o Repositório
Primeiramente, clone o repositório para o seu ambiente local:

git clone https://github.com/arthurcardosso/Finances_App.git

### 2. Navegue para o Diretório do Projeto
Após isso, navegue até o diretório do projeto e digite:

cd finances_app 

### 3. Instalando o Projeto
Por fim, instale o projeto e suas dependências através do pip:

pip install -r requirements.txt

## Uso

O script _example.py_ demonstra como usar o aplicativo. Para analisar mais um uso prático do pacote e para executá-lo:

python example.py

### Exemplo de Uso | Saída

╔════════════════════════════════════════════════════════════════╗

║                     Relatório Financeiro                       ║

╚════════════════════════════════════════════════════════════════╝

══════════════════════════════════════

Relatório Financeiro de Arthur Cardoso

══════════════════════════════════════

Contas:

  Conta: Conta Corrente
  Saldo: R$ 3500.00
  Transações: 2
  Conta: Poupança
  Saldo: R$ 3000.00
  Transações: 1

Resumo Geral:

  Total em Contas: R$ 6500.00
  Total em Investimentos: R$ 11268.25
  Patrimônio Líquido: R$ 17768.25

## Estrutura do Pacote

finances_app/

│

├── finances/                   # Pacote principal contendo as funcionalidades do aplicativo

│   ├── __init__.py              # Torna o diretório 'finances' um pacote Python

│   ├── accounts.py              # Gerenciamento de contas bancárias e transações financeiras

│   ├── clients.py               # Representação de clientes e suas finanças (contas, investimentos)

│   ├── functions.py             # Funções utilitárias, como a geração de relatórios financeiros

│   ├── investments.py           # Controle de investimentos financeiros, cálculo de rendimentos

│   ├── transactions.py          # Registro e manipulação de transações financeiras (depósitos, retiradas)

│

├── tests/                       # Pasta contendo os testes automatizados para cada módulo

│   ├── __init__.py              # Torna o diretório 'tests' um pacote Python

│   ├── test_accounts.py         # Testes para a classe Account e funcionalidades relacionadas

│   ├── test_clients.py          # Testes para a classe Client e gerenciamento de clientes

│   ├── test_functions.py        # Testes para as funções de geração de relatórios (generate_report, etc.)

│   ├── test_investments.py      # Testes para a classe Investment e cálculos de rendimentos

│   ├── test_transactions.py     # Testes para a classe Transaction e manipulação de transações

│

├── setup.py                     # Script de configuração do pacote (instalação e dependências)

├── example.py                   # Exemplo de uso do pacote para fins de demonstração

├── LICENSE                      # Arquivo de licença do projeto

├── README.md                    # Documentação sobre o projeto, incluindo objetivo e uso

├── relations.txt                # Descrição das relações entre as classes do projeto

└── requirements.txt             # Dependências necessárias para o funcionamento do pacote

## Funcionalidades

- Gerenciamento de transações financeiras com categorias e descrições personalizadas.
- Controle de contas, incluindo saldo e histórico de transações.
- Cálculo e rastreamento de investimentos com retorno mensal.
- Geração de relatórios financeiros detalhados.
- Projeção de rendimentos futuros com base na taxa de retorno dos investimentos.

## Dependências

O projeto depende da biblioteca padrão de módulos do Python (versão 3.8 ou superior), onde utiliza os módulos internos _datetime_ e _typing_ em sua estrutura. Além disso, utiliza a biblioteca externa _pytest_ para testes.

## Licença

Esse projeto está licenciado sob a MIT License - veja o arquivo LICENSE.txt para mais detalhes.

## Contato

Se você tiver perguntas, sugestões ou feedback sobre o projeto, fique à vontade para entrar em contato comigo através dos
seguintes meios de contatos:

- Email: arthnrcardoso@gmail.com
- Whatszapp: +55 82 99382-5927
- GitHub: github.com/arthurcardosso

## Agradecimentos

Monitores e Professor Nano, agradeço por dedicar seu tempo para explorar e corrigir esse meu projeto de Programação Orientada a Objetos. 
Um agradecimento especial aos criadores de recursos e bibliotecas open-source que tornaram este projeto possível. A Todos que vizualizaram esse repositório sua contribuição, observações e sugestões são muito bem-vindas por mim!
