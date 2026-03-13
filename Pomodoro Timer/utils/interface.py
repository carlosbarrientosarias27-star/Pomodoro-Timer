import os
import platform

def clear_screen():
    """
    Detecta el sistema operativo y ejecuta el comando de terminal para limpiar la pantalla.
    """
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def progress_bar(current, total, length=30):
    """
    Genera una representación visual de una barra de carga.
    
    Args:
        current (int): Progreso actual (tiempo transcurrido).
        total (int): Valor máximo (tiempo total de la sesión).
        length (int): Longitud en caracteres de la barra.
        
    Returns:
        str: Cadena formateada con la barra [███   ] y el porcentaje.
    """
    percent = float(current) / total
    arrow = '█' * int(round(percent * length))
    spaces = ' ' * (length - len(arrow))
    return f"[{arrow}{spaces}] {int(percent * 100)}%"