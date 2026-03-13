# 🍅 Pomodoro Timer

A cross-platform Pomodoro Timer application built in Python, featuring desktop notifications, a configurable interface, and comprehensive test coverage.

---

# 📋 Description

This application implements the **Pomodoro Technique**, a time management method that breaks work into focused intervals (traditionally 25 minutes) separated by short breaks. The goal is to improve productivity and reduce mental fatigue.

## Key Features

- ⏱️ Configurable work and break intervals
- 🔔 Desktop notifications when sessions end
- 🖥️ Cross-platform support (Windows, macOS, Linux)
- 🧪 Full test suite covering logic, config, interface, and notifications
- 📁 Modular, clean architecture

---

# 🗂️ Project Structure

```
Pomodoro Timer/
├── main.py                   # Application entry point
├── logic.py                  # Core timer logic
├── config.py                 # Configuration and settings
├── requirements.txt          # Python dependencies
├── .gitignore
├── LICENSE
├── utils/
│   ├── interface.py          # User interface utilities
│   └── notifications.py      # Desktop notification handling
├── tests/
│   ├── tests_config.py       # Config tests
│   ├── tests_logic.py        # Logic tests
│   ├── tests_main.py         # Main module tests
│   └── utils/
│       ├── tests_interface.py
│       └── tests_notifications.py
└── docs/
    ├── asistencia_ia.md              # AI assistance notes
    ├── Caso Edge.md                  # Edge cases documentation
    └── Complejidad Multiplataformas.md  # Cross-platform complexity notes
```

---

# 🚀 Getting Started

## Prerequisites

- Python 3.14

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/pomodoro-timer.git
   cd pomodoro-timer
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the App

```
python main.py
```

---

# ⚙️ Configuration

Timer intervals and other settings can be adjusted in `config.py`. Default values:

| Setting | Default |
|---|---|
| Work session | 25 minutes |
| Short break | 5 minutes |
| Long break | 15 minutes |
| Sessions before long break | 4 |

---

# 🧪 Running Tests

```
python -m pytest tests/
```

Or run a specific test file:

```
python -m pytest tests/tests_logic.py
```

---

# 📚 Documentation

Additional documentation is available in the [`docs/`](docs/) folder:

- **`asistencia_ia.md`** — Notes on AI-assisted development
- **`Caso Edge.md`** — Edge cases and how they are handled
- **`Complejidad Multiplataformas.md`** — Notes on cross-platform compatibility challenges

---

# 📄 License

This project is licensed under the terms specified in the [LICENSE](LICENSE MIT) file.