import os
import platform

class UI:
    """Clase estática para gestionar la interfaz de usuario en la terminal."""
    
    @staticmethod
    def clear():
        """Limpia la consola según el sistema operativo (Windows o Unix)."""
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    @staticmethod
    def display_header(mode, current, total):
        """
        Muestra el encabezado visual con el modo actual y el progreso de ciclos.
        
        Args:
            mode (str): Etiqueta del estado (TRABAJO, DESCANSO, PAUSADO).
            current (int): Ciclo actual.
            total (int): Total de ciclos configurados.
        """
        print(f"{'='*10} MODO: {mode} {'='*10}")
        print(f"Ciclo: {current}/{total}")

    @staticmethod
    def progress_bar(current, total, length=30):
        """
        Genera una cadena de texto representando una barra de progreso.
        
        Args:
            current (float): Valor de progreso actual.
            total (float): Valor máximo del progreso.
            length (int): Longitud visual de la barra en caracteres.
        Returns:
            str: Barra de progreso formateada.
        """
        percent = current / total
        filled = int(length * percent)
        bar = '█' * filled + '-' * (length - filled)
        return f"|{bar}| {int(percent * 100)}%"

    @staticmethod
    def welcome_message():
        """Muestra el mensaje de bienvenida inicial."""
        UI.clear()
        print("--- BIENVENIDO AL POMODORO TIMER ---")