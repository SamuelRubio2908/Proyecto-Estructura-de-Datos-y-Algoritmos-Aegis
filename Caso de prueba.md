# Caso de prueba
## Grafo
```
grafo = {
    'A': [('A', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 11)],
    'E': [('D', 4)],
    'F': []
}
```

En este caso, vamos a ingresar un grafo manualmente el cual tiene 6 nodos conectados entre si, y cada arista tiene un peso dado, que puede significar la latencia entre nodo y nodo. Y para que nos arroje un resultado, escribimos lo siguiente:

```print(dijkstra(grafo, 'A'))```

Lo que estamos haciendo es llamar a la funcion "dijkstra", ingresando el grafo que ya definimos y el punto desde el cual estamos partiendo. 

La salida esperado es lo siguiente:

{'A': 0, 'B': 4, 'C': 2, 'E': 5, 'D': 9, 'F': 20}

Como podemos ver, lo que nos arroja es la distancia mas corta encontrada desde el punto hasta todos los demás puntos del grafo. En este caso, que es algo pequeño, podemos mirar cada valor y ver que la distancia hasta el punto F esta anormalmente alta, lo cual más allá de significar que va a ser mucho más demorado comunicarse con ese nodo, tambien puede representar que puede ser riesgoso ese camino porque si tiene tanta latencia en comparacion a los demás, puede ser por un riesgo en el camino.

## Complejidad en este ejemplo
1. Parámetros del grafo

Número de vértices: |V| = 6

Número de aristas: |E| = 7

2. Complejidad general del algoritmo

Con una cola de prioridad (heap):
T (V,E)= O( (V+E)·log V)

3. Aplicamos a este ejemplo:
 
T (6,7) = O( (6+7)·log 6) = O (13·log 6)

Esto equivale a un número constante de operaciones en este tamaño pequeño de entrada.

Es decir que el tiempo aproximado va a ser proporcional a 13·log₆ ≈ 33 operaciones básicas, algo muy eficiente.

Ahora, en cuanto al espacio encontramos que:

Arreglo dist: O(V) = O(6)

Cola de prioridad: O(V + E) = O(13)

Total = O(V + E)

Por lo tanto, también es constante para este caso, y no es muy grande.
