import platform
import sys

def play_beep():
    """
    Emite una alerta sonora. Utiliza winsound en Windows y el carácter de campana 
    de sistema (\a) en sistemas Unix/macOS.
    """
    system = platform.system()
    try:
        if system == "Windows":
            import winsound
            winsound.Beep(1000, 500)
        else:
            sys.stdout.write('\a')
            sys.stdout.flush()
    except Exception:
        print("\n[Nota: No se pudo reproducir el sonido]")