# permutacionEntropyPRO

## Descripción

La función `permutacionEntropyPRO` calcula la entropía de permutación de una señal unidimensional dada utilizando la longitud de permutación (m) especificada. La entropía de permutación es una métrica utilizada en el análisis de series temporales para cuantificar la complejidad de una señal.

## Parámetros de Entrada

- `signal`: Una señal unidimensional representada como un array de NumPy.

- `m` (opcional): La longitud de permutación deseada. El valor predeterminado es 3.

## Valor de Salida

- `entropia`: El valor de la entropía de permutación calculado para la señal dada.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas:

- NumPy
- SciPy

## Uso

Puedes utilizar la función llamándola y pasando la señal como el primer argumento y opcionalmente la longitud de permutación deseada como el segundo argumento. Ejemplo de uso:

```python
import numpy as np

# Definir una señal de ejemplo
permutacion = np.array([4, 7, 9, 10, 6, 11, 3])

# Calcular la entropía de permutación
entropia = permutacionEntropyPRO(permutacion)

# Imprimir el resultado
print("Entropía de Permutación:", entropia)
```
## Más información

Si sea desea algo mas complejo puede buscar en librerias:

- [EntropyHub](https://www.entropyhub.xyz/python/Examples/Ex1.html)


