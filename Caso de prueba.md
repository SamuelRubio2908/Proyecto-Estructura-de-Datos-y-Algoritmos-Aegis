# Caso de prueba
## Grafo
grafo = {
    'A': [('A', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 11)],
    'E': [('D', 4)],
    'F': []
}

En este caso, vamos a ingresar un grafo manualmente el cual tiene 6 nodos conectados entre si, y cada arista tiene un peso dado, que puede significar la latencia entre nodo y nodo. Y para que nos arroje un resultado, escribimos lo siguiente:

print(dijkstra(grafo, 'A'))

La salida esperado es lo siguiente:

{'A': 0, 'B': 4, 'C': 2, 'E': 5, 'D': 9, 'F': 20}

Como podremos ver, 
