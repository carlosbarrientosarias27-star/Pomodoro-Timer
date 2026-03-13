from config import Config
from logic import PomodoroApp

if __name__ == "__main__":
    """
    Punto de entrada principal del programa. 
    Instancia la configuración e inicia la aplicación.
    """
    config = Config()
    app = PomodoroApp(config)
    app.start()