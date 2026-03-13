from config import Config
from logic import PomodoroApp

if __name__ == "__main__":
    """
    Punto de entrada de la aplicación.
    
    Instancia la configuración global e inicia el flujo principal 
    de la aplicación Pomodoro.
    """
    config = Config()
    app = PomodoroApp(config)
    app.start()