# Faça uma função nque me retorne datas dentro de um texto

import re
def find_dates_in_string(text):
    """
    Encontra todas as datas no formato DD/MM/AAAA dentro de uma string.
    
    Args:
        text (str): A string onde as datas serão procuradas.
        
    Returns:
        list: Uma lista de strings representando as datas encontradas.
    """
    date_pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
    return re.findall(date_pattern, text)


