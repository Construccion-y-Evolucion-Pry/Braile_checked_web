import unittest
from app import texto_a_braille, braille_a_texto


class TestBrailleConverter(unittest.TestCase):
    """
    Casos de prueba para el convertidor bidireccional Texto-Braille
    Basado en las especificaciones del proyecto de transcripción Braille
    Versión 2.0 - Incluye pruebas de Braille a Texto
    """

    # ============================================================
    # PARTE 1: CASOS DE PRUEBA TEXTO A BRAILLE
    # ============================================================

    # ============== ALFABETO BÁSICO ==============
    
    def test_CP001_primera_serie_minusculas(self):
        """CP-001: Verificar conversión de primera serie (a-j) en minúsculas"""
        texto = "abcdefghij"
        esperado = "⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado, 
                        f"Error en primera serie: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP002_segunda_serie_minusculas(self):
        """CP-002: Verificar conversión de segunda serie (k-t) en minúsculas"""
        texto = "klmnopqrst"
        esperado = "⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en segunda serie: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP003_tercera_serie_minusculas(self):
        """CP-003: Verificar conversión de tercera serie (u-z) en minúsculas"""
        texto = "uvxyz"
        esperado = "⠥⠧⠭⠽⠵"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en tercera serie: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP004_letra_w(self):
        """CP-004: Verificar conversión de letra w (carácter adicional)"""
        texto = "w"
        esperado = "⠺"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en letra w: esperado '{esperado}', obtenido '{resultado}'")

    # ============== MAYÚSCULAS ==============
    
    def test_CP005_mayuscula_simple(self):
        """CP-005: Verificar conversión de una letra mayúscula"""
        texto = "A"
        esperado = "⠨⠁"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en mayúscula A: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP006_palabra_con_mayuscula_inicial(self):
        """CP-006: Verificar conversión de palabra con mayúscula inicial"""
        texto = "Hola"
        esperado = "⠨⠓⠕⠇⠁"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en 'Hola': esperado '{esperado}', obtenido '{resultado}'")

    def test_CP007_todas_mayusculas(self):
        """CP-007: Verificar conversión de texto todo en mayúsculas"""
        texto = "CASA"
        esperado = "⠨⠉⠨⠁⠨⠎⠨⠁"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en 'CASA': esperado '{esperado}', obtenido '{resultado}'")

    # ============== CARACTERES ESPECIALES ESPAÑOL ==============
    
    def test_CP008_letra_enie(self):
        """CP-008: Verificar conversión de letra ñ"""
        texto = "niño"
        esperado = "⠝⠊⠻⠕"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en 'niño': esperado '{esperado}', obtenido '{resultado}'")

    def test_CP009_vocales_acentuadas(self):
        """CP-009: Verificar conversión de todas las vocales acentuadas"""
        texto = "áéíóú"
        esperado = "⠷⠮⠌⠬⠾"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en vocales acentuadas: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP010_u_dieresis(self):
        """CP-010: Verificar conversión de ü (diéresis)"""
        texto = "güe"
        esperado = "⠛⠳⠑"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en 'güe': esperado '{esperado}', obtenido '{resultado}'")

    def test_CP011_palabra_con_tilde_y_mayuscula(self):
        """CP-011: Verificar conversión de palabra con mayúscula inicial y tilde"""
        texto = "María"
        esperado = "⠨⠍⠁⠗⠌⠁"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en 'María': esperado '{esperado}', obtenido '{resultado}'")

    # ============== NÚMEROS ==============
    
    def test_CP012_numero_simple(self):
        """CP-012: Verificar conversión de un número simple (un dígito)"""
        texto = "5"
        esperado = "⠼⠑"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en número '5': esperado '{esperado}', obtenido '{resultado}'")

    def test_CP013_numero_multiple_digitos(self):
        """CP-013: Verificar conversión de número de múltiples dígitos"""
        texto = "2024"
        esperado = "⠼⠃⠚⠃⠙"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en '2024': esperado '{esperado}', obtenido '{resultado}'")

    def test_CP014_numero_decimal_con_punto(self):
        """CP-014: Verificar conversión de número decimal con punto"""
        texto = "123.45"
        esperado = "⠼⠁⠃⠉⠄⠼⠙⠑"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en '123.45': esperado '{esperado}', obtenido '{resultado}'")

    def test_CP015_numero_decimal_con_coma(self):
        """CP-015: Verificar conversión de número decimal con coma"""
        texto = "3,14"
        esperado = "⠼⠉⠂⠼⠁⠙"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en '3,14': esperado '{esperado}', obtenido '{resultado}'")

    def test_CP016_secuencia_numeros_con_0(self):
        """CP-016: Verificar conversión de números del 1 al 0"""
        texto = "1234567890"
        esperado = "⠼⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en secuencia 1-0: esperado '{esperado}', obtenido '{resultado}'")

    # ============== SIGNOS DE PUNTUACIÓN ==============
    
    def test_CP017_punto_final(self):
        """CP-017: Verificar conversión de punto final"""
        texto = "fin."
        esperado = "⠋⠊⠝⠄"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con punto: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP018_coma_separadora(self):
        """CP-018: Verificar conversión de coma separadora (no decimal)"""
        texto = "hola, mundo"
        esperado = "⠓⠕⠇⠁⠂⠀⠍⠥⠝⠙⠕"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con coma: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP019_signos_interrogacion(self):
        """CP-019: Verificar conversión de signos de interrogación"""
        texto = "¿cómo?"
        esperado = "⠢⠉⠬⠍⠕⠦"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con interrogación: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP020_signos_exclamacion(self):
        """CP-020: Verificar conversión de signos de exclamación"""
        texto = "¡hola!"
        esperado = "⠖⠓⠕⠇⠁⠴"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con exclamación: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP021_parentesis(self):
        """CP-021: Verificar conversión de paréntesis"""
        texto = "(texto)"
        esperado = "⠣⠞⠑⠭⠞⠕⠜"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con paréntesis: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP022_dos_puntos_y_punto_coma(self):
        """CP-022: Verificar conversión de dos puntos y punto y coma"""
        texto = "uno: dos; tres"
        esperado = "⠥⠝⠕⠒⠀⠙⠕⠎⠆⠀⠞⠗⠑⠎"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con : y ;: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP023_guion(self):
        """CP-023: Verificar conversión de guion"""
        texto = "bien-estar"
        esperado = "⠃⠊⠑⠝⠤⠑⠎⠞⠁⠗"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con guion: esperado '{esperado}', obtenido '{resultado}'")

    # ============== ESPACIOS Y FORMATO ==============
    
    def test_CP024_espacios_en_blanco(self):
        """CP-024: Verificar conversión de espacios en blanco"""
        texto = "dos palabras"
        esperado = "⠙⠕⠎⠀⠏⠁⠇⠁⠃⠗⠁⠎"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con espacios: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP025_multiples_espacios(self):
        """CP-025: Verificar conversión de múltiples espacios"""
        texto = "a  b"
        esperado = "⠁⠀⠀⠃"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con múltiples espacios: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP026_salto_de_linea(self):
        """CP-026: Verificar preservación de saltos de línea"""
        texto = "línea1\nlínea2"
        esperado = "⠇⠌⠝⠑⠁⠼⠁\n⠇⠌⠝⠑⠁⠼⠃"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con salto de línea: esperado '{esperado}', obtenido '{resultado}'")

    # ============== FRASES COMPLEJAS ==============
    
    def test_CP027_frase_completa_simple(self):
        """CP-027: Verificar conversión de frase simple completa"""
        texto = "Hola mundo."
        esperado = "⠨⠓⠕⠇⠁⠀⠍⠥⠝⠙⠕⠄"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en frase simple: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP028_frase_con_numeros_y_letras(self):
        """CP-028: Verificar conversión de texto mezclado con números"""
        texto = "Año 2024"
        esperado = "⠨⠁⠻⠕⠀⠼⠃⠚⠃⠙"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en 'Año 2024': esperado '{esperado}', obtenido '{resultado}'")

    def test_CP029_oracion_interrogativa(self):
        """CP-029: Verificar conversión de oración interrogativa completa"""
        texto = "¿Cuál es tu número?"
        esperado = "⠢⠨⠉⠥⠷⠇⠀⠑⠎⠀⠞⠥⠀⠝⠾⠍⠑⠗⠕⠦"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en pregunta: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP030_senaletica_ascensor(self):
        """CP-030: Verificar conversión de señalética típica (ej: Piso 3)"""
        texto = "Piso 3"
        esperado = "⠨⠏⠊⠎⠕⠀⠼⠉"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en señalética: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP031_precio_con_decimal(self):
        """CP-031: Verificar conversión de precio con decimal"""
        texto = "precio: 19.99"
        esperado = "⠏⠗⠑⠉⠊⠕⠒⠀⠼⠁⠊⠄⠼⠊⠊"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en precio: esperado '{esperado}', obtenido '{resultado}'")

    # ============== CASOS LÍMITE ==============
    
    def test_CP032_texto_vacio(self):
        """CP-032: Verificar manejo de texto vacío"""
        texto = ""
        esperado = ""
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con texto vacío: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP033_solo_espacios(self):
        """CP-033: Verificar conversión de solo espacios"""
        texto = "   "
        esperado = "⠀⠀⠀"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con solo espacios: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP034_numeros_separados(self):
        """CP-034: Verificar que números separados tienen su propio prefijo"""
        texto = "1 2 3"
        esperado = "⠼⠁⠀⠼⠃⠀⠼⠉"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en números separados: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP035_alfabeto_completo_minusculas(self):
        """CP-035: Verificar alfabeto completo en minúsculas"""
        texto = "abcdefghijklmnopqrstuvwxyz"
        esperado = "⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en alfabeto completo: esperado '{esperado}', obtenido '{resultado}'")


    # ============================================================
    # PARTE 2: CASOS DE PRUEBA BRAILLE A TEXTO
    # ============================================================

    # ============== ALFABETO BÁSICO INVERSO ==============
    
    def test_CP101_primera_serie_braille_a_texto(self):
        """CP-101: Verificar conversión inversa de primera serie Braille"""
        braille = "⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚"
        esperado = "abcdefghij"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en primera serie inversa: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP102_segunda_serie_braille_a_texto(self):
        """CP-102: Verificar conversión inversa de segunda serie Braille"""
        braille = "⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞"
        esperado = "klmnopqrst"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en segunda serie inversa: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP103_tercera_serie_braille_a_texto(self):
        """CP-103: Verificar conversión inversa de tercera serie Braille"""
        braille = "⠥⠧⠭⠽⠵"
        esperado = "uvxyz"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en tercera serie inversa: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP104_letra_w_braille_a_texto(self):
        """CP-104: Verificar conversión inversa de letra w"""
        braille = "⠺"
        esperado = "w"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en letra w inversa: esperado '{esperado}', obtenido '{resultado}'")

    # ============== MAYÚSCULAS INVERSAS ==============
    
    def test_CP105_mayuscula_simple_braille_a_texto(self):
        """CP-105: Verificar reconocimiento de prefijo de mayúscula"""
        braille = "⠨⠁"
        esperado = "A"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en mayúscula inversa: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP106_palabra_con_mayuscula_inicial_inversa(self):
        """CP-106: Verificar conversión de palabra con mayúscula inicial"""
        braille = "⠨⠓⠕⠇⠁"
        esperado = "Hola"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en 'Hola' inversa: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP107_todas_mayusculas_inversas(self):
        """CP-107: Verificar reconocimiento de múltiples prefijos de mayúsculas"""
        braille = "⠨⠉⠨⠁⠨⠎⠨⠁"
        esperado = "CASA"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en 'CASA' inversa: esperado '{esperado}', obtenido '{resultado}'")

    # ============== CARACTERES ESPECIALES INVERSOS ==============
    
    def test_CP108_letra_enie_braille_a_texto(self):
        """CP-108: Verificar conversión inversa de ñ"""
        braille = "⠝⠊⠻⠕"
        esperado = "niño"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en 'niño' inverso: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP109_vocales_acentuadas_inversas(self):
        """CP-109: Verificar conversión inversa de vocales acentuadas"""
        braille = "⠷⠮⠌⠬⠾"
        esperado = "áéíóú"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en vocales acentuadas inversas: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP110_u_dieresis_inversa(self):
        """CP-110: Verificar conversión inversa de ü"""
        braille = "⠛⠳⠑"
        esperado = "güe"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en 'güe' inverso: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP111_palabra_con_tilde_y_mayuscula_inversa(self):
        """CP-111: Verificar combinación de mayúscula y vocal acentuada"""
        braille = "⠨⠍⠁⠗⠌⠁"
        esperado = "María"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en 'María' inverso: esperado '{esperado}', obtenido '{resultado}'")

    # ============== NÚMEROS INVERSOS ==============
    
    def test_CP112_numero_simple_braille_a_texto(self):
        """CP-112: Verificar reconocimiento de prefijo numérico"""
        braille = "⠼⠑"
        esperado = "5"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en número '5' inverso: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP113_numero_multiple_digitos_inverso(self):
        """CP-113: Verificar conversión de número con prefijo único"""
        braille = "⠼⠃⠚⠃⠙"
        esperado = "2024"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en '2024' inverso: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP114_numero_decimal_con_punto_inverso(self):
        """CP-114: Verificar conversión de decimal con punto"""
        braille = "⠼⠁⠃⠉⠄⠼⠙⠑"
        esperado = "123.45"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en '123.45' inverso: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP115_numero_decimal_con_coma_inverso(self):
        """CP-115: Verificar conversión de decimal con coma"""
        braille = "⠼⠉⠂⠼⠁⠙"
        esperado = "3,14"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en '3,14' inverso: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP116_secuencia_numeros_con_0_inverso(self):
        """CP-116: Verificar conversión de todos los dígitos"""
        braille = "⠼⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚"
        esperado = "1234567890"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en secuencia 1-0 inversa: esperado '{esperado}', obtenido '{resultado}'")

    # ============== SIGNOS DE PUNTUACIÓN INVERSOS ==============
    
    def test_CP117_punto_final_inverso(self):
        """CP-117: Verificar conversión de punto Braille"""
        braille = "⠋⠊⠝⠄"
        esperado = "fin."
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con punto inverso: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP118_coma_separadora_inversa(self):
        """CP-118: Verificar conversión de coma no decimal"""
        braille = "⠓⠕⠇⠁⠂⠀⠍⠥⠝⠙⠕"
        esperado = "hola, mundo"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con coma inversa: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP119_signos_interrogacion_inversos(self):
        """CP-119: Verificar conversión de interrogación Braille"""
        braille = "⠢⠉⠬⠍⠕⠦"
        esperado = "¿cómo?"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con interrogación inversa: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP120_signos_exclamacion_inversos(self):
        """CP-120: Verificar conversión de exclamación Braille"""
        braille = "⠖⠓⠕⠇⠁⠴"
        esperado = "¡hola!"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con exclamación inversa: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP121_parentesis_inversos(self):
        """CP-121: Verificar conversión de paréntesis Braille"""
        braille = "⠣⠞⠑⠭⠞⠕⠜"
        esperado = "(texto)"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con paréntesis inversos: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP122_dos_puntos_y_punto_coma_inversos(self):
        """CP-122: Verificar conversión de : y ; Braille"""
        braille = "⠥⠝⠕⠒⠀⠙⠕⠎⠆⠀⠞⠗⠑⠎"
        esperado = "uno: dos; tres"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con : y ; inversos: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP123_guion_inverso(self):
        """CP-123: Verificar conversión de guion Braille"""
        braille = "⠃⠊⠑⠝⠤⠑⠎⠞⠁⠗"
        esperado = "bien-estar"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con guion inverso: esperado '{esperado}', obtenido '{resultado}'")

    # ============== ESPACIOS Y FORMATO INVERSOS ==============
    
    def test_CP124_espacios_en_blanco_inversos(self):
        """CP-124: Verificar preservación de espacios Braille"""
        braille = "⠙⠕⠎⠀⠏⠁⠇⠁⠃⠗⠁⠎"
        esperado = "dos palabras"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con espacios inversos: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP125_multiples_espacios_inversos(self):
        """CP-125: Verificar preservación de múltiples espacios"""
        braille = "⠁⠀⠀⠃"
        esperado = "a  b"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con múltiples espacios inversos: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP126_salto_de_linea_inverso(self):
        """CP-126: Verificar preservación de saltos de línea"""
        braille = "⠇⠌⠝⠑⠁⠼⠁\n⠇⠌⠝⠑⠁⠼⠃"
        esperado = "línea1\nlínea2"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con salto de línea inverso: esperado '{esperado}', obtenido '{resultado}'")

    # ============== FRASES COMPLEJAS INVERSAS ==============
    
    def test_CP127_frase_completa_simple_inversa(self):
        """CP-127: Verificar conversión completa de frase"""
        braille = "⠨⠓⠕⠇⠁⠀⠍⠥⠝⠙⠕⠄"
        esperado = "Hola mundo."
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en frase simple inversa: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP128_frase_con_numeros_y_letras_inversa(self):
        """CP-128: Verificar mezcla de texto y números"""
        braille = "⠨⠁⠻⠕⠀⠼⠃⠚⠃⠙"
        esperado = "Año 2024"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en 'Año 2024' inverso: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP129_oracion_interrogativa_inversa(self):
        """CP-129: Verificar oración interrogativa completa"""
        braille = "⠢⠨⠉⠥⠷⠇⠀⠑⠎⠀⠞⠥⠀⠝⠾⠍⠑⠗⠕⠦"
        esperado = "¿Cuál es tu número?"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en pregunta inversa: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP130_senaletica_ascensor_inversa(self):
        """CP-130: Verificar lectura de señalética Braille"""
        braille = "⠨⠏⠊⠎⠕⠀⠼⠉"
        esperado = "Piso 3"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en señalética inversa: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP131_precio_con_decimal_inverso(self):
        """CP-131: Verificar formato de precios inverso"""
        braille = "⠏⠗⠑⠉⠊⠕⠒⠀⠼⠁⠊⠄⠼⠊⠊"
        esperado = "precio: 19.99"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en precio inverso: esperado '{esperado}', obtenido '{resultado}'")

    # ============== CASOS LÍMITE INVERSOS ==============
    
    def test_CP132_braille_vacio(self):
        """CP-132: Verificar manejo de entrada Braille vacía"""
        braille = ""
        esperado = ""
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con braille vacío: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP133_solo_espacios_braille(self):
        """CP-133: Verificar entrada con solo espacios Braille"""
        braille = "⠀⠀⠀"
        esperado = "   "
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error con solo espacios braille: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP134_numeros_separados_inversos(self):
        """CP-134: Verificar reconocimiento de múltiples prefijos numéricos"""
        braille = "⠼⠁⠀⠼⠃⠀⠼⠉"
        esperado = "1 2 3"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en números separados inversos: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP135_alfabeto_completo_braille_a_texto(self):
        """CP-135: Verificar alfabeto completo Braille a minúsculas"""
        braille = "⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵"
        esperado = "abcdefghijklmnopqrstuvwxyz"
        resultado = braille_a_texto(braille)
        self.assertEqual(resultado, esperado,
                        f"Error en alfabeto completo inverso: esperado '{esperado}', obtenido '{resultado}'")


    # ============================================================
    # PARTE 3: CASOS DE PRUEBA DE BIDIRECCIONALIDAD
    # ============================================================

    def test_CP201_bidireccionalidad_alfabeto(self):
        """CP-201: Verificar que texto → braille → texto = texto original (alfabeto)"""
        texto_original = "abcdefghijklmnopqrstuvwxyz"
        braille_intermedio = texto_a_braille(texto_original)
        texto_final = braille_a_texto(braille_intermedio)
        self.assertEqual(texto_original, texto_final,
                        f"Bidireccionalidad fallida en alfabeto: '{texto_original}' != '{texto_final}'")

    def test_CP202_bidireccionalidad_frase_compleja(self):
        """CP-202: Verificar ida y vuelta con frase compleja"""
        texto_original = "¡Hola mundo! Año 2024."
        braille_intermedio = texto_a_braille(texto_original)
        texto_final = braille_a_texto(braille_intermedio)
        self.assertEqual(texto_original, texto_final,
                        f"Bidireccionalidad fallida en frase: '{texto_original}' != '{texto_final}'")

    def test_CP203_bidireccionalidad_numeros_decimales(self):
        """CP-203: Verificar ida y vuelta con números y decimales"""
        texto_original = "El precio es 19.99 o 3,14"
        braille_intermedio = texto_a_braille(texto_original)
        texto_final = braille_a_texto(braille_intermedio)
        self.assertEqual(texto_original, texto_final,
                        f"Bidireccionalidad fallida en números: '{texto_original}' != '{texto_final}'")

    def test_CP204_bidireccionalidad_caracteres_especiales(self):
        """CP-204: Verificar ida y vuelta con ñ, tildes y diéresis"""
        texto_original = "El niño español güe áéíóú"
        braille_intermedio = texto_a_braille(texto_original)
        texto_final = braille_a_texto(braille_intermedio)
        self.assertEqual(texto_original, texto_final,
                        f"Bidireccionalidad fallida en especiales: '{texto_original}' != '{texto_final}'")

    def test_CP205_bidireccionalidad_mayusculas_mixtas(self):
        """CP-205: Verificar ida y vuelta con mayúsculas mixtas"""
        texto_original = "María González VIVE en España"
        braille_intermedio = texto_a_braille(texto_original)
        texto_final = braille_a_texto(braille_intermedio)
        self.assertEqual(texto_original, texto_final,
                        f"Bidireccionalidad fallida en mayúsculas: '{texto_original}' != '{texto_final}'")


def run_tests():
    """Ejecutar todos los tests y generar reporte"""
    # Crear suite de tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestBrailleConverter)
    
    # Ejecutar tests con verbosidad
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Resumen final
    print("\n" + "="*70)
    print("RESUMEN DE EJECUCIÓN DE CASOS DE PRUEBA")
    print("="*70)
    print(f"Total de casos de prueba ejecutados: {result.testsRun}")
    print(f"Casos exitosos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Casos fallidos: {len(result.failures)}")
    print(f"Errores: {len(result.errors)}")
    
    # Desglose por tipo de prueba
    print("\nDESGLOSE POR TIPO:")
    print(f"  - Texto a Braille (CP-001 a CP-035): 35 casos")
    print(f"  - Braille a Texto (CP-101 a CP-135): 35 casos")
    print(f"  - Bidireccionalidad (CP-201 a CP-205): 5 casos")
    
    if result.wasSuccessful():
        print("\n✓ TODOS LOS CASOS DE PRUEBA PASARON EXITOSAMENTE")
    else:
        print("\n✗ ALGUNOS CASOS DE PRUEBA FALLARON")
        
    return result


if __name__ == '__main__':
    run_tests()