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
    '.': '⠲', ',': '⠂', ';': '⠆', ':': '⠒',
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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)