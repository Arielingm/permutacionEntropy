# permutacionEntropy
Función: permutacionEntropyPRO(signal, m=3)

Descripción:

Esta función calcula la entropía de permutación de una señal dada utilizando la longitud de permutación (m) especificada. La entropía de permutación se calcula utilizando la fórmula de la entropía de Shannon.

Parámetros de entrada:

signal: una señal unidimensional en forma de array de numpy.
m (opcional): la longitud de permutación deseada. El valor predeterminado es 3.
Valor de salida:

entropia: el valor de la entropía de permutación calculado para la señal dada.
Librerías requeridas:

numpy
itertools
math
scipy.stats
Uso:

La función se puede utilizar llamándola y pasando la señal como el primer argumento y opcionalmente la longitud de permutación deseada como segundo argumento. Por ejemplo:
permutacion = np.array([4, 7, 9, 10, 6, 11, 3])
entropia = permutacionEntropyPRO(permutacion)
