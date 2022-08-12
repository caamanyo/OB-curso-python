numero = int(input("Escribe un número entero:"))

def es_entero(numero):
    """Calcula si un número es entero

    Args:
        numero (int):

    Returns:
        bool: Devuelve True o False
    """
    if numero <= 1:
        return False
    
    for num in range(2, numero):
        if numero % num == 0:
            return False
    
    return True

resultado = f"El número {numero} es primo." if es_entero(numero) else f"El número {numero} no es entero."

print(resultado)