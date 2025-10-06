# Proyecto-Estructura-de-Datos-y-Algoritmos-Aegis
Documentación, instrucciones, ejemplos

## Algoritmo Central del Proyecto

### Contexto
Nombre del algoritmo: Algoritmo de Dijkstra (Edsger Dijkstra, 1956).

Explicación teórica:
El algoritmo resuelve el problema de caminos más cortos en un grafo ponderado, dirigido o no dirigido y es muy importante que no puede tener pesos negativos. Además, construye de manera iterativa un árbol de caminos más cortos desde un vértice fuente `s` hasta todos los demás vértices. Y la estrategia que usa es un enfoque voráz o greedy (avaro), ya que en cada paso selecciona el vértice no visitado con la menor distancia conocida y actualiza las distancias de sus adyacentes.

El resultado es el camino más corto desde la fuente.

Lo que hace el algoritmo es algo así:
1. Inicializa todas las distancias en ∞ (infinito) excepto la del vértice fuente (s), que se pone a 0.
2. Usa una cola de prioridad (min-heap) para elegir y procesar siempre el vértice (u) con la menor distancia conocida desde la fuente.
3. Para cada vecino (v) del vértice actual (u), intenta relajar (actualizar) la arista:
```
   si distancia[u] + peso(u,v) < distancia[v] 
      entonces actualizar distancia[v] y añadir v a la cola
```
4. Repite hasta que la cola de prioridad esté vacía (es decir, hasta visitar todos los vértices alcanzables).

El Resultado es el array dist que contendrá el costo mínimo del camino desde la fuente s hasta cada vértice v.

#### Complejidad del algoritmo

Temporal: O((V+E) log V)

La clave está en la cola de prioridad ya que lo podemos ver la siguiente manera:
- Cada extracción del vértice más cercano cuesta `O(log V)`.
- Se hacen `V` extracciones, por lo tanto nos cuesta `O(V log V)`.
- Cada arista `E` puede provocar una disminución de clave (`decrease-key`), por lo tnato costaría`O(E log V)`.

Combinando, nos da una complejidad temporal **O((V+E) log V)**.

Esto es más eficiente que la versión básica de Dijkstra con matriz de adyacencia (`O(V^2)`).

Espacio: O(V+E)

- O(V) para almacenar distancias, visitados y la cola de prioridad.
- O(E) para guardar la representación del grafo (listas de adyacencia).
- En total: **O(V+E)**.

### ¿Qué hago con este algoritmo y donde se clasifica?
El algoritmo de Dijkstra es un método clásico que se utiliza para encontrar el camino más corto desde un nodo de inicio hasta todos los demás nodos en un grafo que tiene pesos positivos. Este algoritmo se basa en un enfoque **voraz** (se clasifica dentro de los algoritmos voraces), lo que significa que en cada paso toma la decisión que parece más conveniente en ese momento, con la esperanza de llegar a la mejor solución en general.

¿Cómo funciona?
Primero, mantiene una lista de las distancias acumuladas desde el nodo de inicio. Luego, utiliza una cola de prioridad para asegurarse de elegir siempre el nodo con la menor distancia conocida. A medida que avanza, va actualizando las distancias de los nodos vecinos si encuentra un camino más corto.
Las principales características de los algoritmos voraces son las siguientes:
- Decisiones locales óptimas: en cada etapa, se elige la opción que parece ser la mejor en ese instante.
- Irrevocabilidad: una vez que se toma una decisión, no se corrige ni se modifica más adelante.
- Limitaciones: aunque no siempre garantizan la mejor solución global, son muy efectivos en problemas que cumplen con la propiedad de subestructura óptima y la elección voraz

## Solución Formal
En el grafo:
Los nodos representan puntos de conexión (por ejemplo, dispositivos, routers o servidores en una red).
Las aristas representan los enlaces entre esos nodos (las posibles conexiones). El peso de cada arista representa la latencia o el ancho de banda (siendo 1/ancho de banda)

Cómo Funciona:
   - Se asume que al inicio, todos los nodos están infinitamente lejos del origen (dist[i] = ∞).
   - El único nodo con distancia conocida es el de origen, al cual le asignamos 0.
   - Uso de un min-heap (cola de prioridad, en el cúal cada elemento que ingresa tiene cierta prioridad, y entre más prioridad, más al final está, es decir, el que tiene mayor prioridad sale primero. No importa el orden en que ingresen, se posicionarán segun su prioridad)
   - Aquí guardamos siempre el nodo más prometedor a visitar, es decir, el que hasta ahora tiene la distancia más baja.
   - Exploración de vecinos (relajación)
   - Tomamos el nodo más cercano (o más seguro en nuestro caso).
   - Revisamos sus vecinos: si llegar a ellos a través del nodo actual resulta en una distancia menor (un camino más seguro), entonces actualizamos esa distancia.
   - Reconstrucción del camino
   - Cuando llegamos al destino, usamos el arreglo de previo[] para reconstruir cuál fue el camino seguido.

En resumen: Dijkstra va expandiendo paso a paso las rutas más prometedoras y se detiene cuando encuentra la mejor posible para llegar al destino.

#### Código Python
El código en Python se apoya en una estructura llamada heapq, que permite manejar una cola de prioridad de forma eficiente.

Cómo funciona:
   - Se prepara una lista de distancias, marcando todas como infinitas, excepto el nodo origen que arranca en 0.
   - Se mete el origen a la cola de prioridad.
   - Mientras haya nodos en la cola, se va sacando el más prometedor.
   - Se actualizan las distancias de los vecinos si encontramos un camino más corto (más seguro).
   - Al final, se reconstruye el camino usando el arreglo previo.
