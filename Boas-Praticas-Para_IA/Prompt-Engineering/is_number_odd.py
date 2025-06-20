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

def is_prime(number):
    """
    Recebe um número inteiro e retorna True se for primo, False se não for primo.
    Se não for inteiro, lança ValueError. Se for 0 ou 1, retorna False (não são primos).
    """
    if type(number) != int:
        raise ValueError("O valor informado não é um número inteiro")
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


