import unittest
from palindromo import is_palindromo, obtener_cantidad_de_palabras_palindromo

class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        input_str = "a"
        result = is_palindromo(input_str)
        self.assertTrue(result)
    def test_with_ala(self):
        input_str = "ala"
        result = is_palindromo(input_str)
        self.assertTrue(result)
    def test_with_neuquen(self):
        input_str = "neuquen"
        result = is_palindromo(input_str)
        self.assertTrue(result)
    def test_with_hola(self):
        input_str = "hola"
        result = is_palindromo(input_str)
        self.assertFalse(result)

class TestCantidadDePalabrasPalindromes(unittest.TestCase):
    def test_cantidad_de_palabras_palindromes_simple(self):
        palabras = ["ala"]
        resultado = obtener_cantidad_de_palabras_palindromo(palabras)
        self.assertEqual(resultado, 1)
    def test_cantidad_de_palabras_palindromes_con_2(self):
        palabras = ["ala", "neuquen"]
        resultado = obtener_cantidad_de_palabras_palindromo(palabras)
        self.assertEqual(resultado, 2)
    def test_cantidad_de_palabras_palindromes_con_3(self):
        palabras = ["ala", "neuquen", "hola"]
        resultado = obtener_cantidad_de_palabras_palindromo(palabras)
        self.assertEqual(resultado, 2)
    def test_cantidad_de_palabras_palindromes_con_4(self):
        palabras = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cantidad_de_palabras_palindromo(palabras)
        self.assertEqual(resultado, 2)
    def test_cantidad_de_palabras_palindromes_con_5(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cantidad_de_palabras_palindromo(palabras)
        self.assertEqual(resultado, 3)
    def test_cantidad_de_palabras_palindromes_complejo(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cantidad_de_palabras_palindromo(palabras)
        self.assertEqual(resultado, 4)
    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        palabras = [
             "ala",
             "neuquen",
             "hola",
             "programacion",
             "palap",
             "neu  quen",
             "agita falsos usos la fatiga",
             "presidente de la camara de diputados: martin menem",
        ]
        resultado = obtener_cantidad_de_palabras_palindromo(palabras)
        self.assertEqual(resultado, 5)

if __name__ == '__main__':
    unittest.main()