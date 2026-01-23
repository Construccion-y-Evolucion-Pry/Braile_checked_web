import os
import io
from flask import Flask, render_template, request, jsonify, send_file
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

app = Flask(__name__, static_folder='static')

# ================= DICCIONARIOS BRAILLE =================

BRAILLE_MAP = {
    'a': '⠁','b': '⠃','c': '⠉','d': '⠙','e': '⠑',
    'f': '⠋','g': '⠛','h': '⠓','i': '⠊','j': '⠚',
    'k': '⠅','l': '⠇','m': '⠍','n': '⠝','o': '⠕',
    'p': '⠏','q': '⠟','r': '⠗','s': '⠎','t': '⠞',
    'u': '⠥','v': '⠧','w': '⠺','x': '⠭','y': '⠽',
    'z': '⠵',
    'ñ': '⠻',
    'á': '⠷','é': '⠮','í': '⠌','ó': '⠬','ú': '⠾',
    'ü': '⠳',
    ' ': '⠀',
    '.': '⠄', ',': '⠂', ';': '⠆', ':': '⠒',
    '!': '⠖', '?': '⠦', '-': '⠤',
    '\n': '\n'
}

BRAILLE_NUMBERS = {
    '1': '⠁','2': '⠃','3': '⠉','4': '⠙','5': '⠑',
    '6': '⠋','7': '⠛','8': '⠓','9': '⠊','0': '⠚'
}

SIGNO_MAYUSCULA = '⠨'
SIGNO_NUMERO = '⠼'

BRAILLE_TO_TEXT = {v: k for k, v in BRAILLE_MAP.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in BRAILLE_NUMBERS.items()}

# ================= FUNCIÓN DE ESPEJO BRAILLE =================

def espejo_braille(texto_braille):
    """
    Convierte texto Braille al formato espejo para perforar.
    
    Proceso:
    1. Invierte cada carácter Braille horizontalmente (intercambia columnas)
    2. Invierte el orden de los caracteres (de derecha a izquierda)
    
    Al perforar desde atrás con este texto, el relieve se leerá correctamente desde el frente.
    """
    resultado = []
    
    for char in texto_braille:
        # Si es un carácter Braille Unicode (rango 0x2800-0x28FF)
        if '\u2800' <= char <= '\u28FF':
            # Obtener el código del carácter
            codigo = ord(char) - 0x2800
            
            # Extraer los 6 puntos (bits 0-5)
            # Patrón original:  Punto 1 (bit 0), Punto 2 (bit 1), Punto 3 (bit 2)
            #                   Punto 4 (bit 3), Punto 5 (bit 4), Punto 6 (bit 5)
            # 
            # Distribución visual:  1 4
            #                       2 5
            #                       3 6
            
            p1 = (codigo >> 0) & 1
            p2 = (codigo >> 1) & 1
            p3 = (codigo >> 2) & 1
            p4 = (codigo >> 3) & 1
            p5 = (codigo >> 4) & 1
            p6 = (codigo >> 5) & 1
            
            # Intercambiar columnas: 1↔4, 2↔5, 3↔6
            nuevo_codigo = (p4 << 0) | (p5 << 1) | (p6 << 2) | (p1 << 3) | (p2 << 4) | (p3 << 5)
            
            resultado.append(chr(0x2800 + nuevo_codigo))
        else:
            # Caracteres no-Braille se mantienen igual
            resultado.append(char)
    
    # Invertir el orden de los caracteres (escribir de derecha a izquierda)
    return ''.join(resultado[::-1])

# ================= LÓGICA DE CONVERSIÓN =================

def texto_a_braille(texto):
    resultado = []
    numero_activo = False
    buffer = []

    for c in texto:
        if c.isdigit():
            if not numero_activo:
                numero_activo = True
                buffer = []
            buffer.append(BRAILLE_NUMBERS[c])
        else:
            if numero_activo:
                resultado.append(SIGNO_NUMERO + ''.join(buffer))
                buffer = []
                numero_activo = False

            if c.isupper() and c.lower() in BRAILLE_MAP:
                resultado.append(SIGNO_MAYUSCULA + BRAILLE_MAP[c.lower()])
            elif c.lower() in BRAILLE_MAP:
                resultado.append(BRAILLE_MAP[c.lower()])
            else:
                resultado.append(c)

    if numero_activo:
        resultado.append(SIGNO_NUMERO + ''.join(buffer))

    return ''.join(resultado)


def braille_a_texto(braille):
    resultado = []
    i = 0
    numero = False
    mayus = False

    while i < len(braille):
        c = braille[i]

        if c == '\n':
            resultado.append('\n')
            numero = False
            i += 1
            continue

        if c == SIGNO_NUMERO:
            numero = True
            i += 1
            continue

        if c == SIGNO_MAYUSCULA:
            mayus = True
            i += 1
            continue

        if numero:
            if c in BRAILLE_TO_NUMBER:
                resultado.append(BRAILLE_TO_NUMBER[c])
            elif c == '⠀':  # Espacio termina modo número
                numero = False
                resultado.append(' ')
            else:
                numero = False
                if c in BRAILLE_TO_TEXT:
                    letra = BRAILLE_TO_TEXT[c]
                    resultado.append(letra.upper() if mayus else letra)
                    mayus = False
                else:
                    resultado.append(c)
            i += 1
            continue

        if c in BRAILLE_TO_TEXT:
            letra = BRAILLE_TO_TEXT[c]
            resultado.append(letra.upper() if mayus else letra)
            mayus = False
        else:
            resultado.append(c)

        i += 1

    return ''.join(resultado)

# ================= RUTAS =================

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
    texto = request.json.get('texto', '')
    if not texto:
        return jsonify({'error': 'No se proporcionó texto'}), 400
    return jsonify({'texto_braille': texto_a_braille(texto)})

@app.route('/convertir-braille', methods=['POST'])
def convertir_braille():
    braille = request.json.get('braille', '')
    if not braille:
        return jsonify({'error': 'No se proporcionó texto braille'}), 400
    return jsonify({'texto': braille_a_texto(braille)})

@app.route('/validar-braille', methods=['POST'])
def validar_braille():
    """
    Valida si un carácter Braille es válido según el modo activo.
    
    Modos:
    - 'letra': Valida que sea una letra, ñ, vocal con tilde, o signo de puntuación
    - 'numero': Valida que sea un dígito (0-9)
    - 'especial': Valida que sea un carácter especial válido
    """
    data = request.json
    char = data.get('braille', '')
    modo = data.get('modo', 'letra')

    # Validar que se envió un carácter
    if not char:
        return jsonify({'error': 'No se proporcionó carácter Braille'}), 400

    # Validar que sea un carácter Unicode Braille
    if not ('\u2800' <= char <= '\u28FF'):
        return jsonify({'error': 'No es un carácter Braille válido'}), 400

    # Validación según modo
    if modo == 'letra':
        # En modo letra, aceptar letras, signos de puntuación y espacio
        if char not in BRAILLE_TO_TEXT:
            return jsonify({'error': 'No es una letra o signo válido en modo letra'}), 400

    elif modo == 'numero':
        # En modo número, solo aceptar dígitos
        if char not in BRAILLE_TO_NUMBER:
            return jsonify({'error': 'No es un número Braille válido (0-9)'}), 400

    elif modo == 'especial':
        # En modo especial, aceptar cualquier carácter que esté en el mapa
        # (esto incluye signos de puntuación, paréntesis, etc.)
        if char not in BRAILLE_TO_TEXT:
            return jsonify({'error': 'No es un carácter especial reconocido'}), 400

    else:
        return jsonify({'error': 'Modo no reconocido'}), 400

    # Si pasó todas las validaciones
    return jsonify({
        'ok': True, 
        'caracter': char,
        'traduccion': BRAILLE_TO_TEXT.get(char) or BRAILLE_TO_NUMBER.get(char, '')
    })

@app.route('/descargar-braille-word', methods=['POST'])
def descargar_braille_word():
    braille = request.json.get('braille', '')
    texto = request.json.get('texto', '')

    if not braille:
        return jsonify({'error': 'No hay contenido Braille'}), 400

    doc = Document()
    
    # Configurar encabezado con instrucciones
    section = doc.sections[0]
    header = section.header
    header_para = header.paragraphs[0]
    header_para.text = (
        "⚠️ INSTRUCCIONES PARA PERFORAR ⚠️\n"
        "Este documento contiene Braille en formato ESPEJO.\n"
        "1. Imprime este documento\n"
        "2. Voltea la hoja\n"
        "3. Perfora desde el reverso siguiendo los puntos\n"
        "4. Al dar vuelta la hoja, se leerá correctamente"
    )
    header_para.runs[0].font.size = Pt(10)
    header_para.runs[0].bold = True
    
    # Agregar título
    titulo = doc.add_paragraph()
    titulo.text = "BRAILLE PARA PERFORAR (FORMATO ESPEJO)"
    titulo.runs[0].font.size = Pt(14)
    titulo.runs[0].bold = True
    titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Agregar Braille en espejo
    braille_espejo = espejo_braille(braille)
    para_braille = doc.add_paragraph()
    para_braille.text = braille_espejo
    para_braille.runs[0].font.size = Pt(24)
    para_braille.alignment = WD_ALIGN_PARAGRAPH.LEFT
    
    # Salto de página
    doc.add_page_break()
    
    # Agregar referencia del texto original
    titulo_ref = doc.add_paragraph()
    titulo_ref.text = "TEXTO ORIGINAL (Referencia)"
    titulo_ref.runs[0].font.size = Pt(14)
    titulo_ref.runs[0].bold = True
    titulo_ref.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    para_texto = doc.add_paragraph()
    para_texto.text = texto
    para_texto.runs[0].font.size = Pt(12)
    
    # Guardar en memoria
    file = io.BytesIO()
    doc.save(file)
    file.seek(0)

    return send_file(
        file, 
        as_attachment=True,
        download_name='braille_para_perforar.docx',
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)