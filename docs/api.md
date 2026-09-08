# Documentação da API REST

## Endpoints

### Clientes

- **GET /api/clientes/**
  - **Descrição**: Retorna uma lista de clientes.
  - **Parâmetros**: Nenhum
  - **Resposta**: Lista de clientes.

- **POST /api/clientes/**
  - **Descrição**: Cria um novo cliente.
  - **Parâmetros**:
    - `nome` (string): Nome do cliente.
    - `email` (string): Email do cliente.
    - `telefone` (string): Telefone do cliente.
  - **Resposta**: Detalhes do cliente criado.

### Leads

- **GET /api/leads/**
  - **Descrição**: Retorna uma lista de leads.
  - **Parâmetros**: Nenhum
  - **Resposta**: Lista de leads.

- **POST /api/leads/**
  - **Descrição**: Cria um novo lead.
  - **Parâmetros**:
    - `cliente_id` (integer): ID do cliente associado.
    - `descricao` (string): Descrição do lead.
  - **Resposta**: Detalhes do lead criado.

### Interações

- **GET /api/interacoes/**
  - **Descrição**: Retorna uma lista de interações.
  - **Parâmetros**: Nenhum
  - **Resposta**: Lista de interações.

- **POST /api/interacoes/**
  - **Descrição**: Cria uma nova interação.
  - **Parâmetros**:
    - `lead_id` (integer): ID do lead associado.
    - `descricao` (string): Descrição da interação.
  - **Resposta**: Detalhes da interação criada.
