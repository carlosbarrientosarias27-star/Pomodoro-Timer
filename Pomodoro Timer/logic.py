import time
import threading
from utils.interface import UI
from utils.notifications import play_beep
from pynput import keyboard 

class PomodoroApp:
    """
    Orquestador principal de la aplicación. Gestiona el tiempo, hilos y teclado.
    """
    
    def __init__(self, config):
        """
        Inicializa la aplicación con la configuración definida.
        
        Args:
            config (Config): Objeto con los parámetros de tiempo.
        """
        self.config = config
        self.current_cycle = 0 
        self.is_paused = False    
        self.is_running = True

    def _render_frame(self, minutes, seconds, total_seconds, label):
        """
        Dibuja un 'cuadro' de la interfaz en la terminal.
        
        Args:
            minutes (int): Minutos restantes.
            seconds (int): Segundos restantes.
            total_seconds (int): Tiempo inicial total de la fase.
            label (str): Nombre de la fase actual.
        """
        status = "PAUSADO" if self.is_paused else label
        timer_str = f"{minutes:02d}:{seconds:02d}"
        
        UI.clear()
        UI.display_header(status, self.current_cycle + 1, self.config.total_cycles)
        print(f"\nTiempo restante: {timer_str}")
        print(UI.progress_bar(total_seconds - (minutes * 60 + seconds), total_seconds))
        print("\n[P] Pausar/Reanudar | [Q] Salir")

    def run_timer(self, minutes, label):
        """
        Ejecuta el bucle de cuenta regresiva para una fase específica.
        
        Args:
            minutes (int): Duración de la fase en minutos.
            label (str): Nombre de la fase (Trabajo/Descanso).
        """
        total_seconds = minutes * 60
        remaining = total_seconds
        
        while remaining > 0 and self.is_running:
            if not self.is_paused:
                mins, secs = divmod(remaining, 60)
                self._render_frame(mins, secs, total_seconds, label)
                time.sleep(1)
                remaining -= 1
            else:
                # Simula pausa refrescando la UI ocasionalmente
                self._render_frame(0, 0, total_seconds, label) 
                time.sleep(0.2)

        if self.is_running:
            play_beep()

    def start(self):
        """
        Inicia la ejecución global: configuración de usuario, hilos y ciclos.
        """
        UI.welcome_message()
        self._setup_custom_times()
        
        threading.Thread(target=self._listen_keys, daemon=True).start()

        for cycle in range(self.config.total_cycles):
            if not self.is_running: break
            
            self.current_cycle = cycle
            self.run_timer(self.config.work_min, "TRABAJO")
            
            if self.is_running and cycle < self.config.total_cycles - 1:
                is_long_break = (cycle + 1) % 4 == 0
                duration = self.config.long_break_min if is_long_break else self.config.short_break_min
                label = "DESCANSO LARGO" if is_long_break else "DESCANSO CORTO"
                self.run_timer(duration, label)
            
        if self.is_running:
            print("\n¡Felicidades! Has completado todas tus sesiones.")

    def _setup_custom_times(self):
        """Pregunta al usuario los tiempos de sesión antes de empezar."""
        try:
            w = int(input("Minutos de trabajo (1-120) [25]: ") or 25)
            s = int(input("Minutos de descanso corto (1-30) [5]: ") or 5)
            if self.config.validate_positive(w) and self.config.validate_positive(s):
                self.config.work_min, self.config.short_break_min = w, s
        except ValueError:
            print("Entrada no válida, usando valores por defecto...")
            time.sleep(1)

    def _listen_keys(self):
        """Configura el listener de teclado para capturar comandos en tiempo real."""
        def on_press(key):
            try:
                if key.char == 'p': self.is_paused = not self.is_paused
                if key.char == 'q': 
                    self.is_running = False
                    return False
            except AttributeError: pass
            
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()