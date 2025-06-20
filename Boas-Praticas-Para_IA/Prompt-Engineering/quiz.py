# Quiz de Capitais do Mundo
# Este script implementa um quiz interativo sobre capitais do mundo, com limite de tempo para resposta.

import random  # Importa o módulo para embaralhar perguntas e respostas
import threading  # Importa o módulo para criar threads (usado no timeout do input)
import sys

# Lista de perguntas do quiz, cada uma com 4 opções e uma resposta correta
questions = [
    {
        "question": "Qual é a capital da França?",
        "options": ["Paris", "Londres", "Berlim", "Madri"],
        "answer": "Paris"
    },
    {
        "question": "Qual é a capital do Japão?",
        "options": ["Tóquio", "Seul", "Pequim", "Bangkok"],
        "answer": "Tóquio"
    },
    {
        "question": "Qual é a capital do Brasil?",
        "options": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
        "answer": "Brasília"
    },
    {
        "question": "Qual é a capital da Itália?",
        "options": ["Roma", "Milão", "Veneza", "Florença"],
        "answer": "Roma"
    },
    {
        "question": "Qual é a capital da Austrália?",
        "options": ["Canberra", "Sydney", "Melbourne", "Brisbane"],
        "answer": "Canberra"
    },
    # Novas perguntas adicionadas
    {
        "question": "Qual é a capital do Canadá?",
        "options": ["Toronto", "Ottawa", "Vancouver", "Montreal"],
        "answer": "Ottawa"
    },
    {
        "question": "Qual é a capital da Rússia?",
        "options": ["São Petersburgo", "Moscou", "Kazan", "Novosibirsk"],
        "answer": "Moscou"
    },
    {
        "question": "Qual é a capital da Argentina?",
        "options": ["Buenos Aires", "Córdoba", "Rosário", "Mendoza"],
        "answer": "Buenos Aires"
    },
    {
        "question": "Qual é a capital da África do Sul?",
        "options": ["Cidade do Cabo", "Pretória", "Joanesburgo", "Durban"],
        "answer": "Pretória"
    },
    {
        "question": "Qual é a capital da Índia?",
        "options": ["Nova Délhi", "Mumbai", "Bangalore", "Chennai"],
        "answer": "Nova Délhi"
    }
]

# Função para ler a resposta do usuário com limite de tempo (timeout)
def input_with_timeout(prompt, timeout):
    """
    Exibe um prompt e aguarda a resposta do usuário por até 'timeout' segundos.
    Retorna a resposta ou None se o tempo esgotar.
    """
    result = [None]
    def inner():
        try:
            result[0] = input(prompt)
        except Exception:
            result[0] = None
    thread = threading.Thread(target=inner)
    thread.daemon = True
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        print('\nTempo esgotado!')
        return None
    return result[0]

# Função que exibe uma pergunta, embaralha as opções e valida a resposta do usuário
def show_question(question):
    """
    Mostra a pergunta e as opções (embaralhadas), aguarda resposta do usuário
    por até 10 segundos. Informa se acertou, errou ou perdeu a pergunta por tempo.
    """
    print(question["question"])
    # Embaralha as opções de resposta
    options = question["options"][:]
    random.shuffle(options)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    try:
        answer = input_with_timeout("Escolha a opção correta (1-4): ", 10)
        if answer is None:
            print(f'Pergunta perdida. A resposta correta é: {question["answer"]}')
            return False
        answer_index = int(answer) - 1
        if answer_index < 0 or answer_index >= len(options):
            raise ValueError("Opção inválida.")
        user_answer = options[answer_index]
        if user_answer == question["answer"]:
            print("Resposta correta!")
            return True
        else:
            print(f"Resposta incorreta. A resposta correta é: {question['answer']}")
            return False
    except ValueError as e:
        print(f"Erro: {e}")
        return False

# Função que percorre todas as perguntas e calcula a pontuação final
def check_answers(questions):
    """
    Percorre todas as perguntas, chama show_question para cada uma,
    soma os acertos e exibe a pontuação final.
    """
    score = 0
    for question in questions:
        if show_question(question):
            score += 1
    print(f"Sua pontuação final é: {score}/{len(questions)}")

# Função principal do programa
def main():
    """
    Dá boas-vindas, embaralha as perguntas e inicia o quiz.
    """
    print("Bem-vindo ao Quiz de Capitais do Mundo!")
    random.shuffle(questions)  # Embaralha a ordem das perguntas
    check_answers(questions)
    print("Obrigado por jogar!")
    pass

# Executa o programa se for chamado diretamente
if __name__ == "__main__":
    main()