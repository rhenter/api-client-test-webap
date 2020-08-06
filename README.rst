================
Bookstore WEBAPP
================

Projeto de teste como cliente da API usado como demostração da biblioteca Django API Client

Dependências
============

This project requires:
    * Python 3.6 or earlier
    * Git
    * virtualenvwrapper, pyenv virtualenv ou virtualenv para desenvolvimento local

Instalação
==========

1. Crie um virtualenv e faça o clone do repositório:

Usando Virtualenv Wrapper

.. code-block:: shell

    $ git clone git@github.com:rhenter/bookstore-api.git
    $ cd bookstore-api
    $ mkvirtualenv -p $(which python) bookstore_api
    $ workon bookstore_api

Usando pyenv virtualenv

    $ git clone git@github.com:rhenter/bookstore-api.git
    $ cd bookstore-api
    $ pyenv virtualenv bookstore_api
    $ pyenv activate bookstore_api

4. Create your local settings file (use local.env as a template):

.. code-block:: shell

    $ cp local.env .env

    Edit .env file to use your settings

5. Instale as dependencias do projeto:

.. code-block:: shell

    $ pip install -r requirements/local.txt


Migrações do Banco de Dados
===========================

.. code-block:: shell

    $ python manage.py migrate

Testes
======

Use o ``pytest`` com alguns plugins ao invés do sistema de test padrão nativo do Django.

.. code-block:: shell

    $ pytest -vv -s
