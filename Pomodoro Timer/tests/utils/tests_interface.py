import sys
import os

# Añade la raíz del proyecto al path de búsqueda
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import unittest
from unittest.mock import patch, MagicMock
from utils.interface import UI

class TestUI(unittest.TestCase):

    @patch('os.system')
    @patch('platform.system')
    def test_clear_windows(self, mock_platform, mock_system):
        """Prueba que en Windows se llame a 'cls'"""
        mock_platform.return_value = 'Windows'
        UI.clear()
        mock_system.assert_called_once_with('cls')

    @patch('os.system')
    @patch('platform.system')
    def test_clear_unix(self, mock_platform, mock_system):
        """Prueba que en Linux/Mac se llame a 'clear'"""
        mock_platform.return_value = 'Linux'
        UI.clear()
        mock_system.assert_called_once_with('clear')

    def test_progress_bar_calculation(self):
        """Verifica que la barra de progreso calcule bien los caracteres"""
        # 50% de 30 caracteres = 15 bloques '█'
        result = UI.progress_bar(50, 100, length=30)
        self.assertIn('███████████████', result)
        self.assertIn('50%', result)

    @patch('builtins.print')
    def test_display_header_output(self, mock_print):
        """Prueba que el encabezado imprima el modo correcto"""
        UI.display_header("TRABAJO", 1, 4)
        # Verificamos que print fue llamado con el texto esperado
        mock_print.assert_any_call("========== MODO: TRABAJO ==========")
        mock_print.assert_any_call("Ciclo: 1/4")

if __name__ == '__main__':
    unittest.main()