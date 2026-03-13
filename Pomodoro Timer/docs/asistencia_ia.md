# Asistencia de IA - Pomodoro Timer
Este documento detalla el uso de herramientas de Inteligencia Artificial para el desarrollo, mantenimiento y expansión de este proyecto.

## 1. Contexto del Proyecto
El Pomodoro Timer es una aplicación modular escrita en Python. Para que la IA brinde respuestas precisas, es crucial proporcionarle la estructura actual:

main.py: Punto de entrada de la aplicación.

logic.py: Motor de tiempos y estados del Pomodoro.

interface.py: Manejo de la UI (User Interface).

notifications.py: Sistema de alertas y sonidos.

utils/: Funciones auxiliares de configuración y sistema.

## 2. Cómo Solicitar Asistencia
Al interactuar con una IA para este proyecto, se recomienda usar el siguiente formato de Prompt:

"Estoy trabajando en un proyecto de Python llamado Pomodoro Timer. La estructura es modular. Necesito [ayuda/una nueva función/corregir un error] en el archivo [nombre_del_archivo.py]. El comportamiento actual es [X] y espero que sea [Y]."

Ejemplos de uso:
Para depuración: "La notificación no suena en Linux. Revisa notifications.py y sugiera una librería multiplataforma compatible."

Para nuevas funciones: "Quiero añadir un contador de ciclos completados en logic.py. ¿Cómo debería actualizar el estado?"

## 3. Guía de Uso del Temporizador (Ejemplos)
Para documentar el uso técnico, aquí tienes ejemplos de cómo se invocan las funciones principales:

Inicio de una sesión estándar
Python
from logic import PomodoroLogic

- Instanciar la lógica con 25 min de trabajo y 5 min de descanso:

timer = PomodoroLogic(work_time=25, break_time=5)
timer.start()
Configuración personalizada
Si se desea modificar los parámetros desde config.py:

Python
import config

def cargar_preferencias():
    # Ejemplo de cómo la IA sugiere cargar configuraciones externas
    settings = config.load_user_settings()
    print(f"Temporizador configurado para: {settings['work_duration']} min.")

## 4. Notas de Complejidad Multiplataforma
Este proyecto presta especial atención a la compatibilidad. Al pedir cambios en la interfaz o notificaciones, asegúrate de mencionar que debe funcionar en Windows, macOS y Linux, evitando dependencias que solo funcionen en una terminal específica.