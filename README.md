# Sistema de Gestión de Reservas 🏫

Un programa de consola (CLI) sencillo y eficiente para gestionar el préstamo de salas, construido con **Python** y **SQLAlchemy**. Los datos se almacenan de forma local mediante SQLite.

## 🚀 Características

- **Gestión de Salas:** Registra nuevas salas y define su capacidad.
- **Control de Disponibilidad:** Revisa qué salas están libres u ocupadas.
- **Sistema de Reservas:** Asigna una sala a un estudiante en una fecha específica (la sala pasa a estar "No disponible").
- **Cancelaciones:** Elimina reservas y libera automáticamente la sala para que pueda volver a usarse.

## 🛠️ Tecnologías utilizadas

- Python 3
- SQLAlchemy 2.0 (ORM)
- SQLite (Base de datos)

## 📦 Instalación y Ejecución

1. Clona este repositorio o abre el proyecto en tu entorno (como GitHub Codespaces).
2. Instala las dependencias requeridas usando el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt

3. luego de tener esto instalado ejecuta este comando
   ```bash
   python main.py