# payroll-data-inputter

A lightweight desktop utility built in Python with a Tkinter GUI to automate repetitive form data entry from CSV files using `pyautogui` and `pyperclip`.

## Features

- **Tkinter GUI:** Simple interface with file picker and status display.
- **Multithreaded Execution:** Background thread handling ensures the GUI stays responsive during execution.
- **Fail-Safe Ready:** Uses `pyautogui.FAILSAFE = True` (slam cursor into any screen corner to abort immediately).
- **Clipboard Injection:** Uses clipboard pasting for Unicode support across arbitrary character encodings (names, accents, special characters).
- **Error Recovery Reporting:** Shows the failing row alongside the last successful entry if an interruption occurs.

---

## Prerequisites

- **Python 3.8+**
- On Linux (Ubuntu/Debian), Tkinter and scrot/xclip dependencies may need to be installed manually:
  ```bash
  sudo apt-get install python3-tk xclip scrot
  ```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DezJukes/payroll-data-inputter
   cd payroll-data-inputter
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration & Usage

### 1. CSV Format
Ensure your CSV is formatted with columns ordered as follows:
```csv
Account Number,Employee Name,Payroll Amount
12345678,Jane Doe,4500.00
87654321,John Smith,5200.50
```

### 2. Screen Coordinates
Because screen resolutions vary, update the click coordinates in `main.py` before running:

```python
# Line inside automate_csv():
pyautogui.click(x=937, y=507)  # Replace with the (x, y) coordinates of your first input field
```

> **Tip:** You can find your current mouse position by running this in Python:
> ```python
> import pyautogui
> print(pyautogui.position())
> ```

### 3. Running the App
```bash
python main.py
```

1. Click **Browse CSV File** and select your target data.
2. Click **Start Automation**.
3. You will have **15 seconds** to switch to your destination application and position your active window.
4. To stop the automation immediately:
   - Click **Stop Automation** in the app, or
   - Push the mouse cursor forcefully into any **screen corner** to activate the PyAutoGUI fail-safe.

---

## Project Structure

```text
├── main.py              # Main application entry point & GUI
├── requirements.txt     # Third-party dependencies
├── .gitignore           # Git ignore patterns
└── README.md            # Documentation
```