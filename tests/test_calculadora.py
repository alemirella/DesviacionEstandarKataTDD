import unittest
from calculadora_estadistica.src.calculadora import calcular_promedio, calcular_desviacion_estandar, NoSePuedeCalcular

class TestCalculadora(unittest.TestCase):

    # Pruebas para calcular_promedio
    def test_promedio_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_promedio([])

    def test_promedio_un_elemento(self):
        resultado = calcular_promedio([10])
        self.assertEqual(resultado, 10)

    def test_promedio_dos_elementos(self):
        resultado = calcular_promedio([10, 20])
        self.assertEqual(resultado, 15)

    def test_promedio_varios_elementos_positivos(self):
        resultado = calcular_promedio([10, 20, 30, 40, 50])
        self.assertEqual(resultado, 30)

    def test_promedio_todos_ceros(self):
        resultado = calcular_promedio([0, 0, 0, 0, 0])
        self.assertEqual(resultado, 0)

    def test_promedio_elementos_positivos_y_negativos(self):
        resultado = calcular_promedio([10, -10, 20, -20, 30])
        self.assertEqual(resultado, 6)

    def test_promedio_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_promedio([10, "a", 20])

    # Pruebas para calcular_desviacion_estandar
    def test_desviacion_estandar_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_desviacion_estandar([])

    def test_desviacion_estandar_un_elemento(self):
        resultado = calcular_desviacion_estandar([10])
        self.assertEqual(resultado, 0.0)

    def test_desviacion_estandar_dos_elementos(self):
        resultado = calcular_desviacion_estandar([10, 20])
        self.assertAlmostEqual(resultado, 5.0, places=1)

    def test_desviacion_estandar_varios_elementos_positivos(self):
        resultado = calcular_desviacion_estandar([10, 20, 30, 40, 50])
        self.assertAlmostEqual(resultado, 14.14, places=2)

    def test_desviacion_estandar_todos_ceros(self):
        resultado = calcular_desviacion_estandar([0, 0, 0, 0, 0])
        self.assertEqual(resultado, 0.0)

    def test_desviacion_estandar_elementos_positivos_y_negativos(self):
        resultado = calcular_desviacion_estandar([10, -10, 20, -20, 30])
        self.assertAlmostEqual(resultado, 18.17, places=2)

    def test_desviacion_estandar_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_desviacion_estandar([10, "a", 20])

if __name__ == "__main__":
    unittest.main()
