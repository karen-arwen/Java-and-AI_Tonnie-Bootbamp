// src/models/produto.js
// Modelo de Produto (em memória)

// Array para armazenar os produtos em memória
let produtos = [];
// Variável para controlar o próximo ID disponível
let idAtual = 1;

module.exports = {
  // Retorna todos os produtos cadastrados
  listar: () => produtos,

  // Cria um novo produto e adiciona ao array
  criar: (dados) => {
    const novoProduto = { id: idAtual++, ...dados };
    produtos.push(novoProduto);
    return novoProduto;
  },

  // Edita um produto existente pelo ID
  editar: (id, dados) => {
    const produto = produtos.find(p => p.id === id);
    if (!produto) return null;
    produto.nome = dados.nome;
    produto.preco = dados.preco;
    produto.descricao = dados.descricao;
    return produto;
  },

  // Remove um produto do array pelo ID
  deletar: (id) => {
    const index = produtos.findIndex(p => p.id === id);
    if (index === -1) return false;
    produtos.splice(index, 1);
    return true;
  },

  // Busca um produto pelo ID
  buscarPorId: (id) => produtos.find(p => p.id === id)
};
