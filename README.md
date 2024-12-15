![image](https://github.com/user-attachments/assets/6f8132b2-d6dc-4b38-b8eb-57aba77dcd9d)

# Desafio para Desenvolvedor(a) Júnior - API RESTful

## Cenário:

Você foi contratado(a) por um banco fictício chamado **BankEasy** para desenvolver uma API REST que gerencie informações básicas sobre contas bancárias. 

O objetivo é criar um sistema onde o banco possa:

- Cadastrar clientes e suas contas bancárias.
- Consultar informações das contas.
- Realizar transações básicas (depósitos e saques).

**Requisitos Técnicos:**

1. **Linguagem e Framework:**
   - Django com [Django REST Framework (DRF)](https://www.django-rest-framework.org/).

2. **Banco de Dados:**
   - SQLite (ou outro banco embutido, para simplicidade).

3. **Funcionalidades:**
   - Cadastro de clientes:
     - Nome completo.
     - CPF (único).
     - Data de nascimento.
   - Cadastro de contas bancárias:
     - Número da conta (único).
     - Tipo da conta (Corrente ou Poupança).
     - Saldo inicial.
   - Consultar informações de um cliente pelo CPF.
   - Consultar informações de uma conta pelo número da conta.
   - Realizar transações:
     - **Depósito**: adicionar um valor ao saldo da conta.
     - **Saque**: subtrair um valor do saldo da conta (se houver saldo suficiente).

4. **Restrições:**
   - O saldo da conta não pode ser negativo.
   - Cada cliente pode ter no máximo 3 contas.

5. **Endpoints:**
   - `POST /clientes/`: para criar um cliente.
   - `POST /contas/`: para criar uma conta bancária vinculada a um cliente.
   - `GET /clientes/<cpf>/`: para consultar informações de um cliente.
   - `GET /contas/<numero_conta>/`: para consultar informações de uma conta.
   - `POST /transacoes/`: para realizar depósitos ou saques. 

6. **Validações:**
   - CPF deve ser válido e único.
   - O tipo de transação deve ser especificado como "depósito" ou "saque".
   - Para saques, verificar se há saldo suficiente antes de processar.

7. **Documentação:**
   - Documentar os endpoints utilizando ferramentas como Swagger ou DRF-YASG.

**Entregáveis:**

- Código-fonte em um repositório público no GitHub.
- Instruções claras no arquivo `README.md` para executar o projeto.
- Testes básicos para verificar o funcionamento da API (opcional, mas desejável).

**Critérios de Avaliação:**

1. Funcionalidade: a API deve atender aos requisitos descritos.
2. Estrutura e organização do código.
3. Qualidade das validações e tratamento de erros.
4. Uso correto de boas práticas do Django e DRF.
5. Clareza na documentação.

**Prazo para entrega:** 5 dias úteis.

---
