import os
import platform 

def clear_screen(self):
        """Limpia la terminal según el SO (Commit 8)."""
        os.system('cls' if platform.system() == 'Windows' else 'clear')

def progress_bar(self, current, total, length=30):
        """Genera una barra de progreso visual (Commit 8)."""
        percent = float(current) / total
        arrow = '█' * int(round(percent * length))
        spaces = ' ' * (length - len(arrow))
        return f"[{arrow}{spaces}] {int(percent * 100)}%"