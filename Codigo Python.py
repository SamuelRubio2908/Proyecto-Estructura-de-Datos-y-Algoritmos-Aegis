import heapq  # Importa la librería para usar colas de prioridad (min-heap).

def dijkstra(grafo, origen):
    # Inicializa las distancias a infinito para cada nodo del grafo
    dist = {nodo: float('inf') for nodo in grafo}  
    
    dist[origen] = 0  
    
    pq = [(0, origen)]  # Cola de prioridad con tupla (distancia, nodo)
    
    while pq:  # Se ejecuta mientras haya elementos en la cola
        # heapq.heappop extrae el menor elemento
        distancia, nodo = heapq.heappop(pq)
        
        if distancia > dist[nodo]:
            continue  
        
        # Recorremos vecinos del nodo
        for vecino, peso in grafo[nodo]:  
          
            nueva_dist = distancia + peso  
          
            if nueva_dist < dist[vecino]:  
          
                dist[vecino] = nueva_dist  
          
                heapq.heappush(pq, (nueva_dist, vecino))  
          
    return dist  
    # Devuelve las distancias mínimas
