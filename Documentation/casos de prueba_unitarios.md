# Documento de Casos de Prueba
## Sistema de Traducción Texto a Braille

**Proyecto:** Construcción y Evolución de Software  
**Versión:** 1.0  
**Fecha:** Noviembre 2025

---

## 1. Introducción

Este documento detalla los casos de prueba diseñados para validar la funcionalidad del sistema de transcripción de texto a Braille español. Los casos de prueba cubren todos los requisitos especificados en el documento de indicaciones del proyecto.

## 2. Objetivos de las Pruebas

- Verificar la correcta transcripción del alfabeto español (a-z) a Braille
- Validar el manejo de mayúsculas con el prefijo correspondiente
- Comprobar la conversión de números y decimales
- Validar caracteres especiales del español (ñ, vocales acentuadas, ü)
- Verificar signos de puntuación y símbolos
- Probar casos límite y combinaciones complejas

## 3. Casos de Prueba

### 3.1 Alfabeto Básico

#### CP-001: Primera Serie (a-j) Minúsculas
- **Descripción:** Verificar conversión de letras de la primera serie
- **Entrada:** `abcdefghij`
- **Resultado Esperado:** `⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚`
- **Requisito:** Primera serie matriz según especificación
- **Prioridad:** Alta

#### CP-002: Segunda Serie (k-t) Minúsculas
- **Descripción:** Verificar conversión de letras de la segunda serie (primera serie + punto 3)
- **Entrada:** `klmnopqrst`
- **Resultado Esperado:** `⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞`
- **Requisito:** Segunda serie según especificación
- **Prioridad:** Alta

#### CP-003: Tercera Serie (u-z) Minúsculas
- **Descripción:** Verificar conversión de letras de la tercera serie (primera serie + puntos 3 y 6)
- **Entrada:** `uvxyz`
- **Resultado Esperado:** `⠥⠧⠭⠽⠵`
- **Requisito:** Tercera serie según especificación
- **Prioridad:** Alta

#### CP-004: Letra W
- **Descripción:** Verificar conversión de letra w (carácter adicional)
- **Entrada:** `w`
- **Resultado Esperado:** `⠺`
- **Requisito:** Letras adicionales
- **Prioridad:** Media

#### CP-035: Alfabeto Completo
- **Descripción:** Verificar alfabeto completo en minúsculas
- **Entrada:** `abcdefghijklmnopqrstuvwxyz`
- **Resultado Esperado:** `⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵`
- **Requisito:** Alfabeto completo
- **Prioridad:** Alta

### 3.2 Mayúsculas

#### CP-005: Mayúscula Simple
- **Descripción:** Verificar conversión de una letra mayúscula con prefijo ⠨
- **Entrada:** `A`
- **Resultado Esperado:** `⠨⠁`
- **Requisito:** Manejo de mayúsculas
- **Prioridad:** Alta

#### CP-006: Palabra con Mayúscula Inicial
- **Descripción:** Verificar conversión de palabra con primera letra mayúscula
- **Entrada:** `Hola`
- **Resultado Esperado:** `⠨⠓⠕⠇⠁`
- **Requisito:** Mayúsculas en contexto
- **Prioridad:** Alta

#### CP-007: Todas Mayúsculas
- **Descripción:** Verificar que cada mayúscula recibe su prefijo
- **Entrada:** `CASA`
- **Resultado Esperado:** `⠨⠉⠨⠁⠨⠎⠨⠁`
- **Requisito:** Texto en mayúsculas
- **Prioridad:** Media

### 3.3 Caracteres Especiales del Español

#### CP-008: Letra Ñ
- **Descripción:** Verificar conversión de ñ
- **Entrada:** `niño`
- **Resultado Esperado:** `⠝⠊⠻⠕`
- **Requisito:** Caracteres especiales español
- **Prioridad:** Alta

#### CP-009: Vocales Acentuadas
- **Descripción:** Verificar conversión de todas las vocales con tilde
- **Entrada:** `áéíóú`
- **Resultado Esperado:** `⠷⠮⠌⠬⠾`
- **Requisito:** Vocales acentuadas
- **Prioridad:** Alta

#### CP-010: U con Diéresis
- **Descripción:** Verificar conversión de ü
- **Entrada:** `güe`
- **Resultado Esperado:** `⠛⠳⠑`
- **Requisito:** Caracteres especiales español
- **Prioridad:** Media

#### CP-011: Mayúscula con Tilde
- **Descripción:** Verificar combinación de mayúscula inicial con vocal acentuada
- **Entrada:** `María`
- **Resultado Esperado:** `⠨⠍⠷⠗⠊⠁`
- **Requisito:** Mayúsculas + vocales acentuadas
- **Prioridad:** Alta

### 3.4 Números

#### CP-012: Número Simple
- **Descripción:** Verificar conversión de un dígito con prefijo ⠼
- **Entrada:** `5`
- **Resultado Esperado:** `⠼⠑`
- **Requisito:** Escritura de números
- **Prioridad:** Alta

#### CP-013: Número Múltiples Dígitos
- **Descripción:** Verificar que el prefijo ⠼ se coloca solo al inicio
- **Entrada:** `2024`
- **Resultado Esperado:** `⠼⠃⠚⠃⠙`
- **Requisito:** Cantidades de dos o más cifras
- **Prioridad:** Alta

#### CP-014: Número Decimal con Punto
- **Descripción:** Verificar que punto decimal se incluye en el número
- **Entrada:** `123.45`
- **Resultado Esperado:** `⠼⠁⠃⠉⠲⠙⠑`
- **Requisito:** Números con punto decimal
- **Prioridad:** Alta

#### CP-015: Número Decimal con Coma
- **Descripción:** Verificar que coma decimal se incluye en el número
- **Entrada:** `3,14`
- **Resultado Esperado:** `⠼⠉⠂⠁⠙`
- **Requisito:** Números con coma decimal
- **Prioridad:** Alta

#### CP-016: Secuencia 1-0
- **Descripción:** Verificar conversión de todos los dígitos (1 al 0)
- **Entrada:** `1234567890`
- **Resultado Esperado:** `⠼⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚`
- **Requisito:** Los diez dígitos de la primera serie
- **Prioridad:** Media

#### CP-034: Números Separados
- **Descripción:** Verificar que números separados por espacios tienen prefijos independientes
- **Entrada:** `1 2 3`
- **Resultado Esperado:** `⠼⠁⠀⠼⠃⠀⠼⠉`
- **Requisito:** Números separados con espacios
- **Prioridad:** Media

### 3.5 Signos de Puntuación

#### CP-017: Punto Final
- **Descripción:** Verificar conversión de punto
- **Entrada:** `fin.`
- **Resultado Esperado:** `⠋⠊⠝⠲`
- **Requisito:** Signos básicos
- **Prioridad:** Alta

#### CP-018: Coma Separadora
- **Descripción:** Verificar coma usada como separador (no decimal)
- **Entrada:** `hola, mundo`
- **Resultado Esperado:** `⠓⠕⠇⠁⠂⠀⠍⠥⠝⠙⠕`
- **Requisito:** Signos básicos
- **Prioridad:** Alta

#### CP-019: Signos de Interrogación
- **Descripción:** Verificar apertura y cierre de interrogación
- **Entrada:** `¿cómo?`
- **Resultado Esperado:** `⠦⠉⠬⠍⠕⠦`
- **Requisito:** Signos básicos
- **Prioridad:** Alta

#### CP-020: Signos de Exclamación
- **Descripción:** Verificar apertura y cierre de exclamación
- **Entrada:** `¡hola!`
- **Resultado Esperado:** `⠖⠓⠕⠇⠁⠖`
- **Requisito:** Signos básicos
- **Prioridad:** Alta

#### CP-021: Paréntesis
- **Descripción:** Verificar conversión de paréntesis de apertura y cierre
- **Entrada:** `(texto)`
- **Resultado Esperado:** `⠐⠣⠞⠑⠭⠞⠕⠐⠜`
- **Requisito:** Signos básicos
- **Prioridad:** Media

#### CP-022: Dos Puntos y Punto y Coma
- **Descripción:** Verificar conversión de : y ;
- **Entrada:** `uno: dos; tres`
- **Resultado Esperado:** `⠥⠝⠕⠒⠀⠙⠕⠎⠆⠀⠞⠗⠑⠎`
- **Requisito:** Signos básicos
- **Prioridad:** Media

#### CP-023: Guion
- **Descripción:** Verificar conversión de guion
- **Entrada:** `bien-estar`
- **Resultado Esperado:** `⠃⠊⠑⠝⠤⠑⠎⠞⠁⠗`
- **Requisito:** Signos básicos
- **Prioridad:** Media

### 3.6 Espacios y Formato

#### CP-024: Espacios en Blanco
- **Descripción:** Verificar preservación de espacios
- **Entrada:** `dos palabras`
- **Resultado Esperado:** `⠙⠕⠎⠀⠏⠁⠇⠁⠃⠗⠁⠎`
- **Requisito:** Espacios en blanco
- **Prioridad:** Alta

#### CP-025: Múltiples Espacios
- **Descripción:** Verificar que múltiples espacios se preservan
- **Entrada:** `a  b`
- **Resultado Esperado:** `⠁⠀⠀⠃`
- **Requisito:** Preservación de formato
- **Prioridad:** Baja

#### CP-026: Salto de Línea
- **Descripción:** Verificar preservación de saltos de línea
- **Entrada:** `línea1 línea2`
- **Resultado Esperado:** `⠇⠌⠝⠑⠁⠁ ⠇⠌⠝⠑⠁⠃`
- **Requisito:** Preservación de formato
- **Prioridad:** Media

### 3.7 Frases Complejas

#### CP-027: Frase Simple Completa
- **Descripción:** Verificar conversión de frase con mayúscula, espacios y punto
- **Entrada:** `Hola mundo.`
- **Resultado Esperado:** `⠨⠓⠕⠇⠁⠀⠍⠥⠝⠙⠕⠲`
- **Requisito:** Integración de elementos
- **Prioridad:** Alta

#### CP-028: Texto con Números y Letras
- **Descripción:** Verificar mezcla de texto y números
- **Entrada:** `Año 2024`
- **Resultado Esperado:** `⠨⠁⠻⠕⠀⠼⠃⠚⠃⠙`
- **Requisito:** Texto mezclado
- **Prioridad:** Alta

#### CP-029: Oración Interrogativa
- **Descripción:** Verificar oración interrogativa completa
- **Entrada:** `¿Cuál es tu número?`
- **Resultado Esperado:** `⠦⠨⠉⠥⠷⠇⠀⠑⠎⠀⠞⠥⠀⠝⠳⠍⠑⠗⠕⠦`
- **Requisito:** Generación de señalética
- **Prioridad:** Alta

#### CP-030: Señalética Ascensor
- **Descripción:** Verificar señalética típica para ascensores
- **Entrada:** `Piso 3`
- **Resultado Esperado:** `⠨⠏⠊⠎⠕⠀⠼⠉`
- **Requisito:** Generación de señalética braille
- **Prioridad:** Alta

#### CP-031: Precio con Decimal
- **Descripción:** Verificar formato de precios
- **Entrada:** `precio: 19.99`
- **Resultado Esperado:** `⠏⠗⠑⠉⠊⠕⠒⠀⠼⠁⠊⠲⠊⠊`
- **Requisito:** Números decimales en contexto
- **Prioridad:** Media

### 3.8 Casos Límite

#### CP-032: Texto Vacío
- **Descripción:** Verificar manejo de entrada vacía
- **Entrada:** `` (cadena vacía)
- **Resultado Esperado:** `` (cadena vacía)
- **Requisito:** Manejo de casos límite
- **Prioridad:** Media

#### CP-033: Solo Espacios
- **Descripción:** Verificar entrada con solo espacios
- **Entrada:** `   ` (tres espacios)
- **Resultado Esperado:** `⠀⠀⠀`
- **Requisito:** Manejo de casos límite
- **Prioridad:** Baja

---

## 4. Instrucciones de Ejecución

### 4.1 Requisitos Previos
- Python 3.7 o superior
- Módulo `unittest` (incluido en Python estándar)
- Archivo `app.py` con la función `texto_a_braille()`

### 4.2 Ejecución de Pruebas

```bash
# Ejecutar todas las pruebas
python test_braille_converter.py

# Ejecutar con más detalle
python -m unittest test_braille_converter.TestBrailleConverter -v

# Ejecutar un caso específico
python -m unittest test_braille_converter.TestBrailleConverter.test_CP001_primera_serie_minusculas
```



### Plantilla de Análisis de Fallos

**ID Caso:** CP-XXX  
**Fecha de Detección:**  
**Descripción del Fallo:**  
**Análisis de Causa:**  
**Solución Aplicada:**  
**Fecha de Re-ejecución:**  
**Resultado Final:**

---

## 6. Métricas de Calidad

- **Total de Casos de Prueba:** 35
- **Casos de Prioridad Alta:** 23
- **Casos de Prioridad Media:** 10
- **Casos de Prioridad Baja:** 2

### Cobertura de Requisitos

| Requisito | Casos de Prueba | Cobertura |
|-----------|-----------------|-----------|
| Alfabeto español (a-z) | CP-001 a CP-004, CP-035 | 100% |
| Mayúsculas | CP-005 a CP-007, CP-011 | 100% |
| Números | CP-012 a CP-016, CP-034 | 100% |
| Decimales | CP-014, CP-015, CP-031 | 100% |
| Caracteres especiales | CP-008 a CP-011 | 100% |
| Signos de puntuación | CP-017 a CP-023 | 100% |
| Señalética | CP-027 a CP-031 | 100% |

---

## 7. Conclusiones

Este conjunto de casos de prueba garantiza la validación completa de los requisitos del primer bimestre del proyecto. Cada caso está diseñado para verificar aspectos específicos de la transcripción Braille según el estándar español definido en las indicaciones del proyecto.

---
