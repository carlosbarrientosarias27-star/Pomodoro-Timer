import unittest
import sys
import os

# Ajuste dinámico de ruta para evitar ModuleNotFoundError
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import Config

class TestConfig(unittest.TestCase):
    def setUp(self):
        """Inicializa la configuración antes de cada prueba"""
        self.config = Config()

    def test_default_values(self):
        """Verifica los valores iniciales por defecto"""
        self.assertEqual(self.config.work_min, 25)
        self.assertEqual(self.config.total_cycles, 4)

    def test_work_min_setter_valid(self):
        """Prueba asignar un tiempo de trabajo válido"""
        self.config.work_min = 10
        self.assertEqual(self.config.work_min, 10)

    def test_work_min_setter_invalid(self):
        """Debe lanzar ValueError si el tiempo es 0 o negativo"""
        with self.assertRaises(ValueError):
            self.config.work_min = 0

    def test_validate_positive(self):
        """Verifica la lógica de validación de números positivos"""
        self.assertTrue(self.config.validate_positive(5))
        self.assertFalse(self.config.validate_positive(-1))
        self.assertFalse(self.config.validate_positive("texto"))

if __name__ == '__main__':
    unittest.main()