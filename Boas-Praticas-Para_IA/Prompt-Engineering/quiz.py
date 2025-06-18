# cria uma lista de questões com 5 perguntas e 4 possiveis respostas de cada
# cada pergunta deve ter uma resposta correta
# cada resposta correta vale 1 ponto
# esse quiz sera de varias capitais do mundo

import random
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
    }
]

# escreva uma função que recebe a questão e as exibe uma a uma para o usuario
# ela retorna a resposta do usuario e valida se a resposta está correta ou é um erro
def show_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")
    
    try:
        answer_index = int(input("Escolha a opção correta (1-4): ")) - 1
        if answer_index < 0 or answer_index >= len(question["options"]):
            raise ValueError("Opção inválida.")
        
        user_answer = question["options"][answer_index]
        if user_answer == question["answer"]:
            print("Resposta correta!")
            return True
        else:
            print(f"Resposta incorreta. A resposta correta é: {question['answer']}")
            return False
    except ValueError as e:
        print(f"Erro: {e}")
        return False
    

def main():
    pass


if __name__ == "__main__":
    main()