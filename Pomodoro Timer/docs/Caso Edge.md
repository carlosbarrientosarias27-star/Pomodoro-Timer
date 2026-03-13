## 🛡️ Reporte de Pruebas: Casos de Borde (Edge Cases)

| Escenario | Comportamiento Actual | Riesgo / Resultado | Sugerencia de Mejora |
| :--- | :--- | :--- | :--- |
| **0 Ciclos** | El bucle `while` en `start()` no se ejecuta. | La app termina inmediatamente sin mensajes de error. | Validar que `total_cycles` sea > 0 antes de iniciar. |
| **Valores Negativos** | `countdown` recibe minutos negativos. | El bucle `while seconds > 0` no entra y el ciclo termina al instante. | Aplicar `validate_positive()` antes de asignar los inputs. |
| **Valores Gigantes** | Acepta cualquier entero (ej. 1,000,000 min). | Riesgo de overflow visual en la barra de progreso o sesiones inhumanas. | Implementar un límite máximo (Cap) razonable en la configuración. |
| **Input No Numérico** | Capturado por `try-except` en `start()`. | Funciona bien, pero usa valores por defecto sin avisar claramente cuál falló. | Notificar al usuario específicamente qué valor fue invalidado. |
| **Entrada Vacía** | Usa el operador `or` para asignar valores por defecto. | **Correcto.** Es una implementación elegante para una UX rápida. | Mantener comportamiento actual. |