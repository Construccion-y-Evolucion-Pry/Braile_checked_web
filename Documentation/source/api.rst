Referencia de la API
====================

Endpoints Disponibles
---------------------

GET /
^^^^^

Ruta principal que muestra la interfaz web.

**Método:** ``GET``

**URL:** ``/``

**Respuesta:** Página HTML con la interfaz del conversor

**Código de Estado:** 200 OK

**Ejemplo:**

.. code-block:: bash

    curl http://localhost:5000/

POST /convertir
^^^^^^^^^^^^^^^

Endpoint para convertir texto a Braille mediante API REST.

**Método:** ``POST``

**URL:** ``/convertir``

**Content-Type:** ``application/json``

Parámetros de Entrada
""""""""""""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Parámetro
     - Tipo
     - Requerido
     - Descripción
   * - texto
     - string
     - Sí
     - El texto que se desea convertir a Braille

**Ejemplo de Request:**

.. code-block:: json

    {
        "texto": "hola mundo"
    }

Respuestas
""""""""""

**Respuesta Exitosa (200 OK):**

.. code-block:: json

    {
        "texto_original": "hola mundo",
        "texto_braille": "⠓⠕⠇⠁⠀⠍⠥⠝⠙⠕"
    }

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Campo
     - Descripción
   * - texto_original
     - El texto original que se envió para convertir
   * - texto_braille
     - El texto convertido a símbolos Braille Unicode

**Respuesta de Error (400 Bad Request):**

.. code-block:: json

    {
        "error": "No se proporcionó texto"
    }

Se retorna cuando el campo ``texto`` está vacío o no se proporciona.

Ejemplos Completos
------------------

Usando cURL
^^^^^^^^^^^

Conversión básica:

.. code-block:: bash

    curl -X POST http://localhost:5000/convertir \
         -H "Content-Type: application/json" \
         -d '{"texto": "hola mundo"}'

Con texto más complejo:

.. code-block:: bash

    curl -X POST http://localhost:5000/convertir \
         -H "Content-Type: application/json" \
         -d '{"texto": "Python 3.14, increible!"}'

Usando Python (requests)
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests
    import json

    def convertir_a_braille(texto):
        """Convierte texto a Braille usando la API."""
        url = "http://localhost:5000/convertir"
        headers = {"Content-Type": "application/json"}
        data = {"texto": texto}
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            return result['texto_braille']
        else:
            error = response.json()
            raise Exception(f"Error: {error.get('error', 'Unknown error')}")

    # Uso
    try:
        braille = convertir_a_braille("hola mundo")
        print(f"Resultado en Braille: {braille}")
    except Exception as e:
        print(e)

Usando JavaScript (fetch)
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

    async function convertirABraille(texto) {
        const url = 'http://localhost:5000/convertir';
        
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ texto: texto })
            });
            
            if (response.ok) {
                const data = await response.json();
                return data.texto_braille;
            } else {
                const error = await response.json();
                throw new Error(error.error);
            }
        } catch (error) {
            console.error('Error al convertir:', error);
            throw error;
        }
    }

    // Uso
    convertirABraille('hola mundo')
        .then(braille => console.log('Braille:', braille))
        .catch(error => console.error('Error:', error));

Limitaciones y Consideraciones
-------------------------------

Caracteres Soportados
^^^^^^^^^^^^^^^^^^^^^

El conversor actualmente soporta:

* Letras del alfabeto inglés (a-z)
* Números (0-9)
* Espacios
* Signos de puntuación limitados: ``.``, ``,``, ``;``, ``:``, ``!``, ``?``, ``-``, ``(``, ``)``

Caracteres No Soportados
^^^^^^^^^^^^^^^^^^^^^^^^^

Los caracteres que no estén en el mapa de conversión se mantendrán tal como están 
en el texto original. Esto incluye:

* Caracteres acentuados (á, é, í, ó, ú)
* Caracteres especiales no incluidos
* Emojis
* Caracteres de otros idiomas

Manejo de Mayúsculas
^^^^^^^^^^^^^^^^^^^^^

La aplicación convierte todo el texto a minúsculas antes de procesarlo. 
No se preserva la distinción entre mayúsculas y minúsculas en la conversión actual.

Límites de Tamaño
^^^^^^^^^^^^^^^^^

No hay un límite estricto de tamaño para el texto de entrada, pero se recomienda 
no enviar textos excesivamente largos para mantener un rendimiento óptimo.

CORS
^^^^

La aplicación está configurada para desarrollo local. Si necesitas acceder a la API 
desde un dominio diferente, deberás configurar CORS (Cross-Origin Resource Sharing).
