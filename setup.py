
"""Setup.py do Pacote

Script de configuração para o pacote 'Finances'. Esse arquivo usa a função
'setup' do módulo 'setuptools' para definir as informações do pacote e suas dependências.

Functions:
    setup: Configura o pacote com nome, versão, descrição, autor, dependências,
    e outros metadados necessários para distribuição.

Args:
    name (str): O nome do pacote.
    version (str): A versão atual do pacote.
    description (str): Uma breve descrição do pacote.
    long_description (str): Descrição mais detalhada, lida do arquivo 'README.md'.
    long_description_content_type (str): O formato do arquivo de descrição longa, neste caso, Markdown.
    author (str): Nome do autor do pacote.
    author_email (str): Email do autor para contato.
    python_requires (str): Versão mínima do Python necessária para rodar o pacote.
    url (str): A URL principal para o repositório do projeto no GitHub,
    packages (list): Pacotes que serão incluídos na distribuição.
    install_requires (list): Dependências necessárias para rodar o pacote.
    license (str): A licença sob a qual o pacote é distribuído.
    keywords (list): Palavras-chave que descrevem o pacote.
    classifiers (list): Classificações adicionais para o pacote.
"""

from setuptools import setup, find_packages

setup(
    name = "finances_app",  
    version = "1.0.0",  
    description = "Pacote para implementação de um aplicativo para gerenciamento de finanças pessoais",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    author = "Arthur Cardoso", 
    author_email = "arthur.cardoso@email.com",  
    python_requires = ">=3.8",
    url = "https://github.com/arthurcardosso/Finances_App", 
    packages = find_packages(exclude=["tests*"]),
    install_requires = ['pytest'],
    license = "MIT",
    keywords = ["Aplicativo", "Pacote de Implementação", "Finanças Pessoais", "Gerenciamento"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Licença do código (substitua, se necessário)
        "Operating System :: OS Independent",
    ],
)
