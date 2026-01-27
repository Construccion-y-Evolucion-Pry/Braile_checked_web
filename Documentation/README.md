# Documentación del Proyecto

Esta carpeta contiene la documentación del proyecto generada con Sphinx.

## Estructura

```
Documentation/
├── source/          # Archivos fuente de la documentación (.rst)
│   ├── conf.py     # Configuración de Sphinx
│   ├── index.rst   # Página principal
│   ├── app.rst     # Documentación del módulo app.py
│   ├── introduccion.rst
│   ├── instalacion.rst
│   ├── uso.rst
│   └── api.rst
│
├── build/           # Documentación generada (HTML)
│   └── html/       # Archivos HTML (abre index.html)
│
└── Makefile         # Archivo para compilar en Linux/Mac
```

## Generar la Documentación desde web (pythondoc)

### Opción 1: Usando el script automático (Recomendado)

**En Windows (Git Bash):**
```bash
./generar_docs.sh
```

**En Windows (CMD/PowerShell):**
```cmd
generar_docs.bat
```

### Opción 2: Manualmente

```bash
# Activar el entorno virtual
source .venv/Scripts/activate  # En Git Bash
# o
.venv\Scripts\activate.bat     # En CMD

# Generar la documentación
cd Documentation
sphinx-build -b html source build/html
```

### Opción 3: Con Python directamente

```bash
python -m sphinx -b html Documentation/source Documentation/build/html
```

## Ver la Documentación como apartado de python doc

Una vez generada, abre el archivo:

```
Documentation/build/html/index.html
```

En tu navegador web.

## Actualizar la Documentación

Cada vez que modifiques el código o los archivos `.rst` en `source/`, 
debes regenerar la documentación ejecutando alguno de los comandos anteriores.

## Archivos Importantes

- **conf.py**: Configuración de Sphinx (extensiones, tema, etc.)
- **index.rst**: Página principal de la documentación
- **app.rst**: Documentación automática del código Python (usando autodoc)

## Extensiones Utilizadas

- `sphinx.ext.autodoc`: Extrae documentación de los docstrings
- `sphinx.ext.viewcode`: Agrega enlaces al código fuente
- `sphinx.ext.napoleon`: Soporta docstrings estilo Google/NumPy
- `sphinx_rtd_theme`: Tema Read the Docs

## Agregar Nueva Documentación

1. Crear un nuevo archivo `.rst` en `Documentation/source/`
2. Agregar el nombre del archivo (sin extensión) al `toctree` en `index.rst`
3. Regenerar la documentación

Ejemplo:

```rst
.. toctree::
   :maxdepth: 2

   introduccion
   instalacion
   mi_nuevo_archivo  # ← Agregar aquí
```
