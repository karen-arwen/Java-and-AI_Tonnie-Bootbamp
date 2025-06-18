# API de Gerenciamento de Produtos

## Descrição Geral
Esta API RESTful foi desenvolvida para facilitar o gerenciamento de produtos em sistemas de e-commerce, catálogos ou prototipagem. Ela permite criar, listar, editar e excluir produtos de forma simples, segura e validada.

## Objetivos
- Prover uma interface padronizada para manipulação de produtos
- Garantir a validação dos dados recebidos
- Facilitar a integração com frontends, sistemas de testes e automações
- Servir como base para projetos maiores, podendo ser facilmente expandida

## Funcionalidades
- Cadastro de novos produtos
- Listagem de todos os produtos
- Atualização de produtos existentes
- Remoção de produtos
- Validação de dados de entrada
- Respostas padronizadas em JSON

## Tecnologias Utilizadas
- **Node.js**: Ambiente de execução JavaScript
- **Express**: Framework para criação de APIs
- **Joi**: Validação de dados

---

## Instruções de Instalação
1. Clone o repositório ou copie os arquivos para sua máquina.
2. No terminal, navegue até a pasta `API`:
   ```bash
   cd Boas-Praticas-Para_IA/API
   ```
3. Instale as dependências:
   ```bash
   npm install
   ```
4. Inicie o servidor:
   ```bash
   npm start
   ```
5. A API estará disponível em `http://localhost:3000`

---

## Estrutura do Produto
| Campo      | Tipo    | Obrigatório | Descrição                        |
|------------|---------|-------------|----------------------------------|
| id         | Inteiro | Não         | Identificador único do produto   |
| nome       | String  | Sim         | Nome do produto (3-100 caracteres) |
| preco      | Número  | Sim         | Preço do produto (positivo)      |
| descricao  | String  | Não         | Descrição do produto (até 255 caracteres) |

---

## Endpoints e Exemplos

### 1. Listar Produtos
- **GET** `/produtos`
- **Descrição:** Retorna todos os produtos cadastrados.
- **Exemplo de requisição:**
  ```http
  GET http://localhost:3000/produtos
  ```
- **Exemplo de resposta:**
  ```json
  [
    {
      "id": 1,
      "nome": "Camiseta",
      "preco": 49.9,
      "descricao": "Camiseta 100% algodão"
    }
  ]
  ```

### 2. Criar Produto
- **POST** `/produtos`
- **Descrição:** Cria um novo produto.
- **Exemplo de requisição:**
  ```http
  POST http://localhost:3000/produtos
  Content-Type: application/json
  
  {
    "nome": "Camiseta",
    "preco": 49.9,
    "descricao": "Camiseta 100% algodão"
  }
  ```
- **Exemplo de resposta:**
  ```json
  {
    "id": 2,
    "nome": "Camiseta",
    "preco": 49.9,
    "descricao": "Camiseta 100% algodão"
  }
  ```

### 3. Editar Produto
- **PUT** `/produtos/{id}`
- **Descrição:** Atualiza um produto existente pelo ID.
- **Exemplo de requisição:**
  ```http
  PUT http://localhost:3000/produtos/1
  Content-Type: application/json
  
  {
    "nome": "Camiseta Premium",
    "preco": 59.9,
    "descricao": "Camiseta 100% algodão premium"
  }
  ```
- **Exemplo de resposta:**
  ```json
  {
    "id": 1,
    "nome": "Camiseta Premium",
    "preco": 59.9,
    "descricao": "Camiseta 100% algodão premium"
  }
  ```

### 4. Deletar Produto
- **DELETE** `/produtos/{id}`
- **Descrição:** Remove um produto pelo ID.
- **Exemplo de requisição:**
  ```http
  DELETE http://localhost:3000/produtos/1
  ```
- **Exemplo de resposta:**
  - Status: 204 (sem corpo)

---

## Códigos de Resposta
| Código | Significado                |
|--------|----------------------------|
| 200    | Sucesso                    |
| 201    | Criado com sucesso         |
| 204    | Removido com sucesso       |
| 400    | Erro de validação          |
| 404    | Não encontrado             |

---

## Exemplos de Erros
- **Erro de validação:**
  ```json
  {
    "erro": "\"nome\" is required"
  }
  ```
- **Produto não encontrado:**
  ```json
  {
    "erro": "Produto não encontrado"
  }
  ```

---

## Observações
- Todos os campos são validados.
- O campo `descricao` é opcional.
- Utilize o header `Content-Type: application/json` para POST e PUT.
- O armazenamento é em memória (os dados são perdidos ao reiniciar o servidor).
- Para produção, recomenda-se integrar com um banco de dados.

---

