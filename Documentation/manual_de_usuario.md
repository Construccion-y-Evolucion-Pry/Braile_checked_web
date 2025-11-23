# Manual de Usuario

## Visión general

Aplicación web para convertir texto normal a símbolos Braille Unicode.
Interfaz sencilla y un endpoint REST para conversión.

## Requisitos

- Python 3.7 o superior
- `pip`
- (Opcional) Entorno virtual

## Instalación (Windows - CMD)

1. Clona el repositorio o descarga los archivos.
2. Crea y activa un entorno virtual:

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

3. Instala dependencias:

```cmd
pip install -r requirements.txt
```

## Ejecutar la aplicación

```cmd
python app.py
```

Abre `http://localhost:5000` en tu navegador.

## Uso — Interfaz Web

- Escribe o pega el texto en el área "Texto Original".
- Haz clic en el botón "Convertir a Braille ⚡".
- El texto convertido aparecerá en la columna "Texto en Braille".
- Pulsa "📋 Copiar Braille" para copiar el resultado al portapapeles.

Atajos y comportamientos:
- `Ctrl+Enter` en el área de texto dispara la conversión.

## Uso — API REST

Endpoint principal para integración:

- `POST /convertir` — Convierte texto a Braille.

Request (JSON):

```json
{ "texto": "Hola mundo" }
```

Response (200 OK):

```json
{
  "texto_original": "Hola mundo",
  "texto_braille": "⠓⠕⠇⠁⠀⠍⠥⠝⠙⠕"
}
```

Errores comunes:
- Si no se envía `texto` o está vacío, la API devuelve `400` con `{ "error": "No se proporcionó texto" }`.

## Mapeo y límites

- El mapeo se realiza con el diccionario `BRAILLE_MAP` en `app.py`.
- Soporta letras a–z, números 0–9, espacio y puntuación básica (.,;:!?-()).
- Caracteres no mapeados se devuelven tal cual.

## Accesibilidad

- La interfaz usa texto grande para la salida en Braille.
- Se recomienda probar con lectores de pantalla y aumentar el tamaño de la fuente si es necesario.

## Regenerar documentación Sphinx

En Windows (CMD):

```cmd
generar_docs.bat
```

O manualmente:

```cmd
python -m sphinx -b html Documentation/source Documentation/build/html
```

## Consejos de uso y buenas prácticas

- Para grandes volúmenes de texto, considerar paginar la conversión o procesar por lotes.
- Validar entrada en aplicaciones que usen la API para evitar strings muy largos o maliciosos.

## Contacto

Para dudas o contribuciones, abre un issue o un pull request en el repositorio.
