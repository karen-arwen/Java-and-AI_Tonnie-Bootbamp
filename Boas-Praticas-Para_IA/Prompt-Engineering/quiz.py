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
    Deixa a interface mais bonita com bordas e cores.
    """
    # ANSI escape codes para cores
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    # Embaralha as opções de resposta
    options = question["options"][:]
    random.shuffle(options)
    # Monta a caixa da pergunta
    print(f"{CYAN}{BOLD}┌{'─'*46}┐{RESET}")
    print(f"{CYAN}{BOLD}│ {question['question']:<44}│{RESET}")
    for i, option in enumerate(options, start=1):
        print(f"{CYAN}{BOLD}│ {i}. {option:<41}{RESET}{CYAN}{BOLD}│{RESET}")
    print(f"{CYAN}{BOLD}└{'─'*46}┘{RESET}")
    try:
        answer = input_with_timeout(f"{YELLOW}Escolha a opção correta (1-4): {RESET}", 10)
        if answer is None:
            print(f'{RED}Pergunta perdida. A resposta correta é: {question["answer"]}{RESET}')
            return False
        answer_index = int(answer) - 1
        if answer_index < 0 or answer_index >= len(options):
            raise ValueError("Opção inválida.")
        user_answer = options[answer_index]
        if user_answer == question["answer"]:
            print(f"{GREEN}Resposta correta!{RESET}")
            return True
        else:
            print(f"{RED}Resposta incorreta. A resposta correta é: {question['answer']}{RESET}")
            return False
    except ValueError as e:
        print(f"{RED}Erro: {e}{RESET}")
        return False

# Função que percorre todas as perguntas e calcula a pontuação final
def check_answers(questions):
    """
    Percorre todas as perguntas, chama show_question para cada uma,
    soma os acertos e exibe a pontuação final, a porcentagem de acertos e um feedback personalizado.
    """
    score = 0
    for question in questions:
        if show_question(question):
            score += 1
    total = len(questions)
    percent = (score / total) * 100 if total > 0 else 0
    print(f"Sua pontuação final é: {score}/{total} ({percent:.1f}% de acertos)")
    # Feedback personalizado por faixa de porcentagem
    if percent == 0:
        print("Poxa, errou todas! Tente novamente!")
    elif percent <= 10:
        print("Que pena! Mas não desista, tente de novo!")
    elif percent <= 20:
        print("Ainda está difícil, mas continue praticando!")
    elif percent <= 30:
        print("Você está começando, não desanime!")
    elif percent <= 40:
        print("Quase na metade, continue tentando!")
    elif percent <= 50:
        print("Boa! Mas dá pra melhorar!")
    elif percent <= 60:
        print("Mais da metade! Está indo bem!")
    elif percent <= 70:
        print("Quase lá! Continue assim!")
    elif percent <= 80:
        print("Ótimo! Você sabe bastante!")
    elif percent <= 90:
        print("Excelente! Só mais um pouco para a perfeição!")
    elif percent < 100:
        print("Uau! Você é quase um gênio das capitais!")
    else:
        print("Parabéns, você é um gênio das capitais do mundo!!")

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