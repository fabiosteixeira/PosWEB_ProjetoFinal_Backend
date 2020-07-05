Trabalho final POS - Backend - Fábio Souza Teixeira

-- CRUD DE DESPESAS --

- RETORNAR DADOS DE UMA DESPESA
GET /despesa/{id_despesa}/

- RETORNAR A LISTA DE DESPESAS
GET /despesa/

- GRAVAR UMA NOVA DESPESA
POST /despesa/
Json de exemplo: {"classificacao": "OU", "data_pagamento": "", "data_vencimento": "2020-07-05", "descricao": "567g", "formaPagamento": "O", "situacao": "AP", "valor": "2"}

- ATUALIZAR UMA NOVA DESPESA
POST /despesa/{id_despesa}/
Json de exemplo: {"classificacao": "OU", "data_pagamento": "", "data_vencimento": "2020-07-05", "descricao": "567g", "formaPagamento": "O", "situacao": "AP", "valor": "2"}

- EXCLUIR UMA DESPESA
DELETE /despesa/{id_despesa}/


-- CRUD DE RECEITAS --

- RETORNAR DADOS DE UMA RECEITA
GET /receita/{id_receita}/

- RETORNAR A LISTA DE RECEITAS
GET /receita/

- GRAVAR UMA NOVA RECEITA
POST /receita/
Json de exemplo: {"classificacao": "OU", "data_recebimento": "", "data_expectativa": "2020-07-05", "descricao": "567g", "formaRecebimento": "O", "situacao": "AR", "valor": "2"}

- ATUALIZAR UMA NOVA RECEITA
POST /receita/{id_receita}/
Json de exemplo: {"classificacao": "OU", "data_recebimento": "", "data_expectativa": "2020-07-05", "descricao": "567g", "formaRecebimento": "O", "situacao": "AR", "valor": "2"}

- EXCLUIR UMA RECEITA
DELETE /receita/{id_receita}/