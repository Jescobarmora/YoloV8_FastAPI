# Detección de Objetos con YOLOv8 y FastAPI

Este repositorio contiene un Web Service desarrollado en **FastAPI** que utiliza el modelo preentrenado **YOLOv8** para la detección de objetos en imágenes. El servicio recibe una imagen, detecta los objetos presentes, y devuelve tanto los detalles de las detecciones (clase, confianza y coordenadas) como la imagen con las detecciones visualizadas.

Además, el repositorio incluye un **Jupyter Notebook** que permite enviar imágenes al servicio, procesar la respuesta y visualizar las detecciones.

## Características

- **YOLOv8**: Utiliza el modelo YOLOv8 para detección de objetos en imágenes.
- **FastAPI**: El servicio está construido con FastAPI, lo que garantiza un rendimiento rápido y eficiente.
- **Respuesta en JSON**: La API devuelve las detecciones en formato JSON, que incluye:
  - Clase del objeto detectado.
  - Confianza de la detección.
  - Coordenadas de los cuadros delimitadores.
- **Jupyter Notebook**: Incluye un notebook para realizar pruebas automáticas enviando imágenes al servicio y visualizando los resultados.
