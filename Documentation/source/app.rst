Módulo app
==========

.. automodule:: app
   :members:
   :undoc-members:
   :show-inheritance:

Descripción General
-------------------

Este módulo contiene la aplicación Flask principal para el conversor de texto a Braille.
Implementa la lógica de conversión y expone tanto una interfaz web como una API REST.

Función Principal de Conversión
---------------------------------

.. autofunction:: app.texto_a_braille

La función ``texto_a_braille`` es el núcleo del sistema. Convierte texto en español
(incluyendo mayúsculas, números, tildes y caracteres especiales) a símbolos Braille Unicode.

**Características:**

* Soporte completo para el alfabeto español (a-z, ñ)
* Manejo de vocales acentuadas (á, é, í, ó, ú, ü)
* Conversión de mayúsculas con prefijo ``⠨`` (puntos 4-6)
* Números con prefijo ``⠼`` (puntos 3-4-5-6)
* Números decimales (con punto o coma)
* Signos de puntuación y operadores matemáticos
* Preservación de saltos de línea

**Ejemplo de uso:**

.. code-block:: python

    >>> texto_a_braille("Hola")
    '⠨⠓⠕⠇⠁'
    
    >>> texto_a_braille("año 2024")
    '⠁⠻⠕⠀⠼⠃⠚⠃⠙'
    
    >>> texto_a_braille("precio: 19.99")
    '⠏⠗⠑⠉⠊⠕⠒⠀⠼⠁⠊⠄⠊⠊'

Rutas de la Aplicación Web
---------------------------

.. autofunction:: app.index

Ruta principal que renderiza la interfaz web del conversor.

**URL:** ``/``

**Método:** ``GET``

**Retorna:** Plantilla HTML con la interfaz de usuario

.. autofunction:: app.contexto

Página informativa sobre el contexto del proyecto.

**URL:** ``/contexto``

**Método:** ``GET``

**Retorna:** Plantilla HTML con información contextual

.. autofunction:: app.sobre_nosotros

Página con información sobre el equipo de desarrollo.

**URL:** ``/sobre-nosotros``

**Método:** ``GET``

**Retorna:** Plantilla HTML con información del equipo

API REST
--------

.. autofunction:: app.convertir

Endpoint REST para convertir texto a Braille mediante peticiones POST.

**URL:** ``/convertir``

**Método:** ``POST``

**Content-Type:** ``application/json``

**Request Body:**

.. code-block:: json

    {
        "texto": "hola mundo"
    }

**Response (200 OK):**

.. code-block:: json

    {
        "texto_original": "hola mundo",
        "texto_braille": "⠓⠕⠇⠁⠀⠍⠥⠝⠙⠕"
    }

**Response (400 Bad Request):**

.. code-block:: json

    {
        "error": "No se proporcionó texto"
    }

Variables Globales y Constantes
--------------------------------

.. py:data:: BRAILLE_MAP
   :type: dict

   Diccionario de mapeo de caracteres a símbolos Braille Unicode.
   
   Incluye:
   
   * Alfabeto completo (a-z, w)
   * Letra ñ
   * Vocales acentuadas (á, é, í, ó, ú, ü)
   * Espacios
   * Signos de puntuación (. , ; : ! ¡ ? ¿ - ( ))
   * Operadores matemáticos (+ * = /)
   * Saltos de línea

.. py:data:: BRAILLE_NUMBERS
   :type: dict

   Diccionario de mapeo de dígitos (0-9) a símbolos Braille.
   
   En Braille español, los números usan las mismas formas que las primeras
   10 letras (a-j) pero precedidos del signo de número ``⠼``.

.. py:data:: SIGNO_MAYUSCULA
   :type: str
   :value: '⠨'

   Prefijo para indicar mayúsculas (puntos 4-6).
   Se coloca antes de cada letra mayúscula.

.. py:data:: SIGNO_NUMERO
   :type: str
   :value: '⠼'

   Prefijo para indicar números (puntos 3-4-5-6).
   Se coloca al inicio de cada secuencia numérica.

Detalles de Implementación
---------------------------

**Algoritmo de Conversión:**

1. Recorre el texto carácter por carácter
2. Detecta secuencias numéricas y las agrupa
3. Agrega prefijos de mayúscula cuando corresponde
4. Maneja puntos y comas dentro de números (decimales)
5. Mapea caracteres según ``BRAILLE_MAP``
6. Preserva caracteres desconocidos sin cambios

**Manejo de Números:**

Los números se procesan en bloques. El prefijo ``⠼`` se agrega una sola vez
al inicio de cada secuencia numérica, no antes de cada dígito.

Ejemplo: ``"123"`` → ``"⠼⠁⠃⠉"`` (no ``"⠼⠁⠼⠃⠼⠉"``)

**Manejo de Mayúsculas:**

Cada letra mayúscula recibe su propio prefijo ``⠨``.

Ejemplo: ``"HOLA"`` → ``"⠨⠓⠨⠕⠨⠇⠨⠁"``
