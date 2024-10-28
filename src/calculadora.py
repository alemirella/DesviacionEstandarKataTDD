import math
from typing import List, Union

class NoSePuedeCalcular(Exception):
    """Excepción lanzada cuando no se puede calcular promedio o desviación estándar."""
    pass

def calcular_promedio(elementos: List[Union[int, float]]) -> float:
    """Calcula el promedio de una lista de números."""
    if not elementos:
        raise NoSePuedeCalcular("No se puede calcular el promedio de una lista vacía.")
    if any(not isinstance(x, (int, float)) for x in elementos):
        raise TypeError("Todos los elementos deben ser numéricos.")
    return sum(elementos) / len(elementos)

def calcular_desviacion_estandar(elementos: List[Union[int, float]]) -> float:
    """Calcula la desviación estándar de una lista de números."""
    if not elementos:
        raise NoSePuedeCalcular("No se puede calcular la desviación estándar de una lista vacía.")
    if any(not isinstance(x, (int, float)) for x in elementos):
        raise TypeError("Todos los elementos deben ser numéricos.")
    if len(elementos) == 1:
        return 0.0
    promedio = calcular_promedio(elementos)
    varianza = sum((x - promedio) ** 2 for x in elementos) / len(elementos)
    return math.sqrt(varianza)
