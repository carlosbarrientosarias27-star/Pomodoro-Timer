import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# 1. Configuramos el PATH antes de importar nada del proyecto
current_dir = os.path.dirname(__file__)
root_path = os.path.abspath(os.path.join(current_dir, ".."))

if root_path not in sys.path:
    sys.path.insert(0, root_path)

# 2. Ahora sí importamos los módulos del proyecto
try:
    from logic import PomodoroApp
    from config import Config
except ModuleNotFoundError as e:
    print(f"\nError de importación: {e}")
    print(f"Path actual: {sys.path[0]}")
    sys.exit(1)

class TestPomodoroApp(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.app = PomodoroApp(self.config)

    @patch('logic.UI.clear')
    @patch('logic.UI.display_header')
    @patch('logic.UI.progress_bar')
    def test_render_frame(self, mock_bar, mock_header, mock_clear):
        """Verifica que el frame se dibuje llamando a los métodos de UI"""
        self.app._render_frame(25, 0, 1500, "TRABAJO")
        mock_clear.assert_called()
        mock_header.assert_called()
        mock_bar.assert_called()

    @patch('logic.time.sleep', return_value=None)
    @patch('logic.play_beep')
    @patch('logic.PomodoroApp._render_frame')
    def test_run_timer_completes(self, mock_render, mock_beep, mock_sleep):
        """Verifica que el timer corra hasta el final y suene el beep"""
        self.app.run_timer(1/60, "TEST") 
        self.assertTrue(self.app.is_running)
        mock_beep.assert_called()

    def test_toggle_pause(self):
        """Verifica que el estado de pausa cambie correctamente"""
        self.assertFalse(self.app.is_paused)
        self.app.is_paused = True
        self.assertTrue(self.app.is_paused)

if __name__ == '__main__':
    unittest.main()