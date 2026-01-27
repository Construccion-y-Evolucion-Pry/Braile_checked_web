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

# Casos de Prueba General

Este documento propone un conjunto de pruebas (unitarias, de integración y manuales) para verificar el correcto funcionamiento del proyecto.

## 1) Pruebas unitarias (función `texto_a_braille`)

Recomendado usar `pytest`.
AGREGAR IMAGENES

- Caso: letras minusculas
  - Entrada: `"abcxyz"`
  - Esperado: cada caracter mapeado correctamente según `BRAILLE_MAP`.

- Caso: números
  - Entrada: `"0123456789"`
  - Esperado: mapeo correcto (ver `BRAILLE_MAP`).

- Caso: puntuación y espacio
  - Entrada: `"Hola, mundo."`
  - Esperado: comas y puntos convertidos y espacios preservados.

- Caso: caracteres no soportados
  - Entrada: `"@#€"`
  - Esperado: los caracteres no mapeados se devuelven tal cual.

- Caso: cadena vacía
  - Entrada: `""`
  - Esperado: `""` (cadena vacía) o manejo definido.

## Consideraciones

Ejemplo de test (esqueleto):
SI ES OPCINAL TDD

```python
from app import texto_a_braille

def test_letras():
    assert texto_a_braille('abc') == '⠁⠃⠉'

def test_vacio():
    assert texto_a_braille('') == ''
```

## 3) Pruebas End-to-End (UI)

Manual o automatizado (Selenium / Playwright):

### Caso E2E-001: Conversión básica (Texto → Braille)

- Abrir `http://localhost:5000`.
- Asegurar que la pestaña "Texto → Braille" está activa.
- Introducir texto en el `textarea`.
- **Verificar**: La traducción a texto Braille es instantánea en la sección inferior.

### Caso E2E-002: Conversión Inversa (Braille → Texto)

- Cambiar a la pestaña "Braille → Texto".
- Marcar manualmente los puntos 1, 2, 3 (letra 'l') en las casillas.
- Verificar que al completar, se puede confirmar.
- O pegar texto braille unicode en el campo de entrada.
- **Resultado esperado**: El campo "Traducción a texto" muestra la letra correspondiente.

### Caso E2E-003: Exportar Word Espejo

- En la pestaña "Braille → Texto" (o donde esté disponible el botón), escribir una palabra.
- Clic en "Descargar Word Braille (Espejo)".
- **Verificar**: Se descarga un archivo `.docx`.
- Abrir archivo y validar:
  - Título "BRAILLE PARA PERFORAR".
  - Texto braille invertido (espejo).
  - Página de referencia con texto original.

### Caso E2E-004: Validación de Modos

- Ir a pestaña "Braille → Texto".
- Seleccionar "Modo Número".
- Validar que al escribir se agrega automáticamente el prefijo numérico.
- Intentar ingresar un patrón inválido para número (ej. puntos de una letra 'k' si no es válida como número).
- **Esperado**: Mensaje de error o validación en pantalla.

### Caso E2E-005: Responsividad

- Abrir la aplicación en diferentes tamaños de pantalla (desktop, tablet, mobile).
- **Verificar**:
  - Los botones se reorganizan correctamente en pantallas pequeñas.
  - Los botones ocupan el ancho completo en móviles.
  - Todas las funcionalidades siguen operativas.

## 4) Pruebas de accesibilidad

- Probar con lector de pantalla (NVDA, VoiceOver) y comprobar que las secciones son legibles.
- Comprobar contraste de colores y tamaño de fuente adaptables.

## 5) Pruebas de rendimiento

- Medir latencia para textos de diferentes tamaños (por ejemplo: 1KB, 10KB, 100KB).
- Determinar throughput concurrente con herramientas como `ab` o `wrk` si se despliega detrás de un servidor WSGI.

## 6) Pruebas de seguridad

- Limitar tamaño de payload para prevenir DoS.
- Validar que la API no ejecuta código o realiza operaciones peligrosas con la entrada.

### Checklist de aceptación

#### Funcionalidad Core

- Conversión correcta para letras básicas.
- API devuelve 400 para entradas vacías.
- Conversión en tiempo real funciona correctamente.
- Aplicación arranca en entorno virtual con `pip install -r requirements.txt`.
- Pruebas unitarias y de integración pasan en CI.

#### Funcionalidad de Copiar

- Botón "Copiar" copia el texto Braille al portapapeles.
- Feedback visual correcto (cambio a verde y texto "¡Copiado!").
- Validación de campo vacío funciona (muestra alerta).
- Funciona en Chrome, Firefox, Edge.

#### Funcionalidad de Exportar PNG

- Botón "Exportar PNG" genera la imagen correctamente.
- La imagen contiene título, texto original y traducción Braille.
- El nombre del archivo incluye timestamp.
- La imagen tiene alta calidad (scale: 2).
- Feedback visual correcto durante la generación.
- Validación de campo vacío funciona (muestra alerta).
- La librería html2canvas se carga correctamente desde CDN.

#### Interfaz de Usuario

- UI muestra y copia correctamente el resultado.
- Botones tienen estados hover correctos.
- Diseño responsivo funciona en móviles y tablets.
- Botones se apilan verticalmente en pantallas pequeñas.
- Iconos y textos de botones son claros y descriptivos.
