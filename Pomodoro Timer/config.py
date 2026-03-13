class Config:
    """Maneja las variables configurables del temporizador."""
    def __init__(self):
        """Inicializa los valores por defecto para las sesiones de Pomodoro."""
        self.work_min = 25
        self.short_break_min = 5
        self.long_break_min = 15
        self.total_cycles = 4

    def validate_positive(self, val):
        """
        Valida que un valor numérico sea estrictamente positivo.
        
        Args:
            val (int/float): El valor a validar.
            
        Returns:
            bool: True si es mayor a cero, False en caso contrario.
        """
        return val > 0