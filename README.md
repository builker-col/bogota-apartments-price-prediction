# Prediccion de Precio de Venta de Apartamentos en Bogota

Este proyecto se enfoca en la predicción del precio de venta de apartamentos en Bogotá, Colombia, utilizando alrededor de 80,000 datos recopilados del proyecto ["**Bogotá Apartments**"](https://github.com/builker-col/bogota-apartments) de Builker. Estos datos fueron extraídos de Metrocuadrado y Habi mediante web scraping.

## Objetivo Principal:
El objetivo fundamental de este proyecto es desarrollar modelos predictivos precisos que puedan estimar el precio de venta de apartamentos en Bogotá por localidad, tomando en cuenta las particularidades de cada área, utilizando técnicas de aprendizaje automático.

## Alcance y Metodología:
Recopilación de Datos del Proyecto ["**Bogotá Apartments**"](https://github.com/builker-col/bogota-apartments) de Builker:
Los datos fueron recolectados mediante web scraping de Metrocuadrado y Habi, acumulando alrededor de 80,000 registros detallados sobre apartamentos en Bogotá. Estos datos se dividen por localidades.

* **Procesamiento y Limpieza de Datos:**
Tras la recolección, se realizó un exhaustivo proceso de limpieza y procesamiento de los datos para eliminar errores y valores atípicos, además de adaptarlos al formato requerido por los modelos de Machine Learning.

* **Modelado por Localidad:**
Se implementaron modelos de Machine Learning separados para cada localidad de Bogotá, como KNN y Regresión Lineal, considerando las particularidades y características únicas de cada área.

* **Entrenamiento y Evaluación por Localidad:**
Cada modelo fue entrenado con datos históricos específicos de cada localidad y se evaluó su rendimiento y precisión utilizando técnicas de validación cruzada y métricas de evaluación adecuadas a cada modelo y área.

* **Predicción de Precios de Venta por Localidad:**
Utilizando los modelos entrenados y validados por cada localidad, se realizaron predicciones de los precios de venta de apartamentos en Bogotá basados en las características específicas de cada área.

* **Creación de una API Interactiva:**
Se desarrollará una API que permita interactuar con los modelos entrenados, ofreciendo la posibilidad de realizar predicciones de precios de venta de apartamentos en Bogotá a través de una interfaz amigable y accesible.

## Valor y Aplicación:
Este proyecto busca proporcionar herramientas específicas para cada localidad a los interesados en el mercado inmobiliario de Bogotá, ofreciendo estimaciones precisas y contextualizadas del precio de venta de apartamentos en función de sus atributos y la ubicación específica.

## Resultados Esperados:
Se espera obtener modelos de predicción precisos y adaptados a cada localidad de Bogotá, lo que permitirá proporcionar estimaciones más informadas y precisas sobre los precios de venta de apartamentos en la ciudad, facilitando la toma de decisiones en transacciones inmobiliarias a nivel local.

Este proyecto representa un esfuerzo integral para aplicar técnicas avanzadas de Machine Learning en el contexto específico del mercado inmobiliario en Bogotá, ofreciendo modelos de predicción ajustados a las particularidades de cada área de la ciudad.

**Fuente de Datos:** [Bogotá Apartments](https://github.com/builker-col/bogota-apartments)

**Datos Chart:** [Bogotá Apartments Panel](https://builker-col.github.io/bogota-apartments/)