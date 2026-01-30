# 📖 BraiLator

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-Educational-purple.svg)]()

**BraiLator** es una aplicación web bidireccional para la traducción entre texto español y Braille Unicode (Grado 1). Desarrollada con Flask, ofrece una interfaz accesible e intuitiva que permite tanto la conversión de texto a Braille como la decodificación inversa mediante un teclado virtual interactivo.

---

## 🚀 Características Principales

### ✅ Traducción Bidireccional
- **Texto → Braille**: Conversión en tiempo real con soporte completo para español
- **Braille → Texto**: Entrada interactiva mediante casillas virtuales o pegado directo de Unicode

### ✅ Soporte Lingüístico Completo
- Alfabeto español (a-z, incluyendo ñ)
- Vocales acentuadas (á, é, í, ó, ú)
- Diéresis (ü)
- Números (0-9) con prefijos contextuales
- Signos de puntuación (¿?, ¡!, . , ; : - ( ))
- Manejo de mayúsculas con indicador específico

### ✅ Funcionalidades Avanzadas
- **Modos de Validación**: Letra (9), Número (6) y Carácter Especial (3)
- **Entrada por Teclado**: Mapeo del numpad al patrón Braille 2×3
- **Botón Block Mayús**: Sincronización automática con la tecla física Bloq Mayús
- **Tour Interactivo**: Guía visual paso a paso del mapeo de teclas y funcionalidades principales
- **Exportación a Word**: Formato espejo para perforación manual desde el reverso del papel
- **Validación Contextual**: Verificación en tiempo real según el modo activo

### ✅ Accesibilidad y Diseño
- Interfaz responsive (móvil, tablet, desktop)
- Tipografía grande (32px) para visualización de Braille
- Validación contextual en tiempo real
- Mensajes de error claros y descriptivos
- Sistema de notificaciones visuales para feedback inmediato

---

## 📋 Requisitos del Sistema

- **Python**: 3.7 o superior
- **pip**: Gestor de paquetes de Python
- **Navegador moderno**: Chrome, Firefox, Edge (con soporte Unicode Braille)

---

## 🔧 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Construccion-y-Evolucion-Pry/Braile_checked_web.git
cd Braile_checked_web
```

### 2. Crear entorno virtual

```bash
# Windows (CMD)
python -m venv .venv
.venv\Scripts\activate.bat

# Windows (Git Bash)
python -m venv .venv
source .venv/Scripts/activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python app.py
```

Abrir en el navegador: `http://localhost:5000`

---

## 🎯 Uso de la Aplicación

### Pestaña: Texto → Braille

1. Escribir o pegar texto en el área de entrada
2. La traducción a Braille aparece instantáneamente
3. Copiar el resultado con un clic

### Pestaña: Braille → Texto

#### 🎓 Tour Interactivo (¡NUEVO!)

Antes de comenzar, haz clic en el botón **"Tour ❓"** en el menú de navegación para acceder a una guía interactiva que muestra:

- **Mapeo visual del teclado numpad** a los 6 puntos Braille
- **Distribución espacial** del patrón 2×3
- **Instrucciones de uso** con ejemplos prácticos
- **Atajos de teclado** disponibles

El Tour resalta visualmente las casillas Braille y muestra un tooltip con la siguiente información:

```
⌨️ Mapeo de Teclado (Numpad)
Usa tu teclado numérico para marcar los puntos:

7 ➝ ●1    8 ➝ ●4
4 ➝ ●2    5 ➝ ●5
1 ➝ ●3    2 ➝ ●6

El punto 1 comienza arriba a la izquierda.
```

#### 1. Seleccionar modo

- **Modo Letra (9)**: Para escritura normal de letras y símbolos básicos
- **Modo Número (6)**: Añade automáticamente el prefijo numérico (⠼)
- **Modo Carácter (3)**: Para signos de puntuación y caracteres especiales

💡 **Tip**: Los números entre paréntesis son atajos de teclado

#### 2. Entrada de caracteres

**Opción A: Casillas interactivas**
- Marcar manualmente los 6 puntos Braille según el patrón 2×3
- Las casillas se organizan como:
  ```
  ●1  ●4
  ●2  ●5
  ●3  ●6
  ```

**Opción B: Teclado numpad** (recomendado)
- Usar el teclado numérico para marcar/desmarcar puntos:
  ```
  Tecla 7 → Punto 1 (arriba izquierda)
  Tecla 4 → Punto 2 (medio izquierda)
  Tecla 1 → Punto 3 (abajo izquierda)
  Tecla 8 → Punto 4 (arriba derecha)
  Tecla 5 → Punto 5 (medio derecha)
  Tecla 2 → Punto 6 (abajo derecha)
  ```

**Opción C: Pegar Unicode**
- Introducir directamente caracteres Braille copiados desde otra fuente

#### 3. Botón Block Mayús (🔠 NUEVO)

El botón **"Block Mayus"** permite activar el modo de mayúsculas para escritura de nombres propios, siglas o texto en mayúsculas:

- **Ubicación**: A la izquierda de las casillas Braille
- **Funcionamiento**: 
  - Clic manual para activar/desactivar
  - **Sincronización automática** con la tecla física Bloq Mayús del teclado
  - Solo funciona en **Modo Letra** (se desactiva automáticamente en otros modos)
- **Indicador visual**: 
  - Inactivo: Gris oscuro
  - Activo: Rojo brillante con borde destacado
- **Efecto**: Añade el prefijo de mayúscula (⠨) antes de cada letra

**Ejemplo de uso**:
```
1. Activar Block Mayús (botón rojo)
2. Escribir "m" → Se guarda como "⠨⠍" (M)
3. Escribir "a" → Se guarda como "⠁" (a minúscula)
```

#### 4. Confirmar caracteres

- **Presionar `Enter`** para agregar el carácter a la palabra
- El sistema valida automáticamente según el modo activo
- Si el carácter no es válido, aparece un mensaje de error descriptivo

#### 5. Descargar resultados

- **Descargar Texto (.txt)**: Archivo plano con la traducción
- **Descargar Word Braille (Espejo)**: Formato `.docx` optimizado para perforación manual

---

### ⌨️ Atajos de Teclado (Pestaña Braille → Texto)

| Tecla | Función |
|-------|---------|
| **9** | Activar Modo Letra |
| **6** | Activar Modo Número (añade prefijo ⠼) |
| **3** | Activar Modo Carácter Especial |
| **7, 4, 1** | Marcar puntos Braille (columna izquierda: 1, 2, 3) |
| **8, 5, 2** | Marcar puntos Braille (columna derecha: 4, 5, 6) |
| **Enter** | Confirmar y agregar carácter |
| **Escape** | Limpiar entrada y reiniciar (vuelve a Modo Letra) |
| **Bloq Mayús** | Sincroniza con botón Block Mayús (solo en Modo Letra) |

💡 **Nota**: Los atajos de teclado solo funcionan cuando la pestaña "Braille → Texto" está activa.

---

## 📁 Estructura del Proyecto

```
Braile_checked_web/
│
├── app.py                        # Aplicación Flask principal
├── requirements.txt              # Dependencias del proyecto
├── test_braille.py               # Suite de 70 casos de prueba (unittest)
│
├── templates/                    # Plantillas HTML
│   ├── index.html               # Traductor bidireccional con Tour
│   ├── contexto.html            # Información sobre Braille
│   └── sobre-nosotros.html      # Acerca del proyecto
│
├── static/
│   └── css/
│       └── style.css            # Estilos CSS (incluye estilos del Tour)
│
├── Documentation/                # Documentación Sphinx
│   ├── source/                  # Archivos fuente (.rst)
│   ├── build/html/              # Documentación generada (HTML)
│   ├── README.md                # Guía de documentación
│   ├── ambiente_de_desarrollo.md
│   ├── analisis_de_cambios_req_1.md
│   ├── analisis_de_cambios_req_2.md
│   ├── casos_de_prueba_unitarios.md
│   ├── casos_de_prueba_general.md
│   ├── diseno_arquitectonico.md
│   ├── manual_de_instalacion.md
│   └── manual_de_usuario.md
│
├── generar_docs.sh              # Script generación docs (Bash)
├── generar_docs.bat             # Script generación docs (Windows)
└── README.md                    # Este archivo
```

---

## 📚 Documentación Técnica

### Generar Documentación con Sphinx

**Windows (CMD):**
```cmd
generar_docs.bat
```

**Git Bash / Linux / Mac:**
```bash
./generar_docs.sh
```

**Manual:**
```bash
python -m sphinx -b html Documentation/source Documentation/build/html
```

### Ver Documentación

```cmd
start Documentation\build\html\index.html
```

La documentación incluye:
- 📖 Manual de instalación y configuración
- 🎯 Manual de usuario con capturas de pantalla
- 🏗️ Diseño arquitectónico del sistema
- 📡 Referencia completa de la API REST
- 🧪 70 casos de prueba (Texto→Braille, Braille→Texto, Bidireccionalidad)
- 🔍 Documentación automática del código (docstrings)

---

## 🧪 Ejecución de Pruebas

El proyecto incluye una suite completa de 70 casos de prueba:

```bash
# Ejecutar todos los tests
python test_braille.py

# Ejecutar con detalle
python -m unittest test_braille.TestBrailleConverter -v

# Ejecutar solo pruebas de Texto → Braille
python -m unittest test_braille.TestBrailleConverter.test_CP0*

# Ejecutar solo pruebas de Braille → Texto
python -m unittest test_braille.TestBrailleConverter.test_CP1*

# Ejecutar solo pruebas de Bidireccionalidad
python -m unittest test_braille.TestBrailleConverter.test_CP2*
```

**Cobertura de pruebas:**
- ✅ 35 casos Texto → Braille (CP-001 a CP-035)
- ✅ 35 casos Braille → Texto (CP-101 a CP-135)
- ✅ 5 casos de Bidireccionalidad (CP-201 a CP-205)

---

## 🎨 Tecnologías Utilizadas

- **Backend**: Flask 3.0.0, Python 3.7+
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Documentación**: Sphinx 8.2.3, sphinx-rtd-theme
- **Exportación**: python-docx 1.1.0
- **Testing**: unittest (Python estándar)
- **Control de versiones**: Git + GitHub

---

## 🌟 Flujo de Trabajo Git

Modelo de ramificación GitFlow:

- **`main`**: Rama de producción (versiones estables)
- **`develop`**: Rama de integración (desarrollo activo)
- **`feature/*`**: Ramas de nuevas funcionalidades
- **`hotfix/*`**: Correcciones críticas en producción
- **`documentation/*`**: Cambios en documentación

### Ejemplo de Flujo

```bash
# Crear feature desde develop
git checkout develop
git pull origin develop
git checkout -b feature/nueva-funcionalidad

# Trabajar y commitear
git add .
git commit -m "feat: añadir validación de caracteres especiales"

# Mantener actualizado
git fetch origin
git rebase origin/develop

# Push y crear Pull Request
git push origin feature/nueva-funcionalidad
```

---

## 🔤 Caracteres Soportados

### Alfabeto Completo
- Letras: a-z (incluyendo ñ)
- Mayúsculas: Prefijo `⠨` (U+2828)
- Números: 0-9 con prefijo `⠼` (U+283C)

### Signos de Puntuación
- Puntuación básica: `.` `,` `;` `:` `-`
- Interrogación: `¿` `?`
- Exclamación: `¡` `!`
- Paréntesis: `(` `)`
- Comillas: `"` `'`

### Caracteres Especiales
- Vocales acentuadas: á é í ó ú
- Diéresis: ü
- Espacios: preservados
- Saltos de línea: preservados

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para colaborar:

1. Fork el repositorio
2. Crear rama feature (`git checkout -b feature/mejora`)
3. Commit cambios (`git commit -m 'feat: descripción'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abrir Pull Request hacia `develop`

### Convenciones de Commits

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bugs
- `docs:` Cambios en documentación
- `test:` Añadir/modificar tests
- `refactor:` Refactorización de código
- `style:` Cambios de formato (no afectan lógica)

---

## 📚 Aprendizajes del Proyecto

Durante el desarrollo de **BraiLator** aprendimos la importancia de considerar las necesidades reales de los usuarios finales desde las etapas tempranas del diseño. 

**Ejemplos clave de iteración centrada en el usuario**:

1. **Botón Block Mayús**: Inicialmente no contemplado, surgió al analizar el flujo de escritura real. Las personas necesitan escribir nombres propios y siglas, por lo que la sincronización automática con la tecla física se volvió esencial.

2. **Tour Interactivo**: Al observar que los usuarios nuevos no entendían intuitivamente el mapeo del numpad, desarrollamos una guía visual contextual que reduce significativamente la curva de aprendizaje.

3. **Validación Contextual**: Implementamos tres modos distintos (letra, número, carácter) porque comprendimos que las personas con discapacidad visual identifican los patrones Braille mediante la disposición táctil específica de puntos en un rectángulo de 2×3.

4. **Exportación en Espejo**: La funcionalidad de invertir el Braille para perforación manual surgió de entender el proceso físico real de creación de material táctil.

Este proyecto reforzó la necesidad de **diseñar con empatía**, validar continuamente con casos de uso reales y documentar exhaustivamente cada decisión técnica para garantizar la mantenibilidad y escalabilidad del sistema.

---

## 📝 Roadmap Futuro

- [ ] Braille Grado 2 (contracciones)
- [ ] Soporte multiidioma (inglés, francés)
- [ ] Impresión directa a impresora Braille
- [ ] Modo oscuro / personalización de temas
- [ ] Integración con lectores de pantalla (JAWS, NVDA)
- [ ] API REST pública con autenticación
- [ ] Aplicación móvil nativa (iOS/Android)
- [ ] Reconocimiento óptico de Braille (OCR)

---

## 👨‍💻 Equipo de Desarrollo

**Grupo 5 - Construcción y Evolución de Software**  
Escuela Politécnica Nacional  
Facultad de Ingeniería de Sistemas

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible con fines **educativos**. Desarrollado como parte del curso de Construcción y Evolución de Software de la EPN.

---

## 📧 Contacto y Soporte

- **Repositorio**: [GitHub - Braile_checked_web](https://github.com/Construccion-y-Evolucion-Pry/Braile_checked_web)
- **Documentación**: `Documentation/build/html/index.html`
- **Issues**: [GitHub Issues](https://github.com/Construccion-y-Evolucion-Pry/Braile_checked_web/issues)

---

<div align="center">

**Desarrollado con 💙 para mejorar la accesibilidad**

*BraiLator · Inclusión y accesibilidad digital*

</div>