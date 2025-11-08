from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Diccionario de mapeo de caracteres a símbolos Braille Unicode
BRAILLE_MAP = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵',
    '0': '⠚', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙',
    '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊',
    ' ': '⠀',  # Espacio Braille
    '.': '⠲', ',': '⠂', ';': '⠆', ':': '⠒', '!': '⠖',
    '?': '⠦', '-': '⠤', '(': '⠐⠣', ')': '⠐⠜',
}

def texto_a_braille(texto):
    """
    Convierte texto normal a símbolos Braille.
    
    Args:
        texto (str): El texto a convertir
        
    Returns:
        str: El texto convertido a símbolos Braille
    """
    resultado = []
    for caracter in texto.lower():
        if caracter in BRAILLE_MAP:
            resultado.append(BRAILLE_MAP[caracter])
        else:
            # Si el caracter no está en el mapa, mantenerlo como está
            resultado.append(caracter)
    
    return ''.join(resultado)

@app.route('/')
def index():
    """Ruta principal que muestra la interfaz."""
    return render_template('index.html')

@app.route('/convertir', methods=['POST'])
def convertir():
    """
    Endpoint para convertir texto a Braille.
    Espera un JSON con el campo 'texto'.
    """
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
