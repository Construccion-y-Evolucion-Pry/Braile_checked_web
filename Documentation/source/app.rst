Módulo app
==========

.. automodule:: app
   :members:
   :undoc-members:
   :show-inheritance:

Descripción General
-------------------

Este módulo contiene la aplicación Flask principal para el conversor de texto a Braille.
Implementa la lógica de conversión bidireccional (Texto ↔ Braille) y expone tanto una interfaz web como una API REST.

Funciones de Utilidad
---------------------

.. autofunction:: app.espejo_braille

Invierte los puntos de los caracteres Braille y el orden de la cadena para generar un formato "espejo".
Esto es fundamental para imprimir/perforar por el reverso de la hoja y que se lea correctamente por el frente.

**Proceso:**

1. Invierte cada carácter Braille horizontalmente (intercambia columnas de puntos 1↔4, 2↔5, 3↔6).
2. Invierte el orden de los caracteres (de derecha a izquierda).

.. autofunction:: app.texto_a_braille

La función ``texto_a_braille`` convierte texto en español (incluyendo mayúsculas, números, tildes y caracteres especiales) a símbolos Braille Unicode.

**Características:**

* Soporte completo para el alfabeto español (a-z, ñ)
* Manejo de vocales acentuadas (á, é, í, ó, ú, ü)
* Conversión de mayúsculas con prefijo ``⠨`` (puntos 4-6)
* Números con prefijo ``⠼`` (puntos 3-4-5-6)
* Signos de puntuación y operadores matemáticos

.. autofunction:: app.braille_a_texto

Convierte una cadena de caracteres Braille Unicode a texto legible. Interpreta los prefijos de número (``⠼``) y mayúscula (``⠨``) para decodificar correctamente el contexto.

**Lógica:**

* Mantiene un estado para saber si está en modo numérico.
* Aplica mayúsculas al siguiente carácter cuando encuentra el prefijo correspondiente.
* Traduce secuencias vacías o espacios.

Rutas de la Aplicación Web
---------------------------

.. autofunction:: app.index

Ruta principal que renderiza la interfaz web.

**URL:** ``/``

**Método:** ``GET``

.. autofunction:: app.contexto

Página informativa sobre el contexto del proyecto.

**URL:** ``/contexto``

**Método:** ``GET``

.. autofunction:: app.sobre_nosotros

Página con información sobre el equipo de desarrollo.

**URL:** ``/sobre-nosotros``

**Método:** ``GET``

API REST
--------

.. autofunction:: app.convertir

Endpoint para convertir **Texto → Braille**.

**URL:** ``/convertir``
**Método:** ``POST``
**Body:** ``{"texto": "..."}``

.. autofunction:: app.convertir_braille

Endpoint para convertir **Braille → Texto**.

**URL:** ``/convertir-braille``
**Método:** ``POST``
**Body:** ``{"braille": "..."}``

.. autofunction:: app.validar_braille

Valida si un carácter Braille introducido es válido según el modo actual (letra, número, especial). Útil para la entrada interactiva en la UI.

**URL:** ``/validar-braille``
**Método:** ``POST``
**Body:** ``{"braille": "...", "modo": "letra|numero|especial"}``

.. autofunction:: app.descargar_braille_word

Genera y descarga un documento de Microsoft Word (.docx) con el texto Braille formateado en espejo, listo para imprimir y perforar.

**URL:** ``/descargar-braille-word``
**Método:** ``POST``
**Body:** ``{"braille": "...", "texto": "..."}``

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

.. py:data:: BRAILLE_TO_TEXT
   :type: dict

   Diccionario inverso generado a partir de ``BRAILLE_MAP`` para la decodificación.

.. py:data:: BRAILLE_TO_NUMBER
   :type: dict

   Diccionario inverso para decodificar números Braille.
