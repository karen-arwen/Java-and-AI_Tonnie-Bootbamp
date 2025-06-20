# Documentação dos Scripts de Prompt Engineering

Este diretório contém scripts Python para aprendizado e prática de lógica, manipulação de strings e interação com o usuário. Abaixo, cada arquivo é detalhadamente documentado, com exemplos de uso e explicações técnicas.

---

## 1. is_number_odd.py

### Funções

#### `is_number_odd(number)`
- **Descrição:**
  - Verifica se um número é ímpar.
  - Retorna `True` se for ímpar, `False` se for par.
  - Se o valor não for inteiro, lança um `ValueError`.
  - Se for zero, retorna um `ValueError` especial.
- **Exemplo de uso:**
```python
is_number_odd(3)  # True
is_number_odd(4)  # False
is_number_odd(0)  # ValueError: Zero não é um número desejado
is_number_odd('a')  # ValueError: O valor informado não é um número inteiro
```

#### `is_prime(number)`
- **Descrição:**
  - Verifica se um número inteiro é primo.
  - Retorna `True` se for primo, `False` se não for.
  - Se não for inteiro, lança `ValueError`.
  - Números menores ou iguais a 1 não são primos.
- **Exemplo de uso:**
```python
is_prime(2)  # True
is_prime(9)  # False
is_prime(17) # True
is_prime(1)  # False
is_prime('b') # ValueError: O valor informado não é um número inteiro
```

---

## 2. find_dates_string_LearningShots.py

### Funções

#### `find_dates_in_string(text)`
- **Descrição:**
  - Encontra todas as datas no formato `DD/MM/AAAA` dentro de uma string.
  - Retorna uma lista de datas encontradas.
- **Exemplo de uso:**
```python
texto = 'Hoje é 20/06/2025 e amanhã será 21/06/2025.'
datas = find_dates_in_string(texto)
print(datas)  # ['20/06/2025', '21/06/2025']
```

---

## 3. quiz.py

### Descrição

Um quiz interativo sobre capitais do mundo, com perguntas embaralhadas, opções aleatórias, limite de tempo para resposta e feedback motivacional ao final.

### Como funciona
- O usuário tem 10 segundos para responder cada pergunta.
- As perguntas e opções são embaralhadas a cada execução.
- Ao final, é exibida a pontuação, a porcentagem de acertos e um feedback motivacional.

### Exemplo de execução
```
Bem-vindo ao Quiz de Capitais do Mundo!
┌──────────────────────────────────────────────┐
│ Qual é a capital do Japão?                   │
│ 1. Tóquio                                    │
│ 2. Seul                                      │
│ 3. Pequim                                    │
│ 4. Bangkok                                   │
└──────────────────────────────────────────────┘
Escolha a opção correta (1-4):
```

### Melhorias visuais sugeridas
- Uso de bordas e espaçamento para destacar perguntas e opções.
- Cores no terminal (usando ANSI escape codes para realçar acertos/erros).
- Mensagens de feedback motivacional ao final, conforme a porcentagem de acertos.

### Exemplo de feedback final
```
Sua pontuação final é: 7/10 (70.0% de acertos)
Quase lá! Continue assim!
```

---

## Observações Gerais
- Todos os scripts possuem tratamento de erros e exemplos de uso.
- Para rodar qualquer script, use: `python nome_do_arquivo.py`.
- Sinta-se livre para adaptar e expandir os scripts para novos desafios!
