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
Descripción

## Análisis de complejidad
tiempo y espacio en notación Big-O

## Estructuras de datos usadas
1. Lista de adyacencia: Representa el grafo como un diccionario {nodo: [(vecino, riesgo), ...]}.
   - Ventaja: eficiente en memoria cuando el grafo es disperso.
   - Justificación: más realista para redes donde no todos los nodos están conectados entre sí.
2. Arreglo dist[]: Guarda el riesgo acumulado mínimo desde el nodo inicial hasta cada nodo.
3. Arreglo prev[]: Permite reconstruir la ruta más segura al final del algoritmo.

## Restricciones
1.	Pesos de las aristas:
   - Deben ser enteros positivos.
   - Se definen en un rango, por ejemplo 1 = muy seguro, 10 = muy vulnerable.
   - No puede haber valores negativos.
2.	Conectividad del grafo:
   - El grafo debe ser conexo, es decir, que exista al menos una ruta entre cualquier par de nodos.
   - Si el grafo no es conexo, el algoritmo debe indicar que no existe ruta segura.
3.	Entrada válida:
   - Se debe especificar un nodo de inicio y un nodo destino.
   - Ambos nodos deben existir en el grafo (no se permite buscar rutas entre nodos inexistentes).
4.	Ruta única o múltiple:
   - Si hay varias rutas con el mismo riesgo total, el algoritmo devuelve una de ellas (no todas).
5.	Límites de tamaño:
   - Para la versión simple, el grafo debe ser de tamaño pequeño o mediano (ej. hasta 200 nodos).
   - Para la versión optimizada, se pueden manejar redes mucho más grandes
