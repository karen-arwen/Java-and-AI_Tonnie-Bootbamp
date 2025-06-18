// src/routes/produtoRoutes.js
// Define as rotas relacionadas ao recurso Produto

// Importa o Express para criar o roteador
const express = require('express');
const router = express.Router();
// Importa o controller de produto, que contém a lógica das rotas
const produtoController = require('../controllers/produtoController');

// Rota para listar todos os produtos
router.get('/', produtoController.listar);
// Rota para criar um novo produto
router.post('/', produtoController.criar);
// Rota para editar um produto existente
router.put('/:id', produtoController.editar);
// Rota para deletar um produto
router.delete('/:id', produtoController.deletar);

// Exporta o roteador para ser usado no arquivo principal
module.exports = router;
