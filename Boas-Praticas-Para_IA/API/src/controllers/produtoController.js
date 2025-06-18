// src/controllers/produtoController.js
// Controlador de Produto: responsável pela lógica dos endpoints

// Importa o modelo de Produto
const Produto = require('../models/produto');
// Importa o schema de validação do produto
const produtoSchema = require('../validators/produtoValidator');

module.exports = {
  // Lista todos os produtos cadastrados
  listar: (req, res) => {
    res.json(Produto.listar());
  },

  // Cria um novo produto após validar os dados recebidos
  criar: (req, res) => {
    const { error, value } = produtoSchema.validate(req.body);
    if (error) {
      return res.status(400).json({ erro: error.details[0].message });
    }
    const novoProduto = Produto.criar(value);
    res.status(201).json(novoProduto);
  },

  // Edita um produto existente pelo ID, validando os dados recebidos
  editar: (req, res) => {
    const id = parseInt(req.params.id);
    if (!Produto.buscarPorId(id)) {
      return res.status(404).json({ erro: 'Produto não encontrado' });
    }
    const { error, value } = produtoSchema.validate(req.body);
    if (error) {
      return res.status(400).json({ erro: error.details[0].message });
    }
    const produtoEditado = Produto.editar(id, value);
    res.json(produtoEditado);
  },

  // Deleta um produto pelo ID
  deletar: (req, res) => {
    const id = parseInt(req.params.id);
    const sucesso = Produto.deletar(id);
    if (!sucesso) {
      return res.status(404).json({ erro: 'Produto não encontrado' });
    }
    res.status(204).send();
  }
};
