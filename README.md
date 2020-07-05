Trabalho final POS - Backend - Fábio Souza Teixeira

-- CRUD DE DESPESAS --

- RETORNAR DADOS DE UMA DESPESA
GET /despesa/{id_despesa}/

- RETORNAR A LISTA DE DESPESAS
GET /despesa/

- GRAVAR UMA NOVA DESPESA
POST /despesa/
Json de exemplo: {'classificacao': 'OU', 'data_pagamento': None, 'data_vencimento': '2020-07-05', 'descricao': '567g', 'formaPagamento': 'O', 'situacao': 'AP', 'valor': '2'}

- ATUALIZAR UMA NOVA DESPESA
POST /despesa/{id_despesa}/
Json de exemplo: {'classificacao': 'OU', 'data_pagamento': None, 'data_vencimento': '2020-07-05', 'descricao': '567g', 'formaPagamento': 'O', 'situacao': 'AP', 'valor': '2'}

- EXCLUIR UMA DESPESA
DELETE /despesa/{id_despesa}/


-- CRUD DE RECEITAS --