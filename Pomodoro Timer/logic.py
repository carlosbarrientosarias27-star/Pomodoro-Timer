import time
import sys
import threading
import os
# Importaciones desde la subcarpeta utils
from utils.interface import clear_screen, progress_bar
from utils.notifications import play_beep

class PomodoroApp:
    """Controla la lógica de ejecución, hilos y estados del temporizador."""
    
    def __init__(self, config):
        """
        Inicializa la aplicación con una configuración dada.
        
        Args:
            config (Config): Objeto de configuración con los tiempos de sesión.
        """
        self.config = config
        self.current_cycle = 0 
        self.paused = False    
        self.running = True
    
    def countdown(self, minutes, label):
        """
        Ejecuta el contador regresivo visual en la terminal.
        
        Args:
            minutes (int): Duración del temporizador en minutos.
            label (str): Etiqueta descriptiva del modo actual (ej. 'TRABAJO').
        """
        seconds = minutes * 60
        total_seconds = seconds
        
        while seconds > 0 and self.running:
            if not self.paused:
                mins, secs = divmod(seconds, 60)
                timer_display = f"{mins:02d}:{secs:02d}"
                
                clear_screen() 
                print(f"=== MODO: {label} ===")
                print(f"Ciclo: {self.current_cycle + 1}/{self.config.total_cycles}")
                print(f"\nTiempo restante: {timer_display}")
                print(progress_bar(total_seconds - seconds, total_seconds))
                print("\n[P] Pausar/Reanudar | [Q] Salir")
                
                time.sleep(1)
                seconds -= 1
            else:
                clear_screen()
                print(f"=== MODO: {label} (PAUSADO) ===")
                print("\nPresione 'P' para reanudar...")
                time.sleep(0.5)

        if self.running:
            play_beep()

    def start(self):
        clear_screen()
        print("--- BIENVENIDO AL POMODORO TIMER ---")
        
        try:
            # Validación activa de rangos razonables
            w = int(input("Minutos de trabajo (1-120): ") or 25)
            s = int(input("Minutos de descanso corto (1-30): ") or 5)
            
            if self.config.validate_positive(w) and self.config.validate_positive(s):
                self.config.work_min = w
                self.config.short_break_min = s
            else:
                print("Los valores deben ser positivos. Usando valores por defecto.")
                time.sleep(1)
        except ValueError:
            print("Entrada no válida, usando valores por defecto.")
            time.sleep(1)

        threading.Thread(target=self.listen_keys, daemon=True).start()

        while self.current_cycle < self.config.total_cycles and self.running:
            self.countdown(self.config.work_min, "TRABAJO")
            self.current_cycle += 1
            
            if self.current_cycle < self.config.total_cycles and self.running:
                if self.current_cycle % 4 == 0:
                    self.countdown(self.config.long_break_min, "DESCANSO LARGO")
                else:
                    self.countdown(self.config.short_break_min, "DESCANSO CORTO")
            
        if self.running:
            print("\n¡Felicidades! Has completado todas tus sesiones.")

    def listen_keys(self):
        """
        Escucha las pulsaciones de teclado en un hilo separado para controlar la ejecución.
        """
        while self.running:
            cmd = input().strip().lower() 
            if cmd == 'p':
                self.paused = not self.paused
            elif cmd == 'q':
                self.running = False
                os._exit(0)