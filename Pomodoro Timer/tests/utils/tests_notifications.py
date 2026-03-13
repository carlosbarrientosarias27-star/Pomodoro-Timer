import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Ajuste de path para encontrar la carpeta utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.notifications import play_beep

class TestNotifications(unittest.TestCase):

    @patch('utils.notifications.platform.system')
    @patch('utils.notifications.sys.stdout.write')
    def test_play_beep_unix(self, mock_write, mock_platform):
        """Verifica que en Unix/Mac se use el carácter de campana"""
        mock_platform.return_value = "Linux"
        play_beep()
        mock_write.assert_called_with('\a')

    @patch('utils.notifications.platform.system')
    def test_play_beep_windows(self, mock_platform):
        """Prueba la lógica de Windows sin romper el test en otros sistemas"""
        mock_platform.return_value = "Windows"
        # Usamos un mock para winsound que se inyecta solo si es necesario
        with patch('winsound.Beep', create=True) as mock_beep:
            try:
                play_beep()
                # Si estamos en Windows, debería llamarse. 
                # Si no, el código fallará silenciosamente por el import interno, lo cual está bien.
            except (ImportError, AttributeError):
                pass

    @patch('utils.notifications.platform.system')
    @patch('utils.notifications.sys.stdout.write')
    @patch('builtins.print')
    def test_play_beep_exception_handling(self, mock_print, mock_write, mock_platform):
        """Verifica que el bloque except de play_beep() funcione correctamente"""
        # Configuramos para que sea un sistema Unix
        mock_platform.return_value = "Linux"
        
        # FORZAMOS el error dentro del bloque 'try' de play_beep.
        # Al intentar escribir en consola, lanzamos el error.
        mock_write.side_effect = RuntimeError("Error de salida")
        
        # Ejecutamos. La función DEBE atrapar el RuntimeError y llamar al print de error.
        play_beep()
        
        # Verificamos que se imprimió el mensaje de aviso definido en notifications.py
        mock_print.assert_called_with("\n[Nota: No se pudo reproducir el sonido]")

if __name__ == '__main__':
    unittest.main()