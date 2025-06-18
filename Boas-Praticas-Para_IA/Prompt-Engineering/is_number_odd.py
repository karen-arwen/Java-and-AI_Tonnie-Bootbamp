
"""Crie uma função que recebe um numero inteiro e retorne se o numero é par ou impar
Se ele for impar retorne True, se for par retorne False
Caso o usuario não passe um numero inteiro, retorne um erro que não é um numero inteiro
se for 0 diga que é zero e diga que não é um numero desejado"""

def is_number_odd(number):
    
    if type(number) != int:
        raise ValueError("O valor informado não é um número inteiro")
    
    if number == 0:
        return ValueError("Zero não é um número desejado")
    if number % 2 == 0:
        return False    
    else:
        return True


