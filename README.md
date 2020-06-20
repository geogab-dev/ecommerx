# Ecommerx


## About

Simples Restful API Python utilizando Flask e Flask Mongoengine, apenas para aprendizado.

## Pré-requisitos e como rodar

1. Download:
    * [Python 3.8+](https://www.python.org/downloads/)
    * [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows)
    * [Docker](https://www.docker.com/get-started)
    * [Docker Compose](https://docs.docker.com/compose/gettingstarted/)
    * [Postman](https://www.postman.com/)
    
1. Clonar o repositório:
    * [Ecommerx](https://github.com/Geo-Gabriel/ecommerx.git)
    
1. Abrir o projeto pelo PyCharm e configurado com o interpretador Python.

1. Instalar as dependências do projeto pelo terminal do pycharm ou outro terminal:
    ```
     pip install --user pipenv
    ```
    ```
     pipenv install
    ```
   
1. Rodar o serviço do docker-compose:
    ```
     docker-compose up -d
    ```
   ou se estiver utilizando um shell linux:
    ```
     sudo docker-compose up -d
    ```
    
1. Rode o arquivo run.py (verifique se as dependências foram instaladas com êxito e se o interpretador foi devidamente configurado):
    ```
    pipenv run flask run
    ```
