# MyRoutineApp

MyRoutineApp is a Python-based daily routine manager application that helps users manage their daily tasks and select a salad suggestion each day. It features a modern blue-themed GUI and can be launched as an application on Ubuntu.

## Features
- **Daily Routine Management**: Displays a list of daily tasks and allows the user to mark them as completed.
- **Salad Suggestion**: Randomly selects a salad from a PDF and ensures no repetition for at least 5 days.
- **Blue Workout Theme**: The app has a modern workout-themed design with a blue color scheme.
- **Ubuntu Application**: Can be launched like any other app from the Ubuntu app menu.

## Screenshots
*Coming soon!*

## Requirements

- Python 3.x
- Tkinter (for the GUI)
- PyMuPDF (for PDF handling)
- Ubuntu or any Linux-based system

## Installation

1. **Clone the repository**:
   ```bash```
   git clone https://github.com/saidharshan01/MyRoutineApp.git
   cd MyRoutineApp

## Set up the virtual environment:

```bash```

      python3 -m venv .venv
      source .venv/bin/activate

**Install the required packages:**

```bash```

      pip install -r requirements.txt

Set up the application for Ubuntu:

Create a .desktop file to launch the app from the menu:

```bash```

      nano ~/.local/share/applications/MyRoutineApp.desktop

**Add the following content:**

ini

    [Desktop Entry]
    Version=1.0
    Name=MyRoutineApp
    Comment=Manage your daily routine
    Exec=bash -c 'source /path/to/your/project/.venv/bin/activate && python /path/to/your/project/app.py'
    Icon=/path/to/your/project/icon.png
    Terminal=false
    Type=Application
    Categories=Utility;

Replace /path/to/your/project/ with the actual path to the project.

**Run the application:**

    You can now run the application from the terminal:

    ```bash```

      python app.py

Or launch it from the Ubuntu app menu.
# MyRoutineApp
