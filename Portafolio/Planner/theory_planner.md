English:

In the industry, managing production orders according to the available capacity of resources is of utmost importance. The mathematical model we present is designed to maximize the efficiency of this process. It allows us to complete orders that fit within the current resource capacity and, consequently, to process all those that do not exceed capacity limits. When the available capacity is not sufficient for the next order, the default strategy is to recharge the resource to its maximum capacity to ensure the continuity of production. However, with the implementation of the alternative proposal, 'option b', we optimize the process by adjusting the resource volume according to a predetermined fill decision function. This improvement not only avoids unnecessary maximum filling but also ensures that subsequent orders are efficiently fulfilled. My goal is to demonstrate how through modeling and programming we can optimize industrial processes, enhancing productivity and resource management.

Let $O = order_{1}, order_{2}, ..., order_{n}$ be a set of orders to be satisfied.
We define the tuple
1) $$(order_{i},(quantity_{i} , time_{i}))$$
as order $i$with quantity to produce quantity $i$, where each unit of production of order $i$ takes time $i$ time units.
For simplicity, we denote $order_{i} = o_{i}, quantity_{i} = q_{i}, time_{i} = t_{i}$, that is:

2) $$(o_{i},(q_{i} , t_{i}))$$

We denote the resource capacity by $C(R,t)$ at time $t$, then we say that an order is satisfied if:

3) $$(o_{i},(q_{i} , t_{i})) \leq C(R,t_{i})$$

Then, we define $D$ as that set of orders that fulfill condition 3), that is:
$$D = \{{(o_{j},(q_{j} , t_{j}))\mid j = 1,2,...,m}\}$$

If there is at least one order $k$ such that condition 3) is not met, then $C(R,t_{k}) < (o_{k},(q_{k} , t_{k}))$

For this case, we propose 2 solutions that model the usual behaviors in a situation like the previous one.

Let $V(t_{i})$ be the variable that denotes the Resource volume at time $t_{i}$.

a) $$V(t_{i}) = max(C(R,t_{i}))$$

This implies that, if the order cannot be satisfied, the resource must be filled to its maximum capacity.

For the next solution, we must define a fill decision function as follows:

$$L(t_{i}) = \left\{\begin{matrix} 1 \; \text{If } V(t_{i-1})-q_{i-1} < q_{i} & \\0 \; \text{In any other case} & \end{matrix}\right.$$

b) $$V(t_{i}) = V(t_{i-1})-q_{i-1} +L(t_{i})(C'(R,t)-V(t_{i-1})-q_{i-1})$$
Where $C'(R,t)$ represents the capacity that the tank should have to meet the following orders without the need to fill the resource to the maximum.

In any case, taking a) or b) would involve applying 3) until $D$ represents the maximum of our orders. That is, when all our orders have been satisfied.

____

Español:

En la industria, administrar las órdenes de producción de acuerdo con la capacidad disponible de los recursos es de suma importancia. El modelo matemático que presentamos se diseñó para maximizar la eficiencia de este proceso. Nos permite completar las órdenes que se ajustan a la capacidad actual del recurso y, en consecuencia, procesar todas aquellas que no excedan los límites de capacidad. Cuando la capacidad disponible no es suficiente para la orden siguiente, la estrategia predeterminada es recargar el recurso hasta su capacidad máxima para garantizar la continuidad de la producción. Sin embargo, con la implementación de la propuesta alternativa, la 'opción b', optimizamos el proceso al ajustar el volumen de recurso según una función de decisión de llenado predeterminada. Esta mejora no solo evita el llenado innecesario al máximo, sino que también asegura que las órdenes subsecuentes se cumplan de manera eficiente. Mi meta es demostrar cómo a través de la modelización y la programación podemos optimizar procesos industriales, elevando la productividad y la gestión de recursos.

Sea $O = {order_{1}, order_{2} ,..., order_{n}}$ un conjunto de ordenes a satisfacer.
Definimos la tupla
1) $$(order_{i},(quantity_{i} , time_{i}))$$
como la order $i$ con cantidad a producir quantity $i$, en donde cada unidad de produccion de la order $i$ toma time $i$ unidades de tiempo.
Por simplicidad, denotamos  $order_{i} = o_{i}, quantity_{i} = q_{i}, time_{i} = t_{i}$, esto es:

2) $$(o_{i},(q_{i} , t_{i}))$$

Denotamos la capacidad del recurso por $C(R,t)$ en el tiempo $t$, entonces decimos que una orden es satisfecha si se cumple que:

3) $$(o_{i},(q_{i} , t_{i}))\leq C(R,t_{i})$$

Entonces, definimos $D$ como aquel conjunto de ordenes que cumple $3$, es decir:
$$D = \{{(o_{j},(q_{j} , t_{j}))\mid j = 1,2,...,m}\}$$

Si existe al menos una orden $k$ tal que no se cumple $3)$ entonces, se tiene que $C(R,t_{k})<(o_{k},(q_{k} , t_{k}))$

Para este caso, proponemos 2 soluciones que modelan los comportamientos habituales ante una situacion como la anterior.

Sea $V(t_{i})$ la variable que denota el volumen del Recurso en el tiempo $t_{i}$.

a) $$V(t_{i}) = max(C(R,t_{i}))$$

Lo anterior implica que, si la orden no se puede satisfacer, el recurso deberá llenarse hasta el máximo de su capacidad.

Para la siguiente solucion debemos definir una función de decisión de llenado como la siguiente:

$$L(t_{i}) = \left\{\begin{matrix} 1 \; \text{If } V(t_{i-1})-q_{i-1} < q_{i} & \\0 \; \text{In any other case
} & \end{matrix}\right.$$

b) $$V(t_{i}) = V(t_{i-1})-q_{i-1} +L(t_{i})(C´(R,t)-V(t_{i-1})-q_{i-1})$$
En dónde $C´(R,t)$ representa la capacidad que el tanque debería disponer para cumplir las ordenes siguientes sin la necesidad de llenar el recurso al maximo.

En cualquier caso, tomar a) o b) implicaria aplicar 3 hasta que $D$ represente el maximo de nuestras ordenes. Es decir, cuando todas nuestras ordenes han sido satisfechas.


