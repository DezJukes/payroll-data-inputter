import csv
import time
import pyautogui
import keyboard  # For detecting key press
import pyperclip
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

pyautogui.FAILSAFE = True

# Global variable to manage the automation process
is_running = False
file_path = ""  # To store the selected file path

# Function to browse and select a CSV file
def browse_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        file_path_label.config(text=f"Selected File: {file_path}")
        start_button.config(state="normal")

# Function for the automation process
def automate_csv():
    global is_running, file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return

    is_running = True
    progress_label.config(text="Automation in progress...")
    stop_button.config(state="normal")
    start_button.config(state="disabled")

    # Open your CSV file
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)

        # Give yourself some time to open the app and place cursor
        time.sleep(15)

        for row in reader:
            if not is_running:
                break

            account_num = row[0]
            employee_name = row[1]
            payroll_amount = row[2]

            # Click or tab to the Account Number field and type
            pyautogui.click(x=937, y=507)  # Update with your coordinates
            pyautogui.write(account_num)

            pyautogui.press('tab')
            pyperclip.copy(employee_name)
            pyautogui.hotkey("ctrl", "v")

            # Tab or click to Payroll Amount
            pyautogui.press('tab')
            pyautogui.write(payroll_amount)

            # Click Save button (or press Enter)
            pyautogui.press('tab')  # If tab goes to Save button
            pyautogui.press('enter')

            # Wait for the form to reset or process
            time.sleep(1)

    is_running = False
    progress_label.config(text="Automation completed.")
    stop_button.config(state="disabled")
    start_button.config(state="normal")

# Function to stop the automation
def stop_automation():
    global is_running
    is_running = False
    progress_label.config(text="Automation stopped.")
    stop_button.config(state="disabled")
    start_button.config(state="normal")

# Creating the main GUI window
root = tk.Tk()
root.title("CSV Automation Tool")
root.geometry("400x300")

# Make the window always stay on top
root.attributes("-topmost", True)

# File selection section
file_path_label = tk.Label(root, text="No file selected.")
file_path_label.pack(pady=10)

browse_button = tk.Button(root, text="Browse CSV File", command=browse_file)
browse_button.pack(pady=5)

# Progress and control buttons
progress_label = tk.Label(root, text="Progress: Not started")
progress_label.pack(pady=10)

start_button = tk.Button(root, text="Start Automation", state="disabled", command=lambda: threading.Thread(target=automate_csv).start())
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Automation", state="disabled", command=stop_automation)
stop_button.pack(pady=5)

# Run the GUI loop
root.mainloop()