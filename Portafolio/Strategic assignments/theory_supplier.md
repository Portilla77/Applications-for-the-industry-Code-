English:

In the industry, we are aware of the significant challenge involved in fulfilling our customers' requirements on time. A recurrent issue is determining, from a set of suppliers evaluated across multiple criteria (price, quality, delivery time, among others), which one is the most suitable to optimally satisfy our demand. In other words, being able to define an ordering or sequence $P_{1},P_{2},...,P_{n}$ such that $P_{1}$ is the priority supplier we should resort to the most in comparison to $P_{2}$, and $P_{2}$ has priority over $P_{3}$, and so on.

The following model not only allows identifying the most convenient supplier but also facilitates accurately determining the exact amount that we should request from each one, respecting the established order. Therefore, if we choose price, quality, and time, we can ensure not only lower acquisition costs and time but also the quality of the material acquired, thus optimizing our entire supply chain to effectively respond to market needs.

Let $P_{1},P_{2},...,P_{n}$ be the available suppliers, and suppose we can measure the following factors $x_{1},x_{2},...,x_{m}$.. If each $x_{i}$ is associated with $P_{i}$, then $P_{i}(x_{j}) = k_{ij}$
We consider normalization (unless there are restrictions due to some preprocessing and the variation between factors is significant) for $x_{i}$ as:

a)
$$V_{x_{n}} = \frac{v_{x_{j}} - v_{min_{x_{i}}}}{v_{max_{x_{i,j}}} - v_{min_{x_{i,j}}}}$$

We define $w_{i}$ as the weight of each factor $x_{i}$, then:

b)
$$\sum_{e=1}^{m}w_{e}=1$$

Finally, we obtain the sequence of suppliers whose ordered sequence indicates the suppliers to consider according to the values of $x_{i}$ by the following equation:

c) 
$$S_{N_{x_{i}}} = (w_{e})(V_{x_{i}})$$

By denoting the weighted sum of each value, we get a sequence of suppliers. The ordered sequence indicates the suppliers to consider according to the $x_{i}$ values entered.
This approach helps reduce the risk of production loss due to insufficient materials or products to meet demand, as it spreads the demand across different suppliers. Additionally, we propose the following proportionality to determine the percentage associated with each supplier, respecting the sequence mentioned earlier. That is, the amount to request from each supplier according to the sequence obtained in c) is:

d)
$$\frac{S_{N_{x_{i}}}}{\sum_{i=1}^{e}(S_{N_{x_{i}}})}$$

Lastly, it seems important to cover one more aspect. While the above solves the problem of whom and how much to ask, we will next consider one more premise. That is, if the supplier wishes to establish a limit on the materials requested, we can add one more restriction to the model as follows:

Suppose that $P(S_{1}) > P(S_{2}), ..., > P(S_{n})$ is the sequence obtained after applying the previous model.

Let $C_{1} > C_{2}, ..., > C_{n}$ be the capacity associated with each $P_{i}$. Then, the minimum value between the two previous sequences is:

e)
$$\sum_{i=1}^{n}\min(P(S_{i}),C_{i}) = \min(P(S_{1}),C_{1}), \min(P(S_{2}),C_{2}), ..., \min(P(S_{n}),C_{n})$$

With this, we obtain the maximum number of items requested per supplier, considering their maximum capacity and the analysis of the proposed suppliers.

As $P({S}_{1})', P({S}_{2})', ..., P({S}_{m})'$ is the sequence obtained after e), and $D$ is the demand to be met by the suppliers, we denote the remainder obtained from adding up the amount to request from all suppliers according to the **PA** and the total demand to request ($D$), having:

f)
$$R_{t} = D - \sum_{i=1}^{n}\min(P(S_{i}),C_{i})$$

We consider an available supplier, defined as one that meets the following criterion:

g)

${S}'_{i}$ is available $\Leftrightarrow$ $C_{i}-P({S})'_{i}\geq 0$

$$\Rightarrow (S'_{i} + \frac{R_{t}}{\sum_{i=1}^{m}S_{i}})$$

Therefore, $S'_{i} + ... + S'_{j} = D$, thus meeting the demand to be requested from the set of suppliers. This respects the order proposed by **PA** as we are adding equal quantities for all available suppliers.
____
Español:

En la industria conocemos el gran problema que conlleva cumplir a tiempo los requisitos de nuestros clientes de manera oportuna. Un problema recurrente es determinar, de un conjunto de proveedores evaluados bajo múltiples criterios (precio, calidad, tiempo de entrega, entre otros), cuál es el más adecuado para satisfacer nuestra demanda de forma óptima. Es decir, poder definir un ordenamiento o secuencia $P_{1},P_{2},...,P_{n}$ tal que $P_{1}$ sea el proveedor prioritario al que debemos recurrir en mayor medida en comparación con $P_{2}$ ,luego $P_{2}$ tenga prioridad sobre $P_{3}$ y así sucesivamente.

El siguiente modelo no solo permite identificar al proveedor más conveniente sino que también facilita determinar con precisión la cantidad exacta que debemos solicitar a cada uno, respetando el orden establecido. Por tanto,si escojemos precio,calidad y tiempo podemos asegurar no solo costos menores en la adquisicion y tiempo, sino también la calidad del material adquirido, optimizando así toda nuestra cadena de suministro para responder de manera efectiva a las necesidades del mercado.

Sea $P_{1},P_{2},...,P_{n}$ los proveedores disponibles, y supongamos que podemos medir los siguientes factores $x_{1},x_{2},...,x_{m}$. Si cada $x_{i}$ es asociado a $P_{i}$ , entonces $P_{i}(x_{j}) = k_{ij}$
Consideremos la normalización (Sino existen restricciones por algun preproceso y la variación entre los factores es significativa) para $x_{i}$ como:

a)
$$V_{x_{n}} =\frac{v_{x_{j}}-v_{min_{x_{i}}}}{v_{max_{x_{i,j}}}-v_{min_{x_{i,j}}}}$$

Definimos $w_{i}$ como el peso de cada factor $x_{i}$,entonces:

b)
$$\sum_{e=1}^{m}w_{e}=1$$

Finalmente obtenemos la secuencia de proveedores cuya secuencia ordenada indica los proveedores a considerar según los valores de $x_{i}$ mediante la siguiente ecuación:

c) 
$$S_{N_{x_{i}}}= (w_{e})(V_{x_{i}})$$

Al denotar la suma ponderada de cada valor, obtenemos una secuencia de proveedores. La secuencia ordenada indica los proveedores a considerar de acuerdo con los valores $x_{i}$ introducidos.
Este enfoque ayuda a reducir el riesgo de pérdida de producción debido a materiales o productos insuficientes para satisfacer la demanda, ya que distribuye la demanda entre diferentes proveedores. Adicionalmente, proponemos la siguiente proporcionalidad para determinar el porcentaje asociado a cada proveedor, respetando la secuencia antes mencionada. Es decir, la cantidad a solicitar por cada proveedor según la secuencia obtenida en c) es:
d)
$$\frac{S_{N_{x_{i}}}}{\sum_{i=1}^{e}(S_{N_{x_{i}}})}$$

Por ultimo, me parece importante abarcar un aspecto más. Si bien, lo anterior nos soluciona el problema de a quién y cuanto pedir, enseguida consideraremos una premisa más. Esto es, si el proveedor desea establecer un limite de materiales solicitados, podemos agregar una restriccion más al modelo de la siguiente manera:

Supongamos que $P(S_{1})>P(S_{2}),...,>P(S_{n})$ es la  sequencia obtenida despues de aplicar el modelo anterior.

Sea $C_{1}>C_{2},...,>C_{n}$ la capacidad asociada a cada $P_{i}$. entonces, el minimo valor entre las dos secuencias anteriores es:

e)
$$\sum_{i=1}^{n}min(P(S_{i}),C_{i}) =min(P(S_{1}),C_{1}),min(P(S_{2}),C_{2}),...,min(P(S_{n}),C_{n})$$

Con lo anterior obtenemos el número máximo de artículos solicitados por proveedor, considerando su capacidad máxima y el análisis de los proveedores propuestos.

Como $P({S}_{1})', P({S}_{2})', ..., P({S}_{m})'$ es la secuencia obtenida despues de e), y $D$ es la demanda a stisfacer por los proveedores, denotamos el resto obtenido de sumar la cantidad a solicitar de todos los proveedores según el **PA** y la demanda total a solicitar ($D$), teniendo:

f)
$$R_{t}= D - \sum_{i=1}^{n}min(P(S_{i}),C_{i})$$

Consideremos un proveedor disponible, definido como aquel que cumple el siguiente criterio:

g)

${S}'_{i}$ es disponible $\Leftrightarrow$ $C_{i}-P({S})'_{i}\geq 0$

$$\Rightarrow ({S}'_{i}+\frac{R_{t}}{\sum_{i=1}^{m}S_{i}})$$

Por lo tanto, ${S}'{i}+...+{S}'{j} = D$, satisfaciendo así la demanda a solicitar al conjunto de proveedores. Esto respeta el orden propuesto por **PA** ya que estamos sumando cantidades equitativas para todos los proveedores disponibles.

