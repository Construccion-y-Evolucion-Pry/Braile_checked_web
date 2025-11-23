import unittest
from app import texto_a_braille


class TestBrailleConverter(unittest.TestCase):
    """
    Casos de prueba para el convertidor de texto a Braille
    Basado en las especificaciones del proyecto de transcripción Braille
    """

    # ============== CASOS DE PRUEBA: ALFABETO BÁSICO ==============
    
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

    # ============== CASOS DE PRUEBA: MAYÚSCULAS ==============
    
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

    # ============== CASOS DE PRUEBA: CARACTERES ESPECIALES ESPAÑOL ==============
    
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

    # ============== CASOS DE PRUEBA: NÚMEROS ==============
    
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
        esperado = "⠼⠁⠃⠉⠲⠙⠑"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en '123.45': esperado '{esperado}', obtenido '{resultado}'")

    def test_CP015_numero_decimal_con_coma(self):
        """CP-015: Verificar conversión de número decimal con coma"""
        texto = "3,14"
        esperado = "⠼⠉⠂⠁⠙"
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

    # ============== CASOS DE PRUEBA: SIGNOS DE PUNTUACIÓN ==============
    
    def test_CP017_punto_final(self):
        """CP-017: Verificar conversión de punto final"""
        texto = "fin."
        esperado = "⠋⠊⠝⠲"
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
        esperado = "⠦⠉⠬⠍⠕⠦"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con interrogación: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP020_signos_exclamacion(self):
        """CP-020: Verificar conversión de signos de exclamación"""
        texto = "¡hola!"
        esperado = "⠖⠓⠕⠇⠁⠖"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error con exclamación: esperado '{esperado}', obtenido '{resultado}'")

    def test_CP021_parentesis(self):
        """CP-021: Verificar conversión de paréntesis"""
        texto = "(texto)"
        esperado = "⠐⠣⠞⠑⠭⠞⠕⠐⠜"
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

    # ============== CASOS DE PRUEBA: ESPACIOS Y FORMATO ==============
    
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

    # ============== CASOS DE PRUEBA: FRASES COMPLEJAS ==============
    
    def test_CP027_frase_completa_simple(self):
        """CP-027: Verificar conversión de frase simple completa"""
        texto = "Hola mundo."
        esperado = "⠨⠓⠕⠇⠁⠀⠍⠥⠝⠙⠕⠲"
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
        esperado = "⠦⠨⠉⠥⠷⠇⠀⠑⠎⠀⠞⠥⠀⠝⠾⠍⠑⠗⠕⠦"
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
        esperado = "⠏⠗⠑⠉⠊⠕⠒⠀⠼⠁⠊⠲⠊⠊"
        resultado = texto_a_braille(texto)
        self.assertEqual(resultado, esperado,
                        f"Error en precio: esperado '{esperado}', obtenido '{resultado}'")

    # ============== CASOS DE PRUEBA: CASOS LÍMITE ==============
    
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
    
    if result.wasSuccessful():
        print("\n✓ TODOS LOS CASOS DE PRUEBA PASARON EXITOSAMENTE")
    else:
        print("\n✗ ALGUNOS CASOS DE PRUEBA FALLARON")
        
    return result


if __name__ == '__main__':
    run_tests()
