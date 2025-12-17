from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Diccionario con letras (incluye tildes, ñ y signos adicionales)
BRAILLE_MAP = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵',

    # Caracteres especiales del español
    'ñ': '⠻',

    # Vocales con tilde
    'á': '⠷',
    'é': '⠮',
    'í': '⠌',
    'ó': '⠬',
    'ú': '⠾',

    'ü': '⠳',

    # Espacios, signos y operadores
    ' ': '⠀',
    '.': '⠄', ',': '⠂', ';': '⠆', ':': '⠒',
    '!': '⠖', '¡': '⠖', '?': '⠦', '-': '⠤',
    '(': '⠐⠣', ')': '⠐⠜', '¿': '⠦',
    '+': '⠖', '*': '⠦', '=': '⠶', '/': '⠲',
    '\n': '\n'  # Preservar saltos de línea
}

# Números en braille español (1–0)
BRAILLE_NUMBERS = {
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
}

# Signos especiales
SIGNO_MAYUSCULA = '⠨'  # Puntos 4-6
SIGNO_NUMERO = '⠼'     # Puntos 3-4-5-6

# Crear diccionario inverso para Braille → Texto
BRAILLE_TO_TEXT = {v: k for k, v in BRAILLE_MAP.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in BRAILLE_NUMBERS.items()}


def texto_a_braille(texto):
    resultado = []
    numero_activo = False
    numero_buffer = ''
    i = 0

    while i < len(texto):
        caracter = texto[i]
        
        # Detectar si es un dígito
        if caracter.isdigit():
            if not numero_activo:
                numero_activo = True
                numero_buffer = ''
            numero_buffer += BRAILLE_NUMBERS[caracter]
            
        # Si estamos en modo número y encontramos punto o coma decimal
        elif numero_activo and caracter in ['.', ',']:
            numero_buffer += BRAILLE_MAP[caracter]
            
        else:
            # Finalizar el número si estaba activo
            if numero_activo:
                resultado.append(SIGNO_NUMERO + numero_buffer)
                numero_buffer = ''
                numero_activo = False
            
            if caracter == '\n':
                resultado.append('\n')

            # Procesar mayúsculas
            elif caracter.isupper():
                char_lower = caracter.lower()
                if char_lower in BRAILLE_MAP:
                    resultado.append(SIGNO_MAYUSCULA + BRAILLE_MAP[char_lower])
                else:
                    resultado.append(caracter)
                    
            # Otros caracteres (minúsculas, tildes, signos, etc.)
            elif caracter.lower() in BRAILLE_MAP:
                resultado.append(BRAILLE_MAP[caracter.lower()])
            else:
                # Dejar caracteres desconocidos tal cual
                resultado.append(caracter)
        
        i += 1

    # Si terminó en número
    if numero_activo:
        resultado.append(SIGNO_NUMERO + numero_buffer)

    return ''.join(resultado)


def braille_a_texto(braille_texto):
    resultado = []
    i = 0
    mayuscula_siguiente = False
    numero_activo = False
    
    while i < len(braille_texto):
        caracter = braille_texto[i]
        
        # Preservar saltos de línea
        if caracter == '\n':
            resultado.append('\n')
            i += 1
            continue
        
        # Detectar signo de mayúscula
        if caracter == SIGNO_MAYUSCULA:
            mayuscula_siguiente = True
            i += 1
            continue
        
        # Detectar signo de número
        if caracter == SIGNO_NUMERO:
            numero_activo = True
            i += 1
            continue
        
        # Si estamos en modo número
        if numero_activo:
            if caracter in BRAILLE_TO_NUMBER:
                resultado.append(BRAILLE_TO_NUMBER[caracter])
                i += 1
                continue
            elif caracter in [BRAILLE_MAP['.'], BRAILLE_MAP[',']]:
                # Permitir punto o coma en números
                if caracter == BRAILLE_MAP['.']:
                    resultado.append('.')
                else:
                    resultado.append(',')
                i += 1
                continue
            else:
                # Salir del modo número si encontramos algo que no es dígito
                numero_activo = False
        
        # Convertir carácter braille a texto
        if caracter in BRAILLE_TO_TEXT:
            letra = BRAILLE_TO_TEXT[caracter]
            
            # Aplicar mayúscula si es necesario
            if mayuscula_siguiente and letra.isalpha():
                resultado.append(letra.upper())
                mayuscula_siguiente = False
            else:
                resultado.append(letra)
        else:
            # Si no está en el diccionario, dejarlo tal cual
            resultado.append(caracter)
        
        i += 1
    
    return ''.join(resultado)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contexto')
def contexto():
    return render_template('contexto.html')


@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('sobre-nosotros.html')


@app.route('/convertir', methods=['POST'])
def convertir():
    data = request.get_json()
    texto = data.get('texto', '')

    if not texto:
        return jsonify({'error': 'No se proporcionó texto'}), 400

    braille = texto_a_braille(texto)

    return jsonify({
        'texto_original': texto,
        'texto_braille': braille
    })


@app.route('/convertir-braille', methods=['POST'])
def convertir_braille():
    data = request.get_json()
    braille = data.get('braille', '')

    if not braille:
        return jsonify({'error': 'No se proporcionó texto braille'}), 400

    texto = braille_a_texto(braille)

    return jsonify({
        'braille_original': braille,
        'texto': texto
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
