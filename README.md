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

### Solución Formal
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


### Breve recordatorio del proyecto 1

El proyecto se llama Aegis, y busca crear un sistema capaz de vigilar y detectar comportamientos anormales como posibles ataques cibernéticos.

La idea es que el sistema no solo monitoree el trafico de la red, sino que entienda como se muévela información dentro de la red también detectar cuando haya un riesgo para el usuario en la navegación que este realizando.

Para que el sistema pueda hacer todo lo que queremos, representamos la red como un grafo, una estructura matemática que permite modelar las conexiones en los distintos dispositivos, de esta forma el grafo nos permitirá simular el comportamiento real del tráfico. El sistema de Aegis de esa manera podrá analizar cual es el mejor camino para enviar datos delicados y comparar si el rendimiento real de esa ruta coincide con lo esperado. En pocas palabras se busca supervisa la red donde habrá comunicación entre los nodos y alertará cuando algo no ande bien.

### ¿Cómo este algoritmo soluciona parte del problema?

El algoritmo que escogimos es Dijkstra, y es clave en Aegis porque permite que se encuentre la ruta mas segura, corta o eficiente entre los dispositivos de la red de forma rápida y precisa.

Estas son las formas en como nos ayuda este algoritmo:
1.	Modelo:
Aegis toma los dispositivos y conexiones de la red y los convierte en un grafo ponderado cada enlace tiene un peso que representa su “costo”.
2.	Ejecución del algoritmo:
Dijkstra empieza desde un nodo origen, por ejemplo, el servidor principal y calcula la distancia mínima hacia todos los demás nodos. Lo hace avanzando de forma ordenada, siempre eligiendo el nodo con el menor costo acumulado hasta el momento esto se llama enfoque greedy o “avaro”. 
3.	Resultados:
El algoritmo construye un árbol de caminos mínimos. En este árbol, cada conexión representa la mejor ruta posible entre nodos, considerando el menor costo de transmisión.
5.	Análisis de rendimiento:
Una vez conocidas las rutas más eficientes teóricas, Aegis puede medir en tiempo real el desempeño real de cada enlace. Si el costo actual (por ejemplo, la latencia) es mucho mayor al esperado, se interpreta como una anomalía:
•	Puede deberse a congestión de red.
•	A una falla técnica.
•	Incluso a un ataque de denegación de servicio (DoS) o infiltración.
6.	Visualización y alertas:
Aegis muestra gráficamente la ruta más corta y resalta con alertas los cuellos de botella o puntos críticos que puede haber en la navegación.

En conclusión, Dijkstra le da a Aegis la capacidad de pensar de forma lógica: no solo encuentra las rutas óptimas, sino que aprende a reconocer cuándo algo no encaja con el comportamiento normal de la red lo que nos ayuda alertar al usuario. Todo lo que hace este algoritmo contribuye de una forma directa a la eficiencia y ciberseguridad en el sistema de Aegis.

### Justifiación del uso del algoritmo
Elegir el algoritmo de Dijkstra no es casualidad ya que había otras opciones como la fuerza bruta o los enfoques recursivos, pero al investigar sobre cada uno evidenciamos que el que mas concordaba con nosotros era Dijkstra en términos de eficiencia, complejidad y aplicabilidad real en redes modernas

Un enfoque de fuerza bruta implicaría explorar todas las rutas posibles entre los nodos para identificar cual es la ruta más corta, lo que resulta computacionalmente irrealizable en las redes reales, y esto tiene una complejidad factorial (O(V!)), lo que significa que el tiempo de ejecución seria mayor incluso con pocos nodos. Un ejemplo de ello sería:
•	En una red de 10 nodos, se podrían generar hasta 3,6 millones de rutas posibles.
•	En una red de 20 nodos, el número sería astronómico, haciendo el cálculo imposible en tiempo razonable.

Mientras que el algoritmo Dijkstra tiene una complejidad polinómica O((V + E) log V) gracias a su estrategia greedy (avara) y al uso de colas de prioridad, que permiten procesar los nodos más cercanos de una manera óptima.

Este algoritmo hace todo esto:
•	Evita exploraciones innecesarias, reduciendo radicalmente el tiempo de cómputo.
•	Garantiza resultados óptimos en grafos con pesos positivos.
•	Es el estándar en protocolos de enrutamiento modernos, como OSPF (Open Shortest Path First), que son utilizados en redes reales.
Lo que puede hacer en nuestro sistema de Aegis seria:
•	Analizar varios dispositivos y sus conexiones en segundos.
•	Actualizar rutas dinámicamente ante cambios en la red.
•	Detectar ataques o anomalías sin comprometer la velocidad de respuesta.

Por tanto, Dijkstra es la elección más adecuada porque combina precisión óptima y eficiencia práctica, dos cualidades esenciales para un entorno de monitoreo y defensa cibernética en tiempo real.
