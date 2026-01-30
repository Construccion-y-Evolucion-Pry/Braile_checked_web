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

# Documento de Casos de Prueba
## Sistema de Traducción Bidireccional Texto-Braille

## 1. Introducción

Este documento detalla los casos de prueba diseñados para validar la funcionalidad bidireccional del sistema de transcripción entre texto español y Braille. Los casos de prueba cubren:

- **Conversión Texto → Braille**: Transcripción de texto en español a Braille
- **Conversión Braille → Texto**: Transcripción inversa de Braille a texto español

Todos los casos están basados en las especificaciones del proyecto y el estándar Braille español.

## 2. Objetivos de las Pruebas

### 2.1 Conversión Texto → Braille
- Verificar la correcta transcripción del alfabeto español (a-z) a Braille
- Validar el manejo de mayúsculas con el prefijo correspondiente
- Comprobar la conversión de números y decimales
- Validar caracteres especiales del español (ñ, vocales acentuadas, ü)
- Verificar signos de puntuación y símbolos
- Probar casos límite y combinaciones complejas

### 2.2 Conversión Braille → Texto
- Verificar la correcta interpretación de caracteres Braille a letras españolas
- Validar el reconocimiento de prefijos de mayúsculas
- Comprobar la conversión de números con prefijos
- Validar la interpretación de caracteres especiales del español
- Verificar el reconocimiento de signos de puntuación
- Probar la preservación de espacios y formato
- Comprobar la bidireccionalidad (texto → braille → texto = texto original)

## 3. Casos de Prueba: Texto a Braille

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
- **Entrada:** `línea1\nlínea2`
- **Resultado Esperado:** `⠇⠌⠝⠑⠁⠼⠁\n⠇⠌⠝⠑⠁⠼⠃`
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
- **Resultado Esperado:** `⠦⠨⠉⠥⠷⠇⠀⠑⠎⠀⠞⠥⠀⠝⠾⠍⠑⠗⠕⠦`
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

## 4. Casos de Prueba: Braille a Texto (NUEVOS)

### 4.1 Alfabeto Básico Inverso

#### CP-101: Primera Serie Braille a Texto
- **Descripción:** Verificar conversión inversa de primera serie Braille
- **Entrada:** `⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚`
- **Resultado Esperado:** `abcdefghij`
- **Requisito:** Conversión inversa alfabeto
- **Prioridad:** Alta

#### CP-102: Segunda Serie Braille a Texto
- **Descripción:** Verificar conversión inversa de segunda serie Braille
- **Entrada:** `⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞`
- **Resultado Esperado:** `klmnopqrst`
- **Requisito:** Conversión inversa alfabeto
- **Prioridad:** Alta

#### CP-103: Tercera Serie Braille a Texto
- **Descripción:** Verificar conversión inversa de tercera serie Braille
- **Entrada:** `⠥⠧⠭⠽⠵`
- **Resultado Esperado:** `uvxyz`
- **Requisito:** Conversión inversa alfabeto
- **Prioridad:** Alta

#### CP-104: Letra W Braille a Texto
- **Descripción:** Verificar conversión inversa de letra w
- **Entrada:** `⠺`
- **Resultado Esperado:** `w`
- **Requisito:** Caracteres adicionales inversos
- **Prioridad:** Media

#### CP-135: Alfabeto Completo Braille a Texto
- **Descripción:** Verificar alfabeto completo Braille a minúsculas
- **Entrada:** `⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵`
- **Resultado Esperado:** `abcdefghijklmnopqrstuvwxyz`
- **Requisito:** Alfabeto completo inverso
- **Prioridad:** Alta

### 4.2 Mayúsculas Inversas

#### CP-105: Mayúscula Simple Braille a Texto
- **Descripción:** Verificar reconocimiento de prefijo de mayúscula
- **Entrada:** `⠨⠁`
- **Resultado Esperado:** `A`
- **Requisito:** Interpretación de mayúsculas
- **Prioridad:** Alta

#### CP-106: Palabra con Mayúscula Inicial Inversa
- **Descripción:** Verificar conversión de palabra con mayúscula inicial
- **Entrada:** `⠨⠓⠕⠇⠁`
- **Resultado Esperado:** `Hola`
- **Requisito:** Mayúsculas en contexto inversas
- **Prioridad:** Alta

#### CP-107: Todas Mayúsculas Inversas
- **Descripción:** Verificar reconocimiento de múltiples prefijos de mayúsculas
- **Entrada:** `⠨⠉⠨⠁⠨⠎⠨⠁`
- **Resultado Esperado:** `CASA`
- **Requisito:** Texto en mayúsculas inverso
- **Prioridad:** Media

### 4.3 Caracteres Especiales Inversos

#### CP-108: Letra Ñ Braille a Texto
- **Descripción:** Verificar conversión inversa de ñ
- **Entrada:** `⠝⠊⠻⠕`
- **Resultado Esperado:** `niño`
- **Requisito:** Caracteres especiales inversos
- **Prioridad:** Alta

#### CP-109: Vocales Acentuadas Inversas
- **Descripción:** Verificar conversión inversa de vocales acentuadas
- **Entrada:** `⠷⠮⠌⠬⠾`
- **Resultado Esperado:** `áéíóú`
- **Requisito:** Vocales acentuadas inversas
- **Prioridad:** Alta

#### CP-110: U con Diéresis Inversa
- **Descripción:** Verificar conversión inversa de ü
- **Entrada:** `⠛⠳⠑`
- **Resultado Esperado:** `güe`
- **Requisito:** Caracteres especiales inversos
- **Prioridad:** Media

#### CP-111: Palabra con Mayúscula y Tilde Inversa
- **Descripción:** Verificar combinación de mayúscula y vocal acentuada
- **Entrada:** `⠨⠍⠷⠗⠊⠁`
- **Resultado Esperado:** `María`
- **Requisito:** Mayúsculas + vocales inversas
- **Prioridad:** Alta

### 4.4 Números Inversos

#### CP-112: Número Simple Braille a Texto
- **Descripción:** Verificar reconocimiento de prefijo numérico
- **Entrada:** `⠼⠑`
- **Resultado Esperado:** `5`
- **Requisito:** Números inversos
- **Prioridad:** Alta

#### CP-113: Número Múltiples Dígitos Inverso
- **Descripción:** Verificar conversión de número con prefijo único
- **Entrada:** `⠼⠃⠚⠃⠙`
- **Resultado Esperado:** `2024`
- **Requisito:** Números múltiples dígitos inversos
- **Prioridad:** Alta

#### CP-114: Número Decimal con Punto Inverso
- **Descripción:** Verificar conversión de decimal con punto
- **Entrada:** `⠼⠁⠃⠉⠲⠙⠑`
- **Resultado Esperado:** `123.45`
- **Requisito:** Números decimales inversos
- **Prioridad:** Alta

#### CP-115: Número Decimal con Coma Inverso
- **Descripción:** Verificar conversión de decimal con coma
- **Entrada:** `⠼⠉⠂⠁⠙`
- **Resultado Esperado:** `3,14`
- **Requisito:** Números decimales inversos
- **Prioridad:** Alta

#### CP-116: Secuencia 1-0 Inversa
- **Descripción:** Verificar conversión de todos los dígitos
- **Entrada:** `⠼⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚`
- **Resultado Esperado:** `1234567890`
- **Requisito:** Dígitos completos inversos
- **Prioridad:** Media

#### CP-134: Números Separados Inversos
- **Descripción:** Verificar reconocimiento de múltiples prefijos numéricos
- **Entrada:** `⠼⠁⠀⠼⠃⠀⠼⠉`
- **Resultado Esperado:** `1 2 3`
- **Requisito:** Números separados inversos
- **Prioridad:** Media

### 4.5 Signos de Puntuación Inversos

#### CP-117: Punto Final Inverso
- **Descripción:** Verificar conversión de punto Braille
- **Entrada:** `⠋⠊⠝⠲`
- **Resultado Esperado:** `fin.`
- **Requisito:** Signos básicos inversos
- **Prioridad:** Alta

#### CP-118: Coma Separadora Inversa
- **Descripción:** Verificar conversión de coma no decimal
- **Entrada:** `⠓⠕⠇⠁⠂⠀⠍⠥⠝⠙⠕`
- **Resultado Esperado:** `hola, mundo`
- **Requisito:** Signos básicos inversos
- **Prioridad:** Alta

#### CP-119: Signos de Interrogación Inversos
- **Descripción:** Verificar conversión de interrogación Braille
- **Entrada:** `⠦⠉⠬⠍⠕⠦`
- **Resultado Esperado:** `¿cómo?`
- **Requisito:** Signos básicos inversos
- **Prioridad:** Alta

#### CP-120: Signos de Exclamación Inversos
- **Descripción:** Verificar conversión de exclamación Braille
- **Entrada:** `⠖⠓⠕⠇⠁⠖`
- **Resultado Esperado:** `¡hola!`
- **Requisito:** Signos básicos inversos
- **Prioridad:** Alta

#### CP-121: Paréntesis Inversos
- **Descripción:** Verificar conversión de paréntesis Braille
- **Entrada:** `⠐⠣⠞⠑⠭⠞⠕⠐⠜`
- **Resultado Esperado:** `(texto)`
- **Requisito:** Signos básicos inversos
- **Prioridad:** Media

#### CP-122: Dos Puntos y Punto y Coma Inversos
- **Descripción:** Verificar conversión de : y ; Braille
- **Entrada:** `⠥⠝⠕⠒⠀⠙⠕⠎⠆⠀⠞⠗⠑⠎`
- **Resultado Esperado:** `uno: dos; tres`
- **Requisito:** Signos básicos inversos
- **Prioridad:** Media

#### CP-123: Guion Inverso
- **Descripción:** Verificar conversión de guion Braille
- **Entrada:** `⠃⠊⠑⠝⠤⠑⠎⠞⠁⠗`
- **Resultado Esperado:** `bien-estar`
- **Requisito:** Signos básicos inversos
- **Prioridad:** Media

### 4.6 Espacios y Formato Inversos

#### CP-124: Espacios en Blanco Inversos
- **Descripción:** Verificar preservación de espacios Braille
- **Entrada:** `⠙⠕⠎⠀⠏⠁⠇⠁⠃⠗⠁⠎`
- **Resultado Esperado:** `dos palabras`
- **Requisito:** Espacios en blanco inversos
- **Prioridad:** Alta

#### CP-125: Múltiples Espacios Inversos
- **Descripción:** Verificar preservación de múltiples espacios
- **Entrada:** `⠁⠀⠀⠃`
- **Resultado Esperado:** `a  b`
- **Requisito:** Preservación de formato inverso
- **Prioridad:** Baja

#### CP-126: Salto de Línea Inverso
- **Descripción:** Verificar preservación de saltos de línea
- **Entrada:** `⠇⠌⠝⠑⠁⠼⠁\n⠇⠌⠝⠑⠁⠼⠃`
- **Resultado Esperado:** `línea1\nlínea2`
- **Requisito:** Preservación de formato inverso
- **Prioridad:** Media

### 4.7 Frases Complejas Inversas

#### CP-127: Frase Simple Completa Inversa
- **Descripción:** Verificar conversión completa de frase
- **Entrada:** `⠨⠓⠕⠇⠁⠀⠍⠥⠝⠙⠕⠲`
- **Resultado Esperado:** `Hola mundo.`
- **Requisito:** Integración de elementos inversas
- **Prioridad:** Alta

#### CP-128: Texto con Números y Letras Inverso
- **Descripción:** Verificar mezcla de texto y números
- **Entrada:** `⠨⠁⠻⠕⠀⠼⠃⠚⠃⠙`
- **Resultado Esperado:** `Año 2024`
- **Requisito:** Texto mezclado inverso
- **Prioridad:** Alta

#### CP-129: Oración Interrogativa Inversa
- **Descripción:** Verificar oración interrogativa completa
- **Entrada:** `⠦⠨⠉⠥⠷⠇⠀⠑⠎⠀⠞⠥⠀⠝⠾⠍⠑⠗⠕⠦`
- **Resultado Esperado:** `¿Cuál es tu número?`
- **Requisito:** Frases complejas inversas
- **Prioridad:** Alta

#### CP-130: Señalética Ascensor Inversa
- **Descripción:** Verificar lectura de señalética Braille
- **Entrada:** `⠨⠏⠊⠎⠕⠀⠼⠉`
- **Resultado Esperado:** `Piso 3`
- **Requisito:** Señalética inversa
- **Prioridad:** Alta

#### CP-131: Precio con Decimal Inverso
- **Descripción:** Verificar formato de precios inverso
- **Entrada:** `⠏⠗⠑⠉⠊⠕⠒⠀⠼⠁⠊⠲⠊⠊`
- **Resultado Esperado:** `precio: 19.99`
- **Requisito:** Números decimales contexto inverso
- **Prioridad:** Media

### 4.8 Casos Límite Inversos

#### CP-132: Braille Vacío
- **Descripción:** Verificar manejo de entrada Braille vacía
- **Entrada:** `` (cadena vacía)
- **Resultado Esperado:** `` (cadena vacía)
- **Requisito:** Manejo de casos límite inversos
- **Prioridad:** Media

#### CP-133: Solo Espacios Braille
- **Descripción:** Verificar entrada con solo espacios Braille
- **Entrada:** `⠀⠀⠀` (tres espacios Braille)
- **Resultado Esperado:** `   ` (tres espacios)
- **Requisito:** Manejo de casos límite inversos
- **Prioridad:** Baja

---

## 5. Casos de Prueba de Bidireccionalidad

### 5.1 Verificación de Ida y Vuelta

#### CP-201: Bidireccionalidad Alfabeto
- **Descripción:** Verificar que texto → braille → texto = texto original
- **Entrada:** `abcdefghijklmnopqrstuvwxyz`
- **Proceso:** 
  1. Convertir a Braille: `⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵`
  2. Convertir de vuelta a texto: `abcdefghijklmnopqrstuvwxyz`
- **Resultado Esperado:** Texto original = Texto final
- **Requisito:** Bidireccionalidad completa
- **Prioridad:** Alta

#### CP-202: Bidireccionalidad Frase Compleja
- **Descripción:** Verificar ida y vuelta con frase compleja
- **Entrada:** `¿Hola mundo! Año 2024.`
- **Proceso:** texto → braille → texto
- **Resultado Esperado:** Texto idéntico al original
- **Requisito:** Bidireccionalidad en contexto
- **Prioridad:** Alta

#### CP-203: Bidireccionalidad Números y Decimales
- **Descripción:** Verificar ida y vuelta con números
- **Entrada:** `El precio es 19.99 o 3,14`
- **Proceso:** texto → braille → texto
- **Resultado Esperado:** Texto idéntico al original
- **Requisito:** Bidireccionalidad numérica
- **Prioridad:** Alta

#### CP-204: Bidireccionalidad Caracteres Especiales
- **Descripción:** Verificar ida y vuelta con ñ, tildes y diéresis
- **Entrada:** `El niño español güe áéíóú`
- **Proceso:** texto → braille → texto
- **Resultado Esperado:** Texto idéntico al original
- **Requisito:** Bidireccionalidad caracteres especiales
- **Prioridad:** Alta

#### CP-205: Bidireccionalidad Mayúsculas Mixtas
- **Descripción:** Verificar ida y vuelta con mayúsculas
- **Entrada:** `María González VIVE en España`
- **Proceso:** texto → braille → texto
- **Resultado Esperado:** Texto idéntico al original
- **Requisito:** Bidireccionalidad mayúsculas
- **Prioridad:** Alta

---

## 6. Instrucciones de Ejecución

### 6.1 Requisitos Previos
- Python 3.7 o superior
- Módulo `unittest` (incluido en Python estándar)
- Archivo `app.py` con las funciones:
  - `texto_a_braille(texto: str) -> str`
  - `braille_a_texto(braille: str) -> str`

### 6.2 Ejecución de Pruebas

```bash
# Ejecutar todas las pruebas (texto a braille y braille a texto)
python test_braille.py

# Ejecutar con más detalle
python -m unittest test_braille.TestBrailleConverter -v

# Ejecutar solo pruebas de texto a braille
python -m unittest test_braille.TestBrailleConverter.test_CP0*

# Ejecutar solo pruebas de braille a texto
python -m unittest test_braille.TestBrailleConverter.test_CP1*

# Ejecutar solo pruebas de bidireccionalidad
python -m unittest test_braille.TestBrailleConverter.test_CP2*

# Ejecutar un caso específico
python -m unittest test_braille.TestBrailleConverter.test_CP101_primera_serie_braille_a_texto
```

### 6.3 Interpretación de Resultados

- **OK**: El caso de prueba pasó exitosamente
- **FAIL**: El caso de prueba falló (resultado diferente al esperado)
- **ERROR**: Se produjo un error durante la ejecución

---

## 7. Plantilla de Análisis de Fallos

**ID Caso:** CP-XXX  
**Fecha de Detección:**  
**Tipo de Prueba:** [Texto→Braille | Braille→Texto | Bidireccionalidad]  
**Descripción del Fallo:**  
**Entrada Usada:**  
**Resultado Obtenido:**  
**Resultado Esperado:**  
**Análisis de Causa:**  
**Solución Aplicada:**  
**Fecha de Re-ejecución:**  
**Resultado Final:**

---

## 8. Métricas de Calidad

### 8.1 Resumen de Casos de Prueba

- **Total de Casos de Prueba:** 70
  - Texto a Braille: 35 casos (CP-001 a CP-035)
  - Braille a Texto: 35 casos (CP-101 a CP-135)
  - Bidireccionalidad: 5 casos (CP-201 a CP-205)

### 8.2 Distribución por Prioridad

| Prioridad | Texto→Braille | Braille→Texto | Bidireccionalidad | Total |
|-----------|---------------|---------------|-------------------|-------|
| Alta      | 23            | 23            | 5                 | 51    |
| Media     | 10            | 10            | 0                 | 20    |
| Baja      | 2             | 2             | 0                 | 4     |

### 8.3 Cobertura de Requisitos

| Requisito | Casos Texto→Braille | Casos Braille→Texto | Cobertura |
|-----------|---------------------|---------------------|-----------|
| Alfabeto español (a-z) | CP-001 a CP-004, CP-035 | CP-101 a CP-104, CP-135 | 100% |
| Mayúsculas | CP-005 a CP-007, CP-011 | CP-105 a CP-107, CP-111 | 100% |
| Números | CP-012 a CP-016, CP-034 | CP-112 a CP-116, CP-134 | 100% |
| Decimales | CP-014, CP-015, CP-031 | CP-114, CP-115, CP-131 | 100% |
| Caracteres especiales | CP-008 a CP-011 | CP-108 a CP-111 | 100% |
| Signos de puntuación | CP-017 a CP-023 | CP-117 a CP-123 | 100% |
| Señalética | CP-027 a CP-031 | CP-127 a CP-131 | 100% |
| Bidireccionalidad | - | - | CP-201 a CP-205 | 100% |

---

## 9. Conclusiones

Este conjunto de casos de prueba garantiza la validación completa y bidireccional del sistema de transcripción Braille. La inclusión de:

1. **35 casos de Texto a Braille**: Validan la correcta conversión desde texto español estándar
2. **35 casos de Braille a Texto**: Validan la conversión inversa, asegurando que el sistema puede leer Braille
3. **5 casos de Bidireccionalidad**: Garantizan que las conversiones son reversibles y consistentes

Cada caso está diseñado para verificar aspectos específicos de la transcripción según el estándar Braille español, cubriendo todos los requisitos del proyecto y asegurando que el sistema funciona correctamente en ambas direcciones.

---

## 10. Historial de Versiones

| Versión | Fecha | Descripción de Cambios |
|---------|-------|------------------------|
| 1.0 | Noviembre 2025 | Versión inicial con 35 casos de prueba (Texto a Braille) |
| 2.0 | Enero 2026 | Agregados 35 casos de Braille a Texto + 5 casos de Bidireccionalidad |

---