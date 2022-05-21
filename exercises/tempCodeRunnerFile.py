from typing import Iterable
def suma_cubo_pares_sum_list(numeros: Iterable[int]) -> int:
    """Re-Escribir utilizando comprension de listas (debe resolverse en 1
    línea) y la función built-in sum.

    Referencias:
        - https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions # noqa: E501
        - https://docs.python.org/3/library/functions.html#sum
    """
    return sum([x for x in [j**3 for j in numeros] if x%2 == 0 ])

# NO MODIFICAR - INICIO
assert suma_cubo_pares_sum_list([1, 2, 3, 4, 5, 6]) == 288
# NO MODIFICAR - FIN