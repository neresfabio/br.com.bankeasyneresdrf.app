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

## Documentação

### Migrations

As **migrations** (ou "migrações") do Django são um sistema para gerenciar alterações no esquema do banco de dados ao longo do tempo, de forma sincronizada com os modelos definidos no código. Elas permitem que você crie, atualize ou remova tabelas e campos no banco de dados automaticamente, sem a necessidade de escrever SQL manualmente.

### **Como funcionam as migrations no Django?**

1. **Definição de Modelos**:  
   Você define seus modelos (classes Python) em `models.py`, especificando os campos e seus tipos.

2. **Criação de Migrations**:  
   Quando você faz alterações nos modelos (por exemplo, cria uma nova tabela ou adiciona um campo a uma tabela existente), você executa o comando:
   ```bash
   python manage.py makemigrations
   ```
   Esse comando cria um arquivo de migração no diretório `migrations/` de cada app. Esse arquivo contém instruções sobre como aplicar (ou desfazer) as alterações no banco de dados.

3. **Aplicação das Migrations**:  
   Para aplicar as alterações no banco de dados, você usa o comando:
   ```bash
   python manage.py migrate
   ```
   Ele lê os arquivos de migração e executa os comandos necessários no banco de dados (como criar tabelas ou alterar colunas).

4. **Gerenciamento de Versões do Esquema**:  
   Cada migration é como uma versão do esquema do banco de dados. O Django mantém um registro de quais migrations já foram aplicadas, para garantir que o banco de dados esteja sempre em um estado consistente com o código.

---

### **Por que usar migrations?**

- **Automação**: Evitam a necessidade de escrever comandos SQL manualmente.
- **Histórico de Alterações**: Permitem reverter o esquema do banco para um estado anterior.
- **Portabilidade**: O mesmo arquivo de migração funciona em diferentes sistemas de banco de dados suportados pelo Django.
- **Facilidade no Desenvolvimento Colaborativo**: Em equipes, todos podem aplicar as mesmas migrations para manter o banco sincronizado.

---

### **Comandos principais relacionados a migrations**

- **Criar uma migração**:
  ```bash
  python manage.py makemigrations
  ```

- **Aplicar as migrações ao banco de dados**:
  ```bash
  python manage.py migrate
  ```

- **Exibir o estado das migrações aplicadas**:
  ```bash
  python manage.py showmigrations
  ```

- **Reverter uma migração específica**:
  ```bash
  python manage.py migrate <app_name> <migration_name>
  ```
  Exemplo:
  ```bash
  python manage.py migrate myapp 0001_initial
  ```

---

### **Fluxo prático:**

1. Você cria um modelo:
   ```python
   class Cliente(models.Model):
       nome = models.CharField(max_length=100)
       cpf = models.CharField(max_length=11, unique=True)
   ```

2. Gera a migração:
   ```bash
   python manage.py makemigrations
   ```

3. Aplica a migração:
   ```bash
   python manage.py migrate
   ```

O banco agora terá uma tabela `Cliente` com as colunas `nome` e `cpf`. 🎉

Se precisar de mais detalhes ou exemplos, só pedir!




