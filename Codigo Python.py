import heapq

def dijkstra_heap(grafo, inicio, fin):
    n = len(grafo)

    # --- Inicialización: O(n) ---
    dist = [float('inf')] * n          # distancia más corta conocida hasta cada nodo
    previo = [-1] * n                  # para reconstruir el camino
    visitado = [False] * n             # nodos cuya distancia ya es definitiva

    dist[inicio] = 0.0
    heap = [(0.0, inicio)]             # min-heap: (distancia acumulada, nodo). Insertar: O(log n)

    # --- Bucle principal: O((n + m) log n) ---
    while heap:
        d, u = heapq.heappop(heap)     # extraer el nodo no visitado más cercano. O(log n)
        if visitado[u]:
            continue                   # ignorar si ya fue procesado antes (O(1))
        visitado[u] = True             # fijamos la distancia definitiva de u (O(1))

        if u == fin:
            break                      # parada temprana opcional (O(1))

        # Relajación de aristas: en total O(m) veces
        for v, peso in grafo[u]:
            nd = d + peso
            if nd < dist[v]:           # mejora encontrada
                dist[v] = nd
                previo[v] = u
                heapq.heappush(heap, (nd, v))  # insertar en heap. O(log n)

    # --- Reconstrucción del camino: O(n) en el peor caso ---
    if dist[fin] == float('inf'):
        return [], float('inf')        # no hay ruta

    ruta = []
    nodo = fin
    while nodo != -1:
        ruta.append(nodo)
        nodo = previo[nodo]
    ruta.reverse()

    return ruta, dist[fin]
