# 🍅 Pomodoro Timer & Proyecto de Prueba

> Documentación unificada del ecosistema Pomodoro: el temporizador principal y su proyecto de prueba de integración.

---

## 📋 Tabla de Contenidos

- [Pomodoro Timer](#pomodorotimer)
  - [Descripción](#descripción)
  - [Estructura del proyecto](#estructuradelproyecto)
  - [Módulos principales](#módulosprincipales)
  - [Tests](#tests)
  - [Documentación técnica](#documentacióntécnica)
  - [Instalación y uso](#instalaciónyuso)
- [Proyecto de Prueba](#proyectodeprueba)
  - [Descripción](#descripción1)
  - [Estructura](#estructura)
  - [Uso](#uso)
- [Requisitos generales](#requisitosgenerales)
- [Licencia](#licencia)

---

# 🍅 Pomodoro Timer

## Descripción

**Pomodoro Timer** es una aplicación multiplataforma de gestión del tiempo basada en la técnica Pomodoro. Permite al usuario alternar entre períodos de trabajo enfocado y descansos, con soporte de notificaciones del sistema y una interfaz configurable.

---

## Estructura del proyecto

```
Pomodoro Timer/
├── docs/
│   ├── asistencia_ia.md
│   ├── Caso Edge.md
│   └── Complejidad Multiplataformas.md
├── tests/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── tests_interface.py
│   │   └── tests_notifications.py
│   ├── __init__.py
│   ├── tests_config.py
│   ├── tests_logic.py
│   └── tests_main.py
├── utils/
│   ├── __init__.py
│   ├── interface.py
│   └── notifications.py
├── __init__.py
├── .gitignore
├── config.py
├── LICENSE
├── logic.py
├── main.py
├── README.md
└── requirements.txt
```

---

## Módulos principales

| Archivo | Descripción |
|---|---|
| `main.py` | Punto de entrada de la aplicación. Inicializa y arranca el temporizador. |
| `logic.py` | Lógica central del temporizador: ciclos Pomodoro, pausas cortas y largas. |
| `config.py` | Parámetros de configuración: duración de sesiones, número de ciclos, preferencias. |
| `utils/interface.py` | Gestión de la interfaz de usuario. |
| `utils/notifications.py` | Envío de notificaciones nativas del sistema operativo. |

---

## Tests

Los tests están organizados bajo `tests/` y cubren los módulos críticos de la aplicación:

| Archivo de test | Módulo cubierto |
|---|---|
| `tests_config.py` | Validación de la configuración |
| `tests_logic.py` | Lógica del temporizador y gestión de ciclos |
| `tests_main.py` | Flujo de inicio de la aplicación |
| `utils/tests_interface.py` | Comportamiento de la interfaz de usuario |
| `utils/tests_notifications.py` | Sistema de notificaciones |

---

## Documentación técnica

La carpeta `docs/` contiene documentación técnica del desarrollo:

| Documento | Contenido |
|---|---|
| `asistencia_ia.md` | Registro del uso de inteligencia artificial durante el desarrollo |
| `Caso Edge.md` | Identificación y manejo de casos borde de la aplicación |
| `Complejidad Multiplataformas.md` | Análisis de la complejidad técnica para soportar múltiples plataformas |

---

## Instalación y uso

**1. Clonar el repositorio:**
```
git clone <url-del-repositorio>
cd pomodoro-timer
```

**2. Instalar dependencias:**
```
pip install -r requirements.txt
```

**3. Ejecutar la aplicación:**
```
python main.py
```

**4. Ejecutar los tests:**
```
python -m pytest tests/
```

---

# 🧪 Proyecto de Prueba

## Descripción

**Proyecto de Prueba** es un entorno de integración diseñado para importar y validar el módulo **Pomodoro Timer** como dependencia externa, verificando su funcionamiento en un contexto de uso real.

---

## Estructura

```
Proyecto de Prueba/
├── __init__.py
├── Pomodoro.py
└── Readme.md
```

| Archivo | Descripción |
|---|---|
| `Pomodoro.py` | Script principal que importa y ejecuta el módulo Pomodoro Timer. |
| `__init__.py` | Inicialización del paquete Python. |
| `Readme.md` | Notas internas del proyecto de prueba. |

---

## Uso

```python
# Ejemplo de integración en Pomodoro.py
from pomodoro_timer import logic, config

# Crear e iniciar una sesión Pomodoro con la configuración por defecto
sesion = logic.PomodoroSession(config.DEFAULT_WORK_TIME)
sesion.start()
```

---

# ⚙️ Requisitos generales

- **Python** 3.14
- Dependencias definidas en `requirements.txt` del proyecto principal

---

# 📄 Licencia

Este proyecto está distribuido bajo los términos definidos en el archivo [`LICENSE`](./LICENSE MIT).