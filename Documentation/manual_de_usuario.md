<div align="center">
  <h2>Escuela Politecnica Nacional</h2>
  <h3>Facultad de Ingeniería de Sistemas</h3>
  <h4>Construcción y Evolución de Software</h4>
  
  <hr width="60%">
  
  <br>
  
  <table align="center">
    <tr>
      <td><b>Versión:</b></td>
      <td>1.0</td>
    </tr>
    <tr>
      <td><b>Grupo:</b></td>
      <td>5</td>
    </tr>
    <tr>
      <td><b>Fecha:</b></td>
      <td>Noviembre 2025</td>
    </tr>
  </table>
</div>

<div style="page-break-after: always;"></div>

---

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
Al iniciar el servicio web, se vera la siguiente pantalla: 

![Dashboard de la aplicacion](../Documentation/DashbordBraille.png)

- Escribe o pega el texto en el área "Texto Original".
- El texto convertido aparecerá en la columna "Texto en Braille" viendose de esta manera el resultado final:

![Demostración](../Documentation/MuestraBraile.png)


## Accesibilidad

- La interfaz usa texto grande para la salida en Braille.
- Se recomienda probar con lectores de pantalla y aumentar el tamaño de la fuente si es necesario.

## Consejos a futuro

- Para grandes volúmenes de texto, considerar paginar la conversión o procesar por lotes.
- Validar entrada en aplicaciones que usen la API para evitar strings muy largos o maliciosos.


