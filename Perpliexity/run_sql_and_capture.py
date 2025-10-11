def run_sql_and_capture(sql: str, screenshot_path: str, window):
    import time
    import pyperclip
    import pyautogui
    import keyboard

    # Paste and execute
    pyperclip.copy(sql)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "enter")
    keyboard.wait('enter')  # wait for your Enter press

    # Screenshot
    img = pyautogui.screenshot(region=window.box)
    img.save(screenshot_path)

    # Inject “Screenshot taken” comment in editor
    pyautogui.click(x=300, y=200)  # adjust to SQL editor position
    time.sleep(0.2)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    note = f"-- Screenshot taken at {timestamp}\n"
    pyperclip.copy(note)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)

    # Clear original SQL for next run
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    time.sleep(0.5)
