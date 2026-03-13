import csv
import time
import pyautogui
import keyboard  # For detecting key press
import pyperclip

pyautogui.FAILSAFE = True

# Open your CSV file
with open(r'C:\Users\TREAS02\Documents\test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    # Give yourself some time to open the app and place cursor
    print("Switch to the app within 15 seconds...")
    time.sleep(15)

    for row in reader:
        if keyboard.is_pressed('ctrl+j'):
            print("Stopping the automation...")
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

print("Automation completed.")

