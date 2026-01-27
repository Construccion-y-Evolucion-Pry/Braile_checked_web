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

La interfaz web de BraiLator ofrece conversión en tiempo real:

1. Abre tu navegador y ve a http://localhost:5000
2. Escribe o pega el texto que deseas convertir en el área de entrada
3. **La conversión es automática e instantánea** - no necesitas hacer clic en ningún botón
4. El texto en Braille aparece inmediatamente en la sección "Resultado en Braille"

.. note::
   La conversión ocurre mientras escribes. Cada carácter se traduce instantáneamente.

Funcionalidades Adicionales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

📋 **Copiar al Portapapeles**

El botón "📋 Copiar" copia el texto en Braille al portapapeles:

1. Una vez que tienes texto convertido, haz clic en "📋 Copiar"
2. El botón cambiará a "✅ ¡Copiado!" con fondo verde durante 2 segundos
3. Ahora puedes pegar (Ctrl+V) el texto Braille en cualquier aplicación

**Validación:**
   Si no hay texto, mostrará la alerta: "⚠️ No hay texto en Braille para copiar"

🖼️ **Exportar como Imagen PNG**

El botón "🖼️ Exportar PNG" genera una imagen profesional:

1. Con texto ya convertido, haz clic en "🖼️ Exportar PNG"
2. Verás "⏳ Generando..." mientras se procesa
3. Se descarga automáticamente: ``braille-traduccion-YYYY-MM-DD-HH-MM-SS.png``
4. El botón mostrará "✅ ¡Exportado!" brevemente

**Contenido de la imagen PNG:**

* Título: "Traducción a Braille"
* Texto original
* Traducción en Braille (fuente 32px)
* Footer: "Generado por BraiLator"
* Fondo blanco profesional

**Casos de uso:**

* Material educativo
* Señalética en Braille
* Presentaciones y documentación
* Compartir en redes sociales
* Impresión de referencias

**Validación:**
   Sin texto mostrará: "⚠️ No hay texto en Braille para exportar"

Navegación
^^^^^^^^^^

**Secciones disponibles:**

* **Inicio** (``/``): Conversor principal
* **Contexto** (``/contexto``): Información sobre Braille
* **Sobre Nosotros** (``/sobre-nosotros``): Equipo de desarrollo

Atajos de Teclado
^^^^^^^^^^^^^^^^^

* **Escritura continua**: La conversión es automática, simplemente escribe


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
