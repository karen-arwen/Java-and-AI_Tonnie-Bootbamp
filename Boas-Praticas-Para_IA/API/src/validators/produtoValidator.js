// src/validators/produtoValidator.js
// Define o schema de validação para produtos usando Joi

// Importa a biblioteca Joi para validação de dados
const Joi = require('joi');

// Esquema de validação para o objeto Produto
const produtoSchema = Joi.object({
  nome: Joi.string().min(3).max(100).required(), // Nome obrigatório, entre 3 e 100 caracteres
  preco: Joi.number().positive().required(),    // Preço obrigatório, número positivo
  descricao: Joi.string().max(255).optional()   // Descrição opcional, até 255 caracteres
});

// Exporta o schema para ser usado nos controllers
module.exports = produtoSchema;
