// index.js
// Arquivo principal da API RESTful para gerenciar produtos

// Importa o framework Express para criar o servidor
const express = require('express');
const app = express();
const PORT = 3000;

// Middleware para permitir que o Express leia requisições com corpo em JSON
app.use(express.json());

// Importa as rotas organizadas dos produtos
const produtoRoutes = require('./src/routes/produtoRoutes');

// Usa as rotas de produto para todas as requisições que começam com /produtos
app.use('/produtos', produtoRoutes);

// Inicia o servidor na porta definida e exibe uma mensagem no console
app.listen(PORT, () => {
  console.log(`API rodando em http://localhost:${PORT}`);
});
