# 🚀 API Data Extractor (JSON a CSV)

Pequeño script en Python diseñado para **extraer datos de una API autenticada** y guardarlos automáticamente en un archivo **CSV**. Es ideal para tareas rápidas de migración de datos, *reporting* o análisis offline.

## ✨ Características

* **Autenticación Sencilla:** Configurado para usar una clave API (Header `Authorization: Bearer`).
* **Parseo de JSON:** Utiliza la librería `requests` de Python para manejar la respuesta JSON.
* **Guardado en CSV:** Convierte automáticamente la lista de diccionarios JSON en un archivo CSV limpio, usando las claves como encabezados de columna.
* **Manejo Básico de Errores:** Incluye verificación de errores HTTP y problemas de conexión.

## 🛠️ Requisitos

Asegúrate de tener **Python 3.x** instalado.

Para ejecutar el script, necesitarás la librería `requests`:

```bash
pip install requests
