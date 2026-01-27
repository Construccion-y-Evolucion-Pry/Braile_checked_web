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

La interfaz cuenta ahora con dos pestañas principales: **Texto → Braille** (por defecto) y **Braille → Texto**.

Pestaña: Texto → Braille
^^^^^^^^^^^^^^^^^^^^^^^^

1. Escribe o pega el texto que deseas convertir en el área de entrada.
2. **La conversión es automática e instantánea**.
3. El texto en Braille aparece inmediatamente en la sección de salida con una animación de cursor.

Pestaña: Braille → Texto
^^^^^^^^^^^^^^^^^^^^^^^^

Esta nueva funcionalidad permite escribir en Braille y ver la traducción en texto normal.

**Métodos de Entrada:**

1. **Casillas Interactivas (Virtual Braille):**
   Haz clic en los 6 puntos (check-boxes) para formar un carácter y presiona "Enter" o usa los controles.

2. **Teclado Numérico (Numpad Mapping):**
   Puedes usar tu teclado físico para simular un teclado Braille:
   
   * **7:** Punto 1 (Arriba Izq)
   * **8:** Punto 4 (Arriba Der)
   * **4:** Punto 2 (Medio Izq)
   * **5:** Punto 5 (Medio Der)
   * **1:** Punto 3 (Abajo Izq)
   * **2:** Punto 6 (Abajo Der)
   * **Enter:** Confirmar carácter

3. **Modos de Escritura:**
   
   * **Modo Letra (Tecla 9):** Para escribir alfabeto estándar.
   * **Modo Número (Tecla 6):** Activa el modo numérico (agrega prefijo numérico automáticamente).
   * **Modo Carácter (Tecla 3):** Para símbolos especiales y puntuación.

Esta sección incluye validación en tiempo real para asegurar que el carácter formado existe en el diccionario.

Funcionalidades Adicionales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

💾 **Descargar Word Braille (Espejo)**
""""""""""""""""""""""""""""""""""""""

Esta función es vital para la impresión manual (punzón y regleta) o máquinas Perkins.

1. Ve a la sección de descargas.
2. Haz clic en "Descargar Word Braille (Espejo)".
3. Se generará un documento ``.docx`` con:
   
   * Instrucciones de perforado.
   * El texto Braille invertido horizontalmente (espejo) y escrito de derecha a izquierda.
   * Una página de referencia con el texto original.

**¿Por qué espejo?** Al perforar el papel por el reverso, el relieve se forma hacia el frente. Por tanto, se debe escribir al revés para que se lea al derecho.

📋 **Copiar al Portapapeles**
"""""""""""""""""""""""""""""

El botón "Copiar" (en la pestaña Texto → Braille) permite llevar el resultado a otras aplicaciones rápidamente.

🖼️ **Exportar como Imagen PNG**
"""""""""""""""""""""""""""""""
Genera una imagen compartible con diseño profesional que incluye el texto original y su traducción.

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
