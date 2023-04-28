import numpy as np
from itertools import permutations
from math import factorial
from scipy.stats import entropy

def permutacionEntropyPRO(signal, m=3):
    """
    Esta función calcula la entropía de permutación de una señal dada. La entropía de permutación es un método de análisis
    de series temporales que se basa en las permutaciones de un vector de datos y se utiliza para cuantificar la complejidad
    de una señal.

    Args:
        signal: Un array unidimensional de números, que representa la señal de la cual se desea calcular la entropía de permutación.
        m: El tamaño de las sub-series a considerar para el cálculo de la entropía de permutación. El valor por defecto es 3.

    Returns:
        La entropía de permutación de la señal dada.

    """

    N = len(signal) - m + 1  # Número de sub-series de tamaño m en la señal
    P = np.zeros(factorial(m))  # Vector para almacenar el número de permutaciones de cada sub-serie
    perms = np.array(list(permutations(range(m))))  # Array con todas las permutaciones posibles de índices para sub-series de tamaño m

    # Calcular el número de veces que ocurre cada permutación en las sub-series de la señal
    for i in range(N):
        idx = np.argsort(signal[i:i+m])  # Obtener los índices que ordenan la sub-serie i
        perm_idx = np.where((perms == idx).all(axis=1))[0][0]  # Obtener el índice de la permutación en la lista de permutaciones posibles
        P[perm_idx] += 1  # Incrementar el contador correspondiente

    entropia = entropy(P, base=2)  # Calcular la entropía de la distribución de permutaciones

    return entropia

permutacion = np.array([4, 7, 9, 10, 6, 11, 3])  # Permutación de ejemplo

print(permutacionEntropyPRO(permutacion))  # Imprimir la entropía de permutación de la permutación de ejemplo

""" 
Si sea desea algo mas complejo puede buscar en librerias:
https://www.entropyhub.xyz/python/Examples/Ex1.html
"""
