.. Conversor de Texto a Braille documentation master file, created by
   sphinx-quickstart on Sat Nov  8 09:36:47 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

================================
BraiLator - Conversor a Braille
================================

Bienvenido a la documentación de BraiLator
-------------------------------------------

**BraiLator** es una aplicación web desarrollada con Flask que permite convertir texto 
en español a símbolos Braille Unicode de manera rápida, precisa y accesible.

.. image:: https://img.shields.io/badge/python-3.7+-blue.svg
   :alt: Python 3.7+
   
.. image:: https://img.shields.io/badge/flask-3.0.0-green.svg
   :alt: Flask 3.0.0

Características Principales
----------------------------

✅ **Conversión en Tiempo Real**
   Traduce texto a Braille instantáneamente mientras escribes

✅ **Soporte Completo del Español**
   - Alfabeto completo (a-z) incluyendo ñ
   - Vocales acentuadas (á, é, í, ó, ú, ü)
   - Mayúsculas con prefijo correcto
   - Números y decimales

✅ **Interfaz Web Moderna**
   - Diseño responsivo (funciona en móviles, tablets y desktop)
   - Tema oscuro elegante
   - Conversión instantánea
   - Botones para copiar y exportar

✅ **Funcionalidades de Exportación**
   - 📋 Copiar al portapapeles con un clic
   - 🖼️ Exportar traducciones como imágenes PNG profesionales

✅ **API REST**
   Endpoint ``/convertir`` para integración con otras aplicaciones

✅ **Signos y Símbolos**
   Puntuación, operadores matemáticos y caracteres especiales

Inicio Rápido
--------------

**Instalación:**

.. code-block:: bash

   git clone https://github.com/Construccion-y-Evolucion-Pry/Braile_checked_web
   cd Braile_checked_web
   python -m venv .venv
   source .venv/Scripts/activate  # En Windows
   pip install -r requirements.txt

**Ejecutar:**

.. code-block:: bash

   python app.py

Luego abre http://localhost:5000 en tu navegador.

**Uso de la API:**

.. code-block:: python

   import requests

   response = requests.post('http://localhost:5000/convertir',
                           json={'texto': 'Hola mundo'})
   print(response.json()['texto_braille'])
   # Output: ⠨⠓⠕⠇⠁⠀⠍⠥⠝⠙⠕

Casos de Uso
------------

📚 **Educación**
   Material didáctico para enseñanza del sistema Braille

🏢 **Señalética**
   Generación de señales en Braille para edificios públicos

♿ **Accesibilidad**
   Conversión de documentos y contenido web

🔬 **Investigación**
   Herramienta para estudios sobre sistemas de escritura táctil

Contenido de la Documentación
------------------------------

.. toctree::
   :maxdepth: 3
   :caption: Guías de Usuario

   introduccion
   instalacion
   uso
   api

.. toctree::
   :maxdepth: 2
   :caption: Documentación Técnica

   app

.. toctree::
   :maxdepth: 1
   :caption: Recursos Adicionales

   Manual de Usuario <https://github.com/Construccion-y-Evolucion-Pry/Braile_checked_web>
   Reportar Issues <https://github.com/Construccion-y-Evolucion-Pry/Braile_checked_web/issues>

Tecnologías Utilizadas
-----------------------

**Backend:**
   - Python 3.14
   - Flask 3.0.0
   - Werkzeug 3.0.1

**Frontend:**
   - HTML5 semántico
   - CSS3 con diseño responsivo
   - JavaScript vanilla (ES6+)
   - html2canvas (exportación PNG)

**Documentación:**
   - Sphinx 8.2.3
   - Read the Docs Theme

Sobre el Proyecto
-----------------

**Proyecto:** Construcción y Evolución de Software

**Institución:** Escuela Politécnica Nacional

**Facultad:** Ingeniería de Sistemas

**Grupo:** 5

**Versión:** 1.0

**Fecha:** Noviembre 2025

Índices y Búsqueda
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

