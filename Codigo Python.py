import heapq

def ruta_segura_heap(grafo, inicio, fin):
    n = len(grafo)
  
    # --- Inicialización: O(n) ---
    dist = [float('inf')] * n          # distancia (riesgo acumulado) conocida más corta a cada nodo
    previo = [-1] * n                  # para reconstruir la ruta
    visitado = [False] * n             # marca nodos ya “fijados” (su dist es definitiva)

    dist[inicio] = 0.0
    heap = [(0.0, inicio)]             # min-heap por riesgo: (riesgo_acumulado, nodo). push: O(log n)

    # --- Bucle principal: O((n + m) log n) ---
    while heap:
        d, u = heapq.heappop(heap)     # extraer el no visitado con menor riesgo. O(log n)
        if visitado[u]:
            continue                   # entrada obsoleta; ya fijamos u antes (O(1))
        visitado[u] = True

        if u == fin:
            break                      # parada temprana: ya conocemos la mejor ruta a 'fin' (O(1))

        # Relajar aristas de u: el total de iteraciones en todo el algoritmo es O(m)
        for v, riesgo in grafo[u]:
            # Si pasar por u mejora la mejor distancia conocida a v...
            nd = d + riesgo
            if nd < dist[v]:
                dist[v] = nd
                previo[v] = u
                heapq.heappush(heap, (nd, v))  # O(log n)

    # --- Reconstrucción de la ruta: O(longitud de la ruta) ≤ O(n) ---
    if dist[fin] == float('inf'):
        return [], float('inf')         # inalcanzable

    ruta = []
    nodo = fin
    while nodo != -1:
        ruta.append(nodo)
        nodo = previo[nodo]
    ruta.reverse()

    return ruta, dist[fin]
