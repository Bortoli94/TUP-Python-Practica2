
from typing import Any, List, Tuple

nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]


def combinar_basico(nombres: List[str], precios: List[float]) -> Tuple[Any]:
    """Toma dos listas y devuelve una tupla de duplas con los componentes de
    las listas.

    Restricción:
        - Utilizar un bucle FOR.
        - Utilizar la función range.
        - Utilizar índices.
    """
    result=[]
    dupla=[]
    for i in range(len(nombres)):
        dupla.extend([nombres[i],precios[i]])
        tupl = tuple(dupla)
        result.append(tupl)
        dupla.clear()
    return tuple(result)

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48),
    ("lámpara", 16.42),
    ("shampoo", 5.2),
)

assert combinar_basico(nombre_articulos, precio_articulos) == respuesta
# NO MODIFICAR - FIN