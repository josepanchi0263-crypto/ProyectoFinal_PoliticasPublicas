# Evaluación del Impacto del Bono de Desarrollo Humano (BDH) sobre la pobreza en Ecuador: Propensity Score Matching (PSM)

## 1. Introducción

El Bono de Desarrollo Humano (BDH) es una política de transferencia condicionada que busca reducir la pobreza y mejorar el bienestar de los hogares en situación de vulnerabilidad en Ecuador. Este documento propone una estrategia metodológica basada en Propensity Score Matching (PSM) para evaluar el impacto del BDH sobre medidas de pobreza utilizando datos de la ENEMDU y otros indicadores socioeconómicos relevantes.

## 2. Justificación del análisis

### 2.1 Contexto institucional y datos

El análisis se sustenta en las encuestas de hogares de la ENEMDU, que proveen información detallada sobre ingresos, gasto, empleo, educación y condiciones de vida. El BDH puede analizarse comparando beneficiarios y no beneficiarios con características observables similares.

### 2.2 Sesgo de selección y necesidad de PSM

La selección de beneficiarios del MIES a través del Registro Social se realiza con criterios de vulnerabilidad socioeconómica que generan un sesgo de selección no aleatorio. En este contexto, las evaluaciones deben emplear metodologías cuasi-experimentales como PSM para mitigar el sesgo de variables omitidas y para construir un contrafactual confiable (Banco Mundial, 2016).

### 2.3 Impacto en capital humano y alimentación

La evidencia nacional sugiere que el gasto del BDH se orienta prioritariamente a mitigar brechas de pobreza rural, reducir la desnutrición y disminuir la deserción escolar. Estudios de CEPAL en Ecuador destacan que los programas de transferencias condicionadas contribuyen a fortalecer el capital humano y los resultados en alimentación de hogares vulnerables (CEPAL, 2017).

### 2.4 Índice de vulnerabilidad y pobreza multidimensional

Para caracterizar adecuadamente a la población objetivo, se recomienda incorporar indicadores como:
- Índice de Vulnerabilidad económica y social.
- Variables de acceso a servicios básicos (agua, electricidad, saneamiento).
- Características del jefe de hogar: nivel educativo, ocupación, género.
- Composición del hogar: número de miembros, edad, presencia de niños.

La inclusión de estas covariables permite controlar por factores que influyen en la probabilidad de recibir el BDH y en el resultado de pobreza.

## 3. Marco teórico y formulación econométrica

### 3.1 Propensity Score Matching

PSM es un método que busca replicar condiciones de un experimento controlado mediante el emparejamiento de unidades tratadas y de control que tienen probabilidades similares de recibir el tratamiento. El puntaje de propensión se define como:

\[ p(X_i) = P(T_i = 1 \mid X_i) \]

donde:
- \(T_i\) es una variable indicadora del tratamiento (ser beneficiario del BDH).
- \(X_i\) es el vector de covariables observadas.

El uso de PSM en evaluaciones del BDH en Ecuador está respaldado por precedentes metodológicos de la Universidad de Cuenca y FLACSO, que emplean algoritmos nearest neighbor y modelos logit sobre datos transversales de la ENEMDU para estimar efectos causales en contextos de selección no aleatoria.

### 3.2 Modelo logit de propensión

La estimación del propensity score se realiza mediante una regresión logística del tratamiento sobre las covariables observadas:

\[ \text{logit}(P(T_i=1 \mid X_i)) = \alpha + X_i'\beta + \varepsilon_i \]

Donde la función logit se define como:

\[ \text{logit}(p) = \ln\left(\frac{p}{1-p}\right) \]

La probabilidad condicional para cada unidad se obtiene a partir de:

\[ p(X_i) = \frac{\exp(\alpha + X_i'\beta)}{1 + \exp(\alpha + X_i'\beta)} \]

En el contexto del BDH, un vector típico de covariables \(X_i\) puede incluir:

- `Jefe_Mujer`: indicador de género del jefe de hogar.
- `Anios_Escolaridad`: años de educación del jefe de hogar.
- `Num_Hijos`: número de menores en el hogar.
- `Area_Rural`: indicador de residencia rural.
- `Puntaje_Registro_Social`: puntaje socioeconómico de elegibilidad.

La estimación de \(\alpha\) y \(\beta\) se realiza por máxima verosimilitud. El algoritmo de optimización puede ser iterativo, por ejemplo usando iteratively reweighted least squares (IRLS) o descenso de gradiente, para encontrar los parámetros que maximizan la probabilidad de los tratamientos observados.

### 3.3 Especificación econométrica del logit

La fórmula operacional que se utiliza en el modelo logit es:

\[ \ln\left(\frac{P(T_i=1\mid X_i)}{1-P(T_i=1\mid X_i)}\right) = \beta_0 + \beta_1 Jefe\_Mujer_i + \beta_2 Anios\_Escolaridad_i + \beta_3 Num\_Hijos_i + \beta_4 Area\_Rural_i + \beta_5 Puntaje\_Registro\_Social_i \]

Los coeficientes estimados \(\beta_j\) capturan el efecto marginal de cada covariable sobre la probabilidad de recibir el BDH. Una vez estimados, los puntajes de propensión se usan como variable de emparejamiento entre tratados y controles.

### 3.4 Soporte común y emparejamiento

El soporte común o overlap es el rango de valores del puntaje de propensión en el que existen tanto unidades tratadas como controles. Formalmente, el soporte común se define como:

\[ \{x: 0 < P(T=1\mid X=x) < 1\} \]

Para el análisis, se procede en tres pasos:

1. Estimar el puntaje de propensión para cada observación.
2. Identificar el rango compartido de puntajes entre grupos tratados y de control.
3. Excluir observaciones fuera del soporte común para evitar extrapolaciones no sustentadas.

### 3.5 Algoritmo de emparejamiento: Nearest Neighbor

El emparejamiento nearest neighbor selecciona para cada unidad tratada el control más cercano en términos absolutos de puntaje de propensión. El algoritmo básico es:

1. Calcular el puntaje de propensión \(p(X_i)\) para todas las unidades.
2. Dividir los datos en tratados \((T=1)\) y controles \((T=0)\).
3. Para cada tratado, buscar el control \(j\) que minimice \(|p(X_i) - p(X_j)|\).
4. Asignar el control seleccionado como contrafactual del tratado.

El resultado es un conjunto emparejado que preserva la comparabilidad observable. Si se emplea matching con reemplazo, un control puede aparecer como contrafactual de múltiples tratados; si se usa sin reemplazo, cada control se asigna una sola vez.

### 3.6 Supuesto de soporte común en la práctica

Para validar el soporte común se recomienda graficar la densidad de los puntajes de propensión por grupo y comparar los rangos extremos. Un soporte común estrecho o inexistente indica que los resultados pueden estar basados en extrapolación y deben interpretarse con cautela.

### 3.7 Balance de covariables

Después del emparejamiento, se deben comparar las medias y las diferencias estandarizadas de las covariables entre tratados y controles emparejados. El objetivo es reducir las diferencias observadas y aproximar la condición de equilibrio del experimento.

### 3.8 Cálculo del ATT

El efecto promedio del tratamiento sobre los tratados (ATT) se calcula como:

\[ ATT = \frac{1}{N_1} \sum_{i:T_i=1} \left(Y_i - Y_{j(i)}\right) \]

Donde \(Y_i\) es el resultado observado del tratado y \(Y_{j(i)}\) es el resultado del control emparejado.

## 4. Supuestos metodológicos

Para que PSM sea válido, se deben cumplir dos supuestos clave:

1. **Independencia condicional (unconfoundedness)**: Condicionado a \(X\), el tratamiento es independiente del resultado potencial. Esto implica que todas las variables que influyen simultáneamente en la participación y en el resultado deben estar observadas y correctamente incluidas en el modelo.

2. **Soporte común**: Existe superposición en las probabilidades de tratamiento entre grupos. Si no hay solapamiento, el emparejamiento no es informativo.

### 4.1 Exclusión de variables post-tratamiento

Es fundamental que el modelo de propensión incluya únicamente variables anteriores al tratamiento. No deben incorporarse variables que puedan verse afectadas por la recepción del BDH, como gasto educativo o consumo actual del hogar tras recibir el apoyo.

## 5. Estrategia de variables

### 5.1 Variable de tratamiento

- `tratamiento_bd_h`: indicador binario de beneficiario/a del BDH.

### 5.2 Variables de resultado

- `pobreza_ingresos`: indicador de pobreza monetaria.
- `ingreso_per_capita`: ingreso del hogar por persona.
- `pobreza_multidimensional`: indicador alterno si está disponible.

### 5.3 Covariables de emparejamiento

- edad del jefe de hogar
- nivel educativo del jefe de hogar
- género del jefe de hogar
- tamaño del hogar
- número de menores de edad
- acceso a servicios básicos
- región y área urbana/rural
- condición de empleo

## 6. Flujo de análisis en Python

1. Cargar datos de ENEMDU.
2. Definir tratamiento, resultado y covariables.
3. Estimar el modelo logit para el puntaje de propensión.
4. Evaluar soporte común y graficar la densidad de los puntajes para tratados y controles.
5. Emparejar unidades con nearest neighbor y caliper si es necesario.
6. Calcular ATT y estimar efectos sobre pobreza.
7. Verificar balance de covariables antes y después del emparejamiento.
8. Realizar análisis de sensibilidad y robustez.

## 7. Diagnóstico y validación

### 7.1 Balance de covariables

El análisis debe incluir tablas de balance que comparen medias y diferencias estandarizadas antes y después del emparejamiento. El objetivo es reducir diferencias entre los grupos tratados y de control.

### 7.2 Validación del modelo

Se recomienda examinar las siguientes pruebas:
- distribución de puntajes de propensión por grupo
- soporte común gráfico
- resultados de balance estándar
- número de emparejamientos perdidos

## 8. Próximos pasos

1. Ejecutar el flujo inicial con datos reales de ENEMDU.
2. Ajustar covariables según disponibilidad y medición.
3. Documentar resultados de ATT y evaluar su significancia.
4. Comparar con métodos alternativos (DID, RDD) según la calidad de los datos.

## 9. Referencias

- Banco Mundial. (2016). *The growth platform: better jobs for a strong economy* [Documento técnico]. https://documents1.worldbank.org/curated/en/693841467993509355/pdf/104300-SPANISH-WP-P151521-PUBLIC.pdf
- CEPAL. (2017). *Informe nacional: políticas sociales y pobreza en Ecuador* [Informe]. https://www.cepal.org/sites/default/files/static/files/ecuador_-_informe_nacional_2.pdf
- Universidad de Cuenca / FLACSO. (2019). *Estudio de titulación: evaluación del efecto del BDH utilizando ENEMDU* [Trabajo de titulación]. https://dspace-test.ucuenca.edu.ec/bitstream/123456789/5299/1/Trabajo-de-Titulación.pdf
- Rosenbaum, P. R., & Rubin, D. B. (1983). The central role of the propensity score in observational studies for causal effects.
- Becker, S. O., & Ichino, A. (2002). Estimation of average treatment effects based on propensity scores.
- ENEMDU, Encuesta Nacional de Empleo, Desempleo y Subempleo, Ecuador.
