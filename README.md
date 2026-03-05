# Web Scraping de Tweets com Python

## Descrição

Este projeto foi desenvolvido como atividade acadêmica para demonstrar a coleta de dados da plataforma X (Twitter) utilizando técnicas de **Web Scraping** em Python.

O script acessa o perfil de um usuário e coleta os **3 tweets mais recentes**, extraindo algumas informações importantes e salvando os dados em um arquivo estruturado.

## Dados coletados

O programa extrai as seguintes informações de cada tweet:

* Autor do tweet
* Texto do tweet
* Data da publicação

Esses dados são armazenados em um arquivo **CSV** localizado na pasta `data`.

## Tecnologias utilizadas

* Python
* Selenium
* BeautifulSoup
* Pandas

## Estrutura do projeto

x_webscraping/

data/
    tweets.csv

src/
    scraper.py

requirements.txt
README.md
.gitignore

## Como executar o projeto

1. Instalar as dependências:

pip install -r requirements.txt

2. Executar o script:

python src/scraper.py

Após a execução, os dados coletados serão salvos em:

data/tweets.csv

## Observação

O script foi desenvolvido apenas para fins educacionais, com o objetivo de praticar técnicas de **coleta e organização de dados na web**.
