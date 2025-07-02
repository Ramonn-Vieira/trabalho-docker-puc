
#Desafio: Implementação de Estrutura com Docker Compose

Objetivo: Utilizando o jogo demo disponível em https://github.com/fams/guess_gameLinks to an external site., você deverá implementar uma estrutura com Docker Compose que englobe os seguintes serviços:

Um container para o backend em Python (Flask).
Um container para o banco de dados Postgres.
Um container NGINX atuando como proxy reverso e servindo as páginas do frontend React.



# Guess Game com Docker Compose

Esse projeto roda um joguinho de adivinhação feito com Flask e React, usando o Docker Compose para facilitar tudo. Com ele, você sobe tudo com um único comando!

---

## O que vem no projeto

- Backend (Flask): com 2 instâncias (para testar balanceamento de carga)
- Frontend (React): servido com NGINX
- Banco de Dados (PostgreSQL): com dados salvos mesmo se reiniciar
- NGINX: funciona como proxy reverso e balanceador de carga

---

## Como rodar

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/guess_game_docker_compose.git
cd guess_game_docker_compose
```

2. Suba tudo com Docker Compose:

```bash
docker-compose up --build
```

3. Abra o navegador e vá para:

```
http://localhost
```

---

## O que tem nos containers

- backend1 e backend2: rodam o Flask
- frontend: React empacotado pelo NGINX
- db: banco PostgreSQL
- nginx: distribui as requisições e serve o frontend

---

## Extras técnicos (explicado de forma simples)

- Balanceamento: O NGINX envia as requisições pro backend de forma alternada (load balancing).
- Persistência: O banco salva os dados mesmo se você parar tudo.
- Resiliência: Se algo cair, os containers sobem de novo.
- Atualizações: É fácil atualizar só o backend, o frontend ou o banco.

---

## Variáveis de ambiente

O backend usa isso pra acessar o banco:

```bash
postgresql://guess_user:guess_pass@db:5432/guess_db
```

