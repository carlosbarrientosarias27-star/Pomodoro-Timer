import time
import os
import sys
import platform
import threading

# --- CONFIGURACIÓN (Commit 4) ---
class Config:
    """Maneja las variables configurables del temporizador."""
    def __init__(self):
        self.work_min = 25
        self.short_break_min = 5
        self.long_break_min = 15
        self.total_cycles = 4

    def validate_positive(self, val):
        """Valida que los valores sean positivos (Commit 4)."""
        return val > 0

# --- NOTIFICACIONES (Commit 6) ---
def play_beep():
    """Emite un sonido de notificación según el SO (Commit 6)."""
    system = platform.system()
    try:
        if system == "Windows":
            import winsound
            winsound.Beep(1000, 500)
        else:
            # Para Linux/Mac requiere usualmente 'beep' o usar el carácter de campana
            sys.stdout.write('\a')
            sys.stdout.flush()
    except Exception:
        print("\n[Nota: No se pudo reproducir el sonido]")

# --- INTERFAZ Y LÓGICA (Commits 2, 3, 5, 7, 8) ---
class PomodoroApp:
    def __init__(self, config):
        self.config = config
        self.current_cycle = 0 # Commit 5
        self.paused = False    # Commit 7
        self.running = True

    def clear_screen(self):
        """Limpia la terminal según el SO (Commit 8)."""
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    def progress_bar(self, current, total, length=30):
        """Genera una barra de progreso visual (Commit 8)."""
        percent = float(current) / total
        arrow = '█' * int(round(percent * length))
        spaces = ' ' * (length - len(arrow))
        return f"[{arrow}{spaces}] {int(percent * 100)}%"

    def countdown(self, minutes, label):
        """Función principal de cuenta regresiva (Commit 2)."""
        seconds = minutes * 60
        total_seconds = seconds
        
        while seconds > 0 and self.running:
            if not self.paused:
                mins, secs = divmod(seconds, 60)
                timer_display = f"{mins:02d}:{secs:02d}"
                
                self.clear_screen()
                print(f"=== MODO: {label} ===")
                print(f"Ciclo: {self.current_cycle + 1}/{self.config.total_cycles}")
                print(f"\nTiempo restante: {timer_display}")
                print(self.progress_bar(total_seconds - seconds, total_seconds))
                print("\n[P] Pausar/Reanudar | [Q] Salir")
                
                time.sleep(1)
                seconds -= 1
            else:
                self.clear_screen()
                print(f"=== MODO: {label} (PAUSADO) ===")
                print("\nPresione 'P' para reanudar...")
                time.sleep(0.5)

        if self.running:
            play_beep()

    def start(self):
        """Ciclo de vida de la sesión Pomodoro (Commit 3 y 5)."""
        self.clear_screen()
        print("--- BIENVENIDO AL POMODORO TIMER ---")
        
        # Entrada de usuario (Commit 8)
        try:
            self.config.work_min = int(input("Minutos de trabajo: ") or 25)
            self.config.short_break_min = int(input("Minutos de descanso corto: ") or 5)
        except ValueError:
            print("Entrada no válida, usando valores por defecto.")
            time.sleep(1)

        # Hilo para capturar teclado (Commit 7)
        threading.Thread(target=self.listen_keys, daemon=True).start()

        while self.current_cycle < self.config.total_cycles and self.running:
            # Sesión de Trabajo
            self.countdown(self.config.work_min, "TRABAJO")
            self.current_cycle += 1
            
            if self.current_cycle < self.config.total_cycles and self.running:
                # Determinar tipo de descanso (Commit 5)
                if self.current_cycle % 4 == 0:
                    self.countdown(self.config.long_break_min, "DESCANSO LARGO")
                else:
                    self.countdown(self.config.short_break_min, "DESCANSO CORTO")
            
        if self.running:
            print("\n¡Felicidades! Has completado todas tus sesiones. (Commit 10)")

    def listen_keys(self):
        """Escucha teclas de forma rudimentaria para la terminal (Commit 7)."""
        # Nota: En una app de producción se usaría la librería 'pynput'
        while self.running:
            cmd = input().lower()
            if cmd == 'p':
                self.paused = not self.paused
            elif cmd == 'q':
                self.running = False
                print("\nSaliendo del programa...")
                sys.exit()

# --- EJECUCIÓN ---
if __name__ == "__main__":
    config = Config()
    app = PomodoroApp(config)
    app.start()