<div align="center">
  <h2>Escuela Politecnica Nacional</h2>
  <h3>Facultad de Ingeniería de Sistemas</h3>
  <h4>Construcción y Evolución de Software</h4>
  
  <hr width="60%">
  
  <br>
  
  <table align="center">
    <tr>
      <td><b>Versión:</b></td>
      <td>2.0</td>
    </tr>
    <tr>
      <td><b>Grupo:</b></td>
      <td>5</td>
    </tr>
    <tr>
      <td><b>Fecha:</b></td>
      <td>Enero 2026</td>
    </tr>
  </table>
</div>

<div style="page-break-after: always;"></div>

---

# Casos de Prueba General

Este documento propone un conjunto de pruebas (unitarias, de integración y manuales) para verificar el correcto funcionamiento del proyecto.

## 1) Pruebas unitarias (funciones de conversión)

Recomendado usar `pytest` o `unittest`.

### Función `texto_a_braille`

- **Caso**: letras minúsculas
  - Entrada: `"abcxyz"`
  - Esperado: cada carácter mapeado correctamente según `BRAILLE_MAP`.

- **Caso**: números
  - Entrada: `"0123456789"`
  - Esperado: mapeo correcto con prefijo numérico (⠼).

- **Caso**: puntuación y espacio
  - Entrada: `"Hola, mundo."`
  - Esperado: comas y puntos convertidos y espacios preservados.

- **Caso**: caracteres no soportados
  - Entrada: `"@#€"`
  - Esperado: los caracteres no mapeados se devuelven tal cual.

- **Caso**: cadena vacía
  - Entrada: `""`
  - Esperado: `""` (cadena vacía).

### Función `braille_a_texto`

- **Caso**: texto Braille básico
  - Entrada: `"⠓⠕⠇⠁"`
  - Esperado: `"hola"`

- **Caso**: texto con mayúsculas
  - Entrada: `"⠨⠓⠕⠇⠁"`
  - Esperado: `"Hola"`

- **Caso**: texto con números
  - Entrada: `"⠼⠃⠚⠃⠙"`
  - Esperado: `"2024"`

### Función `espejo_braille`

- **Caso**: inversión de un carácter simple
  - Entrada: `"⠇"` (letra "l", puntos 1,2,3)
  - Esperado: `"⠸"` (puntos 4,5,6 - columna derecha)

- **Caso**: inversión de una palabra
  - Entrada: `"⠓⠕⠇⠁"` (hola)
  - Esperado: Caracteres invertidos horizontalmente y en orden reverso

### Ejemplo de test (esqueleto):

```python
from app import texto_a_braille, braille_a_texto, espejo_braille

def test_letras():
    assert texto_a_braille('abc') == '⠁⠃⠉'

def test_vacio():
    assert texto_a_braille('') == ''

def test_braille_a_texto_basico():
    assert braille_a_texto('⠓⠕⠇⠁') == 'hola'

def test_espejo_simple():
    resultado = espejo_braille('⠇')
    assert len(resultado) == 1
    # Verificar que los puntos se invirtieron
```

---

## 2) Pruebas de Integración (API)

### Endpoint `/convertir` (POST)

- **Caso**: Conversión exitosa
  - Body: `{"texto": "hola"}`
  - Esperado: `{"texto_braille": "⠓⠕⠇⠁"}`
  - Status: 200

- **Caso**: Texto vacío
  - Body: `{"texto": ""}`
  - Esperado: `{"error": "No se proporcionó texto"}`
  - Status: 400

### Endpoint `/convertir-braille` (POST)

- **Caso**: Conversión exitosa
  - Body: `{"braille": "⠓⠕⠇⠁"}`
  - Esperado: `{"texto": "hola"}`
  - Status: 200

- **Caso**: Braille vacío
  - Body: `{"braille": ""}`
  - Esperado: `{"error": "No se proporcionó texto braille"}`
  - Status: 400

### Endpoint `/validar-braille` (POST)

- **Caso**: Validación exitosa en modo letra
  - Body: `{"braille": "⠇", "modo": "letra"}`
  - Esperado: `{"ok": true, "caracter": "⠇", "traduccion": "l"}`
  - Status: 200

- **Caso**: Validación fallida - número en modo letra
  - Body: `{"braille": "⠁", "modo": "numero"}`
  - Esperado: `{"error": "No es un número Braille válido (0-9)"}`
  - Status: 400

- **Caso**: Carácter vacío
  - Body: `{"braille": "", "modo": "letra"}`
  - Esperado: `{"error": "No se proporcionó carácter Braille"}`
  - Status: 400

- **Caso**: Modo no reconocido
  - Body: `{"braille": "⠁", "modo": "invalido"}`
  - Esperado: `{"error": "Modo no reconocido"}`
  - Status: 400

### Endpoint `/descargar-braille-word` (POST)

- **Caso**: Descarga exitosa
  - Body: `{"braille": "⠓⠕⠇⠁", "texto": "hola"}`
  - Esperado: Archivo .docx con contenido correcto
  - Status: 200
  - Headers: `Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document`

- **Caso**: Sin contenido Braille
  - Body: `{"braille": "", "texto": "hola"}`
  - Esperado: `{"error": "No hay contenido Braille"}`
  - Status: 400

---

## 3) Pruebas End-to-End (UI)

Manual o automatizado (Selenium / Playwright):

### Caso E2E-001: Conversión básica (Texto → Braille)

**Objetivo**: Verificar la conversión en tiempo real de texto a Braille.

**Pasos**:
1. Abrir `http://localhost:5000`
2. Asegurar que la pestaña "Texto → Braille" está activa
3. Introducir "hola" en el `textarea`

**Verificar**:
- La traducción a Braille "⠓⠕⠇⠁" aparece instantáneamente
- El cursor parpadeante se muestra después del texto
- No hay errores en la consola

**Prioridad**: Alta

---

### Caso E2E-002: Conversión Inversa (Braille → Texto)

**Objetivo**: Verificar la traducción de Braille a texto usando casillas.

**Pasos**:
1. Cambiar a la pestaña "Braille → Texto"
2. Marcar manualmente los puntos 1, 2, 3 (letra 'l')
3. Presionar Enter

**Verificar**:
- El carácter ⠇ aparece en el área de Braille
- El campo "Traducción a texto" muestra "l"
- Mensaje de éxito: "Carácter agregado correctamente"
- Las casillas se limpian automáticamente

**Prioridad**: Alta

---

### Caso E2E-003: Exportar Word Espejo

**Objetivo**: Verificar la generación correcta del documento Word en formato espejo.

**Pasos**:
1. En la pestaña "Braille → Texto", escribir la palabra "hola"
2. Hacer clic en "Descargar Word Braille (Espejo)"

**Verificar**:
- Se descarga un archivo `braille_para_perforar.docx`
- Al abrir el archivo:
  - Página 1: Encabezado con instrucciones de perforación
  - Página 1: Título "BRAILLE PARA PERFORAR (FORMATO ESPEJO)"
  - Página 1: Texto Braille invertido (fuente 24pt)
  - Página 2: Título "TEXTO ORIGINAL (Referencia)"
  - Página 2: Texto "hola" (fuente 12pt)

**Prioridad**: Alta

---

### Caso E2E-004: Validación de Modos

**Objetivo**: Verificar que la validación contextual funciona correctamente.

**Pasos**:
1. Ir a pestaña "Braille → Texto"
2. Seleccionar "Modo Número" (clic en el botón o presionar `6`)

**Verificar**:
- Botón "Modo Número" se pone amarillo con borde dorado
- Se añade automáticamente el prefijo numérico (⠼) al área de Braille
- Mensaje de ayuda: "Modo NÚMERO activo (6) - Presiona Enter para confirmar cada carácter"

**Continuar**:
3. Intentar ingresar un patrón de letra (ej: puntos 1,2,3 = "l")
4. Presionar Enter

**Verificar**:
- Mensaje de error: "No es un número Braille válido (0-9)"
- El carácter NO se agrega a la palabra
- Las casillas permanecen marcadas

**Prioridad**: Alta

---

### Caso E2E-005: Responsividad

**Objetivo**: Verificar que la aplicación funciona en diferentes tamaños de pantalla.

**Pasos**:
1. Abrir la aplicación en diferentes dispositivos o usar DevTools
2. Probar resoluciones: 1920x1080 (desktop), 768x1024 (tablet), 375x667 (móvil)

**Verificar** en cada resolución:
- Los botones se reorganizan correctamente (vertical en móviles)
- Las pestañas son accesibles y legibles
- Las casillas Braille son utilizables
- Los textos no se sobreponen
- Todas las funcionalidades siguen operativas

**Prioridad**: Media

---

### Caso E2E-006: Tour Interactivo (NUEVO)

**Objetivo**: Verificar que el Tour muestra correctamente el mapeo de teclado.

**Pasos**:
1. Abrir `http://localhost:5000`
2. Hacer clic en el botón "Tour ❓" en el menú de navegación

**Verificar**:
- El sistema cambia automáticamente a la pestaña "Braille → Texto"
- Aparece un tooltip a la derecha de las casillas Braille
- El tooltip contiene:
  - Título: "⌨️ Mapeo de Teclado (Numpad)"
  - Grid 2×3 con mapeo visual: 7→●1, 8→●4, 4→●2, 5→●5, 1→●3, 2→●6
  - Nota: "El punto 1 comienza arriba a la izquierda."
  - Botón × para cerrar
- Las casillas Braille tienen un resplandor amarillo (clase "tour-active")

**Continuar**:
3. Hacer clic en el botón × del tooltip

**Verificar**:
- El tooltip desaparece
- El resplandor amarillo desaparece
- La funcionalidad normal continúa

**Prioridad**: Alta

---

### Caso E2E-007: Botón Block Mayús - Activación Manual (NUEVO)

**Objetivo**: Verificar que el botón Block Mayús funciona correctamente al hacer clic.

**Precondición**: Modo Letra debe estar activo.

**Pasos**:
1. Ir a pestaña "Braille → Texto"
2. Asegurar que "Modo Letra" está activo (botón blanco)
3. Hacer clic en el botón "Block Mayus"

**Verificar**:
- El botón cambia a color rojo (#e74c3c)
- El botón tiene borde rojo oscuro (#c0392b)
- El botón tiene la clase "modo-mayus-activo"

**Continuar**:
4. Escribir la letra "m" (puntos 1,3,4)
5. Presionar Enter

**Verificar**:
- El área de Braille muestra: ⠨⠍ (prefijo de mayúscula + m)
- La traducción muestra: "M" (mayúscula)
- Mensaje de éxito aparece

**Continuar**:
6. Hacer clic nuevamente en "Block Mayus" para desactivar

**Verificar**:
- El botón vuelve a color gris oscuro (#42494f)
- La clase "modo-mayus-activo" se elimina

**Prioridad**: Alta

---

### Caso E2E-008: Botón Block Mayús - Sincronización con Tecla Física (NUEVO)

**Objetivo**: Verificar que el botón se sincroniza con la tecla Bloq Mayús del teclado.

**Precondición**: Modo Letra activo, Bloq Mayús del teclado INACTIVO al inicio.

**Pasos**:
1. Ir a pestaña "Braille → Texto" en Modo Letra
2. Verificar que el botón "Block Mayus" está inactivo (gris)
3. Presionar la tecla física **Bloq Mayús** del teclado

**Verificar**:
- El botón "Block Mayus" en pantalla se activa (rojo)
- La sincronización es inmediata (evento `keydown` detectado)

**Continuar**:
4. Presionar nuevamente la tecla física **Bloq Mayús**

**Verificar**:
- El botón en pantalla se desactiva (vuelve a gris)

**Nota**: Este test requiere interacción física con el teclado, difícil de automatizar.

**Prioridad**: Media

---

### Caso E2E-009: Block Mayús - Restricción por Modo (NUEVO)

**Objetivo**: Verificar que Block Mayús solo funciona en Modo Letra.

**Pasos**:
1. Ir a pestaña "Braille → Texto"
2. Activar Block Mayús (botón rojo)
3. Presionar `6` para cambiar a Modo Número

**Verificar**:
- El botón "Block Mayus" se desactiva automáticamente (vuelve a gris)
- La clase "modo-mayus-activo" se elimina
- El botón "Modo Número" se activa (amarillo)

**Continuar**:
4. Intentar hacer clic en "Block Mayus"

**Verificar**:
- El botón NO se activa (permanece gris)
- No tiene efecto mientras esté en Modo Número

**Continuar**:
5. Volver a Modo Letra presionando `9`

**Verificar**:
- Ahora el botón "Block Mayus" puede activarse nuevamente

**Prioridad**: Media

---

### Caso E2E-010: Atajos de Teclado - Cambio de Modo (NUEVO)

**Objetivo**: Verificar que los atajos `9`, `6`, `3` cambian de modo correctamente.

**Pasos**:
1. Ir a pestaña "Braille → Texto"
2. Presionar la tecla `9`

**Verificar**:
- Botón "Modo Letra" se activa (blanco con borde gris)
- Mensaje de ayuda: "Modo LETRA activo (9) - Presiona Enter para confirmar cada letra"

**Continuar**:
3. Presionar la tecla `6`

**Verificar**:
- Botón "Modo Número" se activa (amarillo)
- Se añade prefijo ⠼ al área de Braille
- Mensaje de ayuda: "Modo NÚMERO activo (6) - Presiona Enter para confirmar cada carácter"

**Continuar**:
4. Presionar la tecla `3`

**Verificar**:
- Botón "Modo Carácter" se activa (verde)
- Mensaje de ayuda: "Modo CARÁCTER ESPECIAL activo (3) - Presiona Enter para confirmar"

**Prioridad**: Alta

---

### Caso E2E-011: Atajos de Teclado - Entrada de Puntos con Numpad (NUEVO)

**Objetivo**: Verificar que las teclas del numpad marcan/desmarcan casillas correctamente.

**Precondición**: Bloq Num (Num Lock) debe estar ACTIVO.

**Pasos**:
1. Ir a pestaña "Braille → Texto"
2. Presionar la tecla `7` del numpad

**Verificar**:
- La casilla del Punto 1 (arriba izquierda) se marca
- Aparece un punto negro en el centro de la casilla

**Continuar**:
3. Presionar las teclas `4` y `1` del numpad

**Verificar**:
- Las casillas de los Puntos 2 y 3 se marcan
- Ahora hay tres casillas marcadas (columna izquierda completa)

**Continuar**:
4. Presionar `7` nuevamente

**Verificar**:
- La casilla del Punto 1 se DESMARCa (toggle off)
- Solo quedan marcados los Puntos 2 y 3

**Prioridad**: Alta

---

### Caso E2E-012: Atajos de Teclado - Enter y Escape (NUEVO)

**Objetivo**: Verificar que Enter confirma y Escape limpia todo.

**Pasos**:
1. Ir a pestaña "Braille → Texto"
2. Marcar los puntos 1, 2, 3 (letra "l")
3. Presionar `Enter`

**Verificar**:
- El carácter ⠇ se agrega al área de Braille
- La traducción muestra "l"
- Las casillas se limpian automáticamente
- Mensaje de éxito aparece

**Continuar**:
4. Escribir otra letra cualquiera (ej: "a" - punto 1)
5. Presionar `Escape` (antes de confirmar con Enter)

**Verificar**:
- El área de Braille se limpia completamente
- La traducción se limpia
- Todas las casillas se desmarcan
- El modo vuelve a "Modo Letra" si estaba en otro modo
- Block Mayús se desactiva si estaba activo

**Prioridad**: Alta

---

### Caso E2E-013: Validación - Mensaje de Error Visual (NUEVO)

**Objetivo**: Verificar que los mensajes de error aparecen y desaparecen correctamente.

**Pasos**:
1. Ir a pestaña "Braille → Texto" en Modo Letra
2. Presionar `Enter` sin marcar ningún punto

**Verificar**:
- Aparece un mensaje debajo de las casillas Braille
- Mensaje: "No has marcado ningún punto"
- Fondo rojo claro (#fdf1f1), texto rojo oscuro (#6b1f1f)
- Animación de entrada (slideDown)

**Continuar**:
3. Esperar 3 segundos

**Verificar**:
- El mensaje desaparece automáticamente con animación de fade
- El mensaje se elimina del DOM

**Prioridad**: Media

---

### Caso E2E-014: Validación - Error de Modo Incorrecto (NUEVO)

**Objetivo**: Verificar que la validación rechaza patrones inválidos según el modo.

**Pasos**:
1. Ir a pestaña "Braille → Texto"
2. Activar Modo Número (presionar `6` o hacer clic)
3. Marcar los puntos 1, 2, 3 (letra "l", no válida como número)
4. Presionar Enter

**Verificar**:
- Mensaje de error: "No es un número Braille válido (0-9)"
- Fondo rojo claro, texto rojo oscuro
- El carácter NO se agrega al área de Braille
- Las casillas permanecen marcadas (no se limpian)

**Prioridad**: Alta

---

### Caso E2E-015: Integración Completa - Escribir una Palabra Completa (NUEVO)

**Objetivo**: Verificar el flujo completo de escritura de una palabra con mayúscula inicial.

**Pasos**:
1. Ir a pestaña "Braille → Texto"
2. Activar Block Mayús
3. Escribir "M" (puntos 1,3,4) y presionar Enter
4. Desactivar Block Mayús
5. Escribir "a" (punto 1) y presionar Enter
6. Escribir "r" (puntos 1,2,3,5) y presionar Enter
7. Escribir "í" (puntos 3,4) y presionar Enter
8. Escribir "a" (punto 1) y presionar Enter

**Verificar después de cada Enter**:
- Mensaje de éxito: "Carácter agregado correctamente"
- Las casillas se limpian
- El área de Braille se actualiza
- La traducción se actualiza en tiempo real

**Verificar al final**:
- Área de Braille: ⠨⠍⠁⠗⠌⠁
- Traducción: "María"

**Prioridad**: Alta

---

### Caso E2E-016: Tour - Responsive en Móvil (NUEVO)

**Objetivo**: Verificar que el Tour se adapta a pantallas pequeñas.

**Pasos**:
1. Abrir la aplicación en modo móvil (375x667) usando DevTools
2. Hacer clic en "Tour ❓"

**Verificar**:
- El tooltip aparece DEBAJO de las casillas (no al lado)
- El tooltip tiene `position: static` (no absolute)
- El ancho del tooltip es 100% o max-width: 300px
- No hay flechas del tooltip (se ocultan en móvil)
- El contenido es legible y no se corta

**Prioridad**: Baja

---

## 4) Pruebas de Accesibilidad

### Caso ACC-001: Navegación con Teclado

**Pasos**:
1. Abrir la aplicación
2. Usar solo la tecla `Tab` para navegar

**Verificar**:
- Todos los botones son alcanzables
- El foco es visible (outline o borde)
- El orden de tabulación es lógico
- Las casillas Braille NO son alcanzables con Tab (usar atajos numéricos)

### Caso ACC-002: Contraste de Colores

**Herramienta**: WebAIM Contrast Checker

**Verificar**:
- Texto blanco (#ecf0f1) sobre fondo oscuro (#212529): Ratio ≥ 7:1 (AAA)
- Botones activos tienen contraste suficiente con el fondo
- Mensajes de error/éxito son legibles

### Caso ACC-003: Lector de Pantalla

**Herramienta**: NVDA (Windows) o VoiceOver (Mac)

**Verificar**:
- Los botones tienen textos descriptivos
- Las áreas de texto tienen etiquetas (`<label>`)
- Los mensajes de error se leen automáticamente (aria-live)
- La estructura semántica es correcta (`<header>`, `<main>`, `<footer>`)

---

## 5) Pruebas de Rendimiento

### Caso PERF-001: Conversión de Texto Largo

**Pasos**:
1. Generar un texto de 10,000 caracteres
2. Pegarlo en el área de texto (pestaña Texto → Braille)
3. Medir el tiempo de conversión

**Verificar**:
- La conversión se completa en < 1 segundo
- No hay congelamiento de la UI
- No hay errores de memoria en la consola

### Caso PERF-002: Múltiples Conversiones Rápidas

**Pasos**:
1. En pestaña Braille → Texto, escribir 50 letras rápidamente
2. Presionar Enter después de cada una

**Verificar**:
- Todas las letras se procesan sin pérdida
- No hay retrasos visuales
- Los mensajes de éxito no se acumulan (uno a la vez)

---

## 6) Pruebas de Seguridad

### Caso SEC-001: Inyección de Código en Texto

**Pasos**:
1. Intentar ingresar código JavaScript en el área de texto:
   ```
   <script>alert('XSS')</script>
   ```

**Verificar**:
- El código NO se ejecuta
- Se convierte a Braille como texto normal
- No aparece ninguna alerta

### Caso SEC-002: Payload Grande

**Pasos**:
1. Intentar enviar un JSON muy grande (>10MB) al endpoint `/convertir`

**Verificar**:
- La petición es rechazada
- Status 400 o 413 (Payload Too Large)
- No hay caída del servidor

---

## Checklist de Aceptación

### Funcionalidad Core

- [✅] Conversión correcta para letras básicas (a-z)
- [✅] Conversión correcta para números (0-9)
- [✅] Conversión correcta para caracteres especiales (ñ, á, é, í, ó, ú, ü)
- [✅] API `/convertir` funciona correctamente
- [✅] API `/convertir-braille` funciona correctamente
- [✅] API `/validar-braille` valida según modo
- [✅] Conversión en tiempo real funciona sin delays

### Funcionalidad de Traducción Inversa

- [✅] Casillas interactivas funcionan correctamente
- [✅] Entrada por numpad funciona correctamente
- [✅] Entrada por pegado directo funciona
- [✅] Validación contextual rechaza patrones inválidos
- [✅] Mensajes de error son claros y descriptivos

### Funcionalidad Tour Interactivo (NUEVO)

- [✅] Botón "Tour ❓" es visible en el menú
- [✅] Tour cambia automáticamente a la pestaña correcta
- [✅] Tooltip muestra el mapeo de teclado correcto
- [✅] Tooltip tiene botón × para cerrar
- [✅] Tooltip desaparece al hacer clic en ×
- [✅] Resplandor amarillo aparece/desaparece correctamente
- [✅] Tour es responsive en móviles

### Funcionalidad Block Mayús (NUEVO)

- [✅] Botón "Block Mayus" está visible en panel lateral
- [✅] Botón cambia de color al activarse (rojo)
- [✅] Botón se sincroniza con tecla física Bloq Mayús
- [✅] Botón solo funciona en Modo Letra
- [✅] Botón añade prefijo de mayúscula correctamente
- [✅] Estado se detecta al cargar la página

### Atajos de Teclado (NUEVO)

- [✅] Tecla `9` activa Modo Letra
- [✅] Tecla `6` activa Modo Número y añade prefijo
- [✅] Tecla `3` activa Modo Carácter
- [✅] Teclas `7,4,1,8,5,2` marcan/desmarcan casillas
- [✅] Tecla `Enter` confirma y valida el carácter
- [✅] Tecla `Escape` limpia todo y reinicia

### Funcionalidad de Exportación

- [✅] Botón "Descargar Texto" genera archivo .txt correcto
- [✅] Botón "Descargar Word Braille (Espejo)" genera .docx
- [✅] Archivo Word contiene Braille invertido correctamente
- [✅] Archivo Word contiene página de referencia
- [✅] Archivo Word tiene encabezado con instrucciones
- [✅] Descarga funciona en Chrome, Firefox, Edge

### Interfaz de Usuario

- [✅] Pestañas cambian correctamente
- [✅] Botones tienen estados hover correctos
- [✅] Diseño responsive funciona en móviles y tablets
- [✅] Botones se apilan verticalmente en pantallas pequeñas
- [✅] Iconos y textos de botones son claros
- [✅] Mensajes de validación aparecen y desaparecen
- [✅] Mensajes tienen colores y animaciones correctas

### Accesibilidad

- [✅] Navegación por teclado funciona completamente
- [✅] Contraste de colores cumple WCAG AA
- [✅] Textos son legibles con lectores de pantalla
- [✅] Fuentes son suficientemente grandes
- [✅] Foco visual es claro en todos los elementos

### Rendimiento

- [  ] Conversión de texto largo (10K caracteres) < 1s
- [  ] No hay memory leaks en sesiones largas
- [  ] UI no se congela durante operaciones

### Seguridad

- [ ] No hay ejecución de código inyectado
- [ ] Payloads grandes son rechazados
- [✅] API valida todos los parámetros

---

## Matriz de Cobertura de Pruebas

| Funcionalidad | Unitaria | Integración | E2E | Accesibilidad |
|---------------|----------|-------------|-----|---------------|
| Texto → Braille | ✅ | ✅ | ✅ | ✅ |
| Braille → Texto | ✅ | ✅ | ✅ | ✅ |
| Validación contextual | ✅ | ✅ | ✅ | - |
| Tour Interactivo | - | - | ✅ | ✅ |
| Block Mayús | - | - | ✅ | ✅ |
| Atajos de teclado | - | - | ✅ | ✅ |
| Exportar Word | ✅ | ✅ | ✅ | - |
| Exportar Texto | - | - | ✅ | - |

---

## Registro de Cambios

### Versión 2.0 (Enero 2026)
- ✅ Añadidos 11 casos E2E nuevos (E2E-006 a E2E-016)
- ✅ Añadida sección de validación contextual
- ✅ Documentadas pruebas para Tour Interactivo
- ✅ Documentadas pruebas para Block Mayús
- ✅ Documentadas pruebas para atajos de teclado
- ✅ Actualizado checklist de aceptación
- ✅ Añadida matriz de cobertura

### Versión 1.0 (Noviembre 2025)
- ✅ Casos E2E básicos (E2E-001 a E2E-005)
- ✅ Pruebas de integración de API
- ✅ Pruebas unitarias básicas
- ✅ Checklist inicial

---

<div align="center">

**Casos de Prueba General**  
*Versión 2.0 - Enero 2026*

Total de casos documentados: **60+**  
(16 E2E + 10 Unitarias + 8 Integración + 26 Checklist)

</div>