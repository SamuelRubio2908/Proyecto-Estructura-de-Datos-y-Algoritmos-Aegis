# Proyecto-Estructura-de-Datos-y-Algoritmos-Aegis
Documentación, instrucciones, ejemplos

## Problema Propuesto
Actualmente, la mayoría de las personas en el mundo están expuestas al robo de información o datos, ya que nuestros datos están almacenados en diferentes sectores, como las entidades públicas, bancos y hospitales alrededor del mundo. Nosotros vimos que estos entornos son puntos vulnerables para sufrir algún ataque cibernético si no están equipados con mecanismos de seguridad adecuados, y los que están actualmente pueden resultar siendo no suficientes ante este riesgo, ya que la tecnología esta evolucionando en una velocidad sin precedentes. En este ámbito los atacantes o hackers aprovechan diversas vías para obtener información, entre ellas.
Del mismo modo que vimos esta ventana en la ciberseguridad, en los últimos años se han presentado diversas noticias relacionadas a esta problemática y aunque algunas son más impactantes que otras, todas evidencian que puede llegar a afectar de una forma significativa en tres ámbitos: a nivel personal, que impacta directamente en los individuos, en el ámbito empresarial y a nivel social.
En la perspectiva personal uno de los riesgos más recurrentes es el robo de identidad, en el cual se utilizan los datos mas importantes como el nombre, la cédula o la información bancaria para solicitar créditos y/o realizar compras de una manera fraudulenta, además de poder realizar extorsiiones a los sujetos compremetidos.
De igual modo en el ámbito empresarial, las consecuencias suelen ser pérdidas económicas que se asocian a robos financieros, pero también pueden ser por sanciones legales gracias a el incumplimiento de normativas relacionadas a los tratamientos de datos o normativas de seguridad. Asi mismo se le suma que por este tipo de problemáticas en las empresas hay una fuga de clientes generado por la desconfianza en la empresa luego de una situación asi. Y en el último lugar esta el impacto de ataques como lo es el ransomware que es capaz de paralizar sistemas completos, lo que conlleva a interrumpir las operaciones del negocio.
Finalmente vamos con el ámbito social, el cual podríamos ver la suplantación de identidad masiva que puede haber si usan todos los datos robados y su implementación pueden ser en fraudes electorales, crear cuentas falsas en las diferentes redes sociales, entre otras cosas. Además de ellos esta que pueden vender esta información a diferentes empresas o también en la “dark wed”. La última afectación es que las personas teman a usar servidores digitales lo que afectaría a la economía digital.
Para concluir, al encontrar las afectaciones mencionadas anteriormente podemos ver que puede ser algo muy peligroso al estar en un mundo tan digitalizado y donde la información es tan importante. Por lo tanto, si no hayamos una solución para esta problemática, sabemos que existe varios sistemas de protección pero ninguna está especializada en el trato de datos. Además, la evolución de la tecnología ha hecho que los atacantes desarrollen métodos mas sofisticados, y por tanto se puede evidenciar que hay una necesidad de implementar mecanismos de seguridad más fuertes y robustos. Por ello es una prioridad que haya nuevas implementaciones en la seguridad digital.
Nuestra motivación para abarcar esta problemática es que, como próximos ingenieros informáticos debemos pensar en que problemáticas hay en la era digital en la que nos encontramos ya que nosotros también hacemos parte de la generación que está recibiendo estos cambios y problemas, y los tendremos que abordar en los próximos años. Adicionalmente, cuando tomamos la decisión de formarnos también nos surgió la duda de en qué podríamos aportar al mundo y este proyecto fue una posible respuesta a esa pregunta.





## Solución Formal
#### Código GCL
El algoritmo de Dijkstra es una técnica que nos permite encontrar el camino más corto (o en nuestro caso, el camino más seguro) entre un punto de origen y un destino dentro de un grafo ponderado.

En el grafo:
Los nodos representan puntos de conexión (por ejemplo, dispositivos, routers o servidores en una red).
Las aristas representan los enlaces entre esos nodos (las posibles conexiones).
El peso de cada arista representa el “riesgo” o nivel de inseguridad de esa conexión (entre más bajo, más segura es).

Nota: Como en nuestro proyecto el objetivo no es buscar rapidez sino seguridad, interpretamos los pesos como “riesgos de la red”, y buscamos el camino donde la suma de esos riesgos sea la menor posible.

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


## Análisis de complejidad
### Tiempo
El algoritmo de Dijkstra, cuando se implementa con un min-heap, que es la cola de prioridad, tiene la siguiente complejidad en tiempo:

Cada nodo puede ser insertado en la cola de prioridad varias veces, que es cuando se actualizan distancias.
En el peor caso, se hacen hasta m inserciones y n extracciones, donde:

n = número de nodos.
m = número de aristas.

Cada operación sobre el heap, osea, insertar o extraer mínimo, cuesta O(log n).

Por eso, el tiempo total es:
O((n+m) * log n)

Aunque en grafos densos, es decir, con muchas aristas, esto se suele simplificar a:
𝑂(𝑚 * log 𝑛)

### Espacio
El algoritmo de Dijkstra también necesita memoria extra además del grafo.
El grafo mismo, si está representado con listas de adyacencia, ocupa O(n + m), porque cada nodo guarda sus vecinos y pesos.
Los arreglos auxiliares (dist, previo, visitado) ocupan O(n).
La cola de prioridad min-heap puede crecer hasta O(m) en el peor caso (cuando muchas aristas actualizan distancias).

Por lo tanto, el peso total en el espacio seria de:
O(n+m)

## Estructuras de datos usadas
1. Lista de adyacencia: Representa el grafo como un diccionario o lista de listas. Tendría una estructura así:
   {nodo: [(vecino, riesgo), ...]}>
   Por ejemplo:
   grafo = {
     0: [(1, 5), (2, 2)], 
     1: [(2, 1)], 
     2: [(3, 3)] }}
   
   - Ventaja: eficiente en memoria cuando el grafo es disperso.
   - ¿Por qué?: más realista para redes donde no todos los nodos están conectados entre sí.
   
3. Arreglo dist[]: Guarda el riesgo acumulado mínimo desde el nodo inicial hasta cada nodo.
4. Arreglo prev[]: Permite reconstruir la ruta más segura al final del algoritmo.
5. Cola de prioridad (mean-heap): Se usa para elegir siempre el nodo “más prometedor”, es decir, el de menor riesgo acumulado hasta ese momento.
En Python se implementa con heapq.


## Restricciones
1.	Pesos de las aristas:
   - Deben ser enteros positivos.
   - Se definen en un rango, por ejemplo 1 = muy seguro, 10 = muy vulnerable.
2.	Conectividad del grafo:
   - El grafo debe ser conexo, es decir, que exista al menos una ruta entre cualquier par de nodos.
   - Si el grafo no es conexo, el algoritmo debe indicar que no existe ruta segura.
3.	Entrada válida:
   - Se debe especificar un nodo de inicio y un nodo destino.
   - Ambos nodos deben existir en el grafo (no se permite buscar rutas entre nodos inexistentes).
4.	Ruta única o múltiple:
   - Si hay varias rutas con el mismo riesgo total, el algoritmo devuelve una de ellas (no todas).
