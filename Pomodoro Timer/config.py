class Config:
    """
    Maneja las variables de configuración y validación del temporizador Pomodoro.
    """
    def __init__(self):
        """Inicializa los valores por defecto para el flujo de trabajo."""
        self._work_min = 25
        self.short_break_min = 5
        self.long_break_min = 15
        self.total_cycles = 4

    @property
    def work_min(self):
        """Obtiene el valor actual de los minutos de trabajo."""
        return self._work_min

    @work_min.setter
    def work_min(self, value):
        """
        Establece los minutos de trabajo validando que el valor sea positivo.
        
        Args:
            value (int): Minutos a asignar.
        Raises:
            ValueError: Si el valor es menor o igual a cero.
        """
        if value > 0:
            self._work_min = value
        else:
            raise ValueError("El tiempo debe ser mayor a 0")
            
    def validate_positive(self, val):
        """
        Verifica si un valor es un número positivo.
        
        Args:
            val: Valor a validar.
        Returns:
            bool: True si es un número mayor a cero, False en caso contrario.
        """
        return isinstance(val, (int, float)) and val > 0