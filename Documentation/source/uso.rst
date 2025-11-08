Uso de la Aplicación
====================

Iniciar el Servidor
-------------------

Para iniciar la aplicación, ejecuta::

    python app.py

O si estás usando un entorno virtual en Windows::

    ".venv/Scripts/python.exe" app.py

La aplicación se iniciará en modo desarrollo y podrás acceder a ella en:

* http://localhost:5000
* http://127.0.0.1:5000

Interfaz Web
------------

Conversión de Texto
^^^^^^^^^^^^^^^^^^^

1. Abre tu navegador y ve a http://localhost:5000
2. En el área de texto "Texto Original", escribe el texto que deseas convertir
3. Haz clic en el botón "Convertir a Braille ⚡"
4. El texto en Braille aparecerá en el panel derecho "Texto en Braille"

Copiar Resultado
^^^^^^^^^^^^^^^^

Una vez que el texto ha sido convertido:

1. Aparecerá un botón "📋 Copiar Braille"
2. Haz clic en él para copiar el texto en Braille al portapapeles
3. Podrás pegar el resultado en cualquier otra aplicación

Atajos de Teclado
^^^^^^^^^^^^^^^^^

* **Ctrl + Enter** (mientras escribes en el área de texto): Convierte automáticamente el texto sin hacer clic en el botón

Ejemplos de Uso
---------------

Ejemplo 1: Texto Simple
^^^^^^^^^^^^^^^^^^^^^^^

**Entrada:**::

    hola mundo

**Salida:**::

    ⠓⠕⠇⠁⠀⠍⠥⠝⠙⠕

Ejemplo 2: Texto con Números
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Entrada:**::

    hola 123

**Salida:**::

    ⠓⠕⠇⠁⠀⠁⠃⠉

Ejemplo 3: Texto con Puntuación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Entrada:**::

    hola, ¿como estas?

**Salida:**::

    ⠓⠕⠇⠁⠂⠀⠦⠉⠕⠍⠕⠀⠑⠎⠞⠁⠎⠦

Uso Programático (API)
-----------------------

La aplicación también expone un endpoint REST para conversión programática.

Endpoint de Conversión
^^^^^^^^^^^^^^^^^^^^^^^

**URL:** ``POST /convertir``

**Headers:**

.. code-block:: http

    Content-Type: application/json

**Body (JSON):**

.. code-block:: json

    {
        "texto": "hola mundo"
    }

**Respuesta Exitosa (200 OK):**

.. code-block:: json

    {
        "texto_original": "hola mundo",
        "texto_braille": "⠓⠕⠇⠁⠀⠍⠥⠝⠙⠕"
    }

**Respuesta de Error (400 Bad Request):**

.. code-block:: json

    {
        "error": "No se proporcionó texto"
    }

Ejemplo con cURL
^^^^^^^^^^^^^^^^

.. code-block:: bash

    curl -X POST http://localhost:5000/convertir \
         -H "Content-Type: application/json" \
         -d '{"texto": "hola mundo"}'

Ejemplo con Python
^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    url = "http://localhost:5000/convertir"
    data = {"texto": "hola mundo"}
    
    response = requests.post(url, json=data)
    result = response.json()
    
    print(f"Original: {result['texto_original']}")
    print(f"Braille: {result['texto_braille']}")

Ejemplo con JavaScript
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

    fetch('http://localhost:5000/convertir', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ texto: 'hola mundo' })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Original:', data.texto_original);
        console.log('Braille:', data.texto_braille);
    });

Detener el Servidor
-------------------

Para detener el servidor, presiona ``Ctrl + C`` en la terminal donde está ejecutándose.
