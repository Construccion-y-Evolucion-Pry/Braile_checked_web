Instalación
===========

Requisitos Previos
------------------

* Python 3.7 o superior
* pip (gestor de paquetes de Python)
* Git (opcional, para clonar el repositorio)

Instalación Paso a Paso
------------------------

1. Clonar el Repositorio
^^^^^^^^^^^^^^^^^^^^^^^^

Si el proyecto está en un repositorio Git::

    git clone https://github.com/usuario/braille-converter.git
    cd braille-converter

O simplemente descargar y descomprimir el proyecto.

2. Crear un Entorno Virtual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Es recomendable usar un entorno virtual para aislar las dependencias::

    python -m venv .venv

3. Activar el Entorno Virtual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**En Windows (Git Bash):**

.. code-block:: bash

    source .venv/Scripts/activate

**En Windows (CMD):**

.. code-block:: cmd

    .venv\Scripts\activate.bat

**En Linux/Mac:**

.. code-block:: bash

    source .venv/bin/activate

4. Instalar las Dependencias
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install -r requirements.txt

Las dependencias principales son:

* Flask==3.0.0
* Werkzeug==3.0.1

Verificación de la Instalación
-------------------------------

Para verificar que todo está instalado correctamente::

    python -c "import flask; print(flask.__version__)"

Deberías ver la versión de Flask (3.0.0).

Configuración Adicional
-----------------------

No se requiere configuración adicional para el funcionamiento básico de la aplicación.
La aplicación está preconfigurada para ejecutarse en modo desarrollo en el puerto 5000.

Solución de Problemas Comunes
------------------------------

**Error: No module named 'flask'**

Si obtienes este error, asegúrate de:

1. Haber activado el entorno virtual
2. Haber instalado las dependencias con ``pip install -r requirements.txt``
3. Usar el Python correcto: ``".venv/Scripts/python.exe" app.py`` en Windows

**Error al instalar requirements.txt**

Asegúrate de usar el flag ``-r``::

    pip install -r requirements.txt

Y no::

    pip install requirements.txt  # ❌ Incorrecto
