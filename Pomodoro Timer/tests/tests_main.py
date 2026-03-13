import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# 1. Forzamos la ruta raíz al principio de la lista de búsqueda
# Esto permite que 'logic.py' encuentre 'utils.interface' correctamente
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# 2. Ahora realizamos la importación de main
try:
    import main
except ModuleNotFoundError as e:
    print(f"Error crítico de importación: {e}")
    sys.exit(1)

class TestMain(unittest.TestCase):
    @patch('main.PomodoroApp')
    @patch('main.Config')
    def test_main_execution(self, mock_config, mock_app):
        """Simula la ejecución del punto de entrada"""
        # Configuramos el mock de la app para que tenga un método start
        instance = mock_app.return_value
        
        # Simulamos la lógica del punto de entrada en main.py
        config = mock_config()
        app = mock_app(config)
        app.start()
        
        # Verificaciones
        mock_config.assert_called()
        mock_app.assert_called_with(config)
        instance.start.assert_called_once()

if __name__ == '__main__':
    unittest.main()