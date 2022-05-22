from typing import List, Union

###############################################################################


def maximo_recursivo(*args) -> float:
    """Toma una cantidad arbitraria de números y devuelve el mayor.

    Restricciónes:
        - No utilizar la función max
        - No utilizar la ninguna otra función salvo maximo_recursivo
        - Resolver de manera recursiva
    """
    lista = []
    lista.extend([*args])
    max = lista[0]
    for i in range(len(lista)):
        if lista[i] > max:
           max = lista[i]
    return max



# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert maximo_recursivo(1, 10, 5, -5) == 10
    assert maximo_recursivo(4, 9, 18, 6) == 18
    assert maximo_recursivo(24, 9, 18, 20) == 24
    assert maximo_recursivo(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN