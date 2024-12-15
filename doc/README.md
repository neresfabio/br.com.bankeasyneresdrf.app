# Planejamento

### **1. Compreender os Requisitos**
   - Leia atentamente o enunciado para entender o objetivo do projeto.
   - Liste as funcionalidades principais (cadastro de clientes, cadastro de contas, transações, etc.).
   - Identifique as validações e restrições exigidas (CPF único, saldo não pode ser negativo, etc.).
   - Visualize como os endpoints e a estrutura do projeto serão interligados.

---

### **2. Planejamento do Projeto**
   - **Divida o projeto em tarefas menores**:
     - Configurar o ambiente.
     - Criar o modelo de clientes.
     - Criar o modelo de contas.
     - Implementar os endpoints CRUD para clientes e contas.
     - Implementar os endpoints para transações.
     - Adicionar validações.
     - Documentar e testar.
   - Priorize tarefas básicas antes de adicionar funcionalidades extras.
   - Crie uma estrutura inicial para gerenciar o tempo e garantir que todas as funcionalidades sejam implementadas.

---

### **3. Configurar o Ambiente**
   - Instale o Django e Django REST Framework no ambiente local:
     ```bash
     pip install django djangorestframework
     ```
   - Inicie um novo projeto Django:
     ```bash
     django-admin startproject bank_easy
     cd bank_easy
     ```
   - Crie um app para a API:
     ```bash
     python manage.py startapp api
     ```
   - Adicione o app `api` e `rest_framework` no `settings.py`.

---

### **4. Modelagem do Banco de Dados**
   - Defina os **modelos** com base nos requisitos:
     - Modelo `Cliente`:
       - Nome completo
       - CPF (único)
       - E-mail (único)
       - Telefone
       - Data de nascimento
       - Data de criação do registro
       - createdAt
       - updateAt
     - Modelo `ContaBancaria`:
       - Cliente (chave estrangeira para o modelo de Clientes)
       - Número da conta (único)
       - Tipo de conta (corrente, poupança)
       - Saldo inicial (padrão: 0.00)
       - Data de criação da conta
   - Adicione validações básicas, como a unicidade do CPF e número da conta.
   - Realize a migração para criar as tabelas:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

---

### **5. Desenvolvimento dos Endpoints**
   - **Endpoints CRUD**:
     - Use serializers e views do DRF para criar as operações básicas de clientes e contas.
     - Exemplo: `ListCreateAPIView` para listar e criar clientes.
   - **Endpoints de Transações**:
     - Crie uma lógica para verificar se o saldo é suficiente para saques.
     - Use uma view personalizada para processar as transações.

---

### **6. Validações e Regras de Negócio**
   - Adicione validações no `serializer` ou nos modelos:
     - CPF único.
     - Saldo não pode ser negativo.
     - Um cliente não pode ter mais de 3 contas.
   - Garanta que as transações sejam registradas corretamente.

---

### **7. Testes**
   - Teste os endpoints manualmente usando o **Postman** ou **cURL**.
   - Crie testes automatizados para verificar se os endpoints funcionam conforme esperado:
     - Teste criação de cliente.
     - Teste criação de conta.
     - Teste transações.

---

### **8. Documentação**
   - Configure o Swagger ou DRF-YASG para gerar a documentação da API.
   - Garanta que os endpoints estejam documentados com exemplos de entrada e saída.

---

### **9. Finalização**
   - Escreva um arquivo `README.md` com as instruções de instalação, configuração e execução do projeto.
   - Suba o código no GitHub.
   - Revise o projeto antes de enviar, verificando se os requisitos foram atendidos.

---

Esse planejamento vai ajudar o desenvolvedor a se organizar e progredir de forma estruturada no desafio! 🚀
