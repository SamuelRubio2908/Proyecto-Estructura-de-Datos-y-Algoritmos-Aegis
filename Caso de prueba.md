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

Como podemos ver, lo que nos arroja es la distancia mas corta encontrada desd eel punto hasta todos los demás puntos del grafo. En este caso, que es algo pequeño, podemos mirar cada valor y ver que la distancia hasta el punto F esta anormalmente alta, lo cual más allá de significar que va a ser mucho más demorado comunicarse con ese nodo, tambien puede representar que puede ser riesgoso ese camino porque si tiene tanta latencia en comparacion a los demás, puede ser por un riesgo en el camino.
