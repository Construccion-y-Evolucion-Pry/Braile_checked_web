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

    # Vocales con tilde: signo de acento ⠬ + vocal
    'á': '⠷',
    'é': '⠮',
    'í': '⠌',
    'ó': '⠬',
    'ú': '⠾',

    'ü': '⠳',

    # Espacios y signos
    ' ': '⠀',
    '.': '⠲', ',': '⠂', ';': '⠆', ':': '⠒',
    '!': '⠖', '¡': '⠖', '?': '⠦', '-': '⠤',
    '(': '⠐⠣', ')': '⠐⠜', '¿': '⠦',
    '\n': '\n'  # Preservar saltos de línea
}

# Números en braille español (1–0)
BRAILLE_NUMBERS = {
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
}


def texto_a_braille(texto):
    resultado = []
    numero_activo = False
    numero_buffer = ''

    for caracter in texto.lower():
        # Caracter numérico
        if caracter.isdigit():
            numero_buffer += BRAILLE_NUMBERS[caracter]
            numero_activo = True
        else:
            # Si termina un bloque de números → agregamos prefijo ⠼
            if numero_activo:
                resultado.append('⠼' + numero_buffer)
                numero_buffer = ''
                numero_activo = False

            # Caracter del mapa
            if caracter in BRAILLE_MAP:
                resultado.append(BRAILLE_MAP[caracter])
            else:
                # Dejar caracteres desconocidos tal cual
                resultado.append(caracter)

    # Si terminó en número
    if numero_activo:
        resultado.append('⠼' + numero_buffer)

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
