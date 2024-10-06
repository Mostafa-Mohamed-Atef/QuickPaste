from pynput import mouse, keyboard
import win32gui
# initializing keyboard controller for pressing ctrlv and ctrlc
keyboard_controller = keyboard.Controller()


def pasting():
    try:
        with keyboard_controller.pressed(keyboard.Key.ctrl):
            keyboard_controller.press('v')
            keyboard_controller.release('v')   
            return         
    except Exception as e:
        print(f"An error occurred: {e}")

def pasting_with_terminal():
    try:
        with keyboard_controller.pressed(keyboard.Key.ctrl):
            keyboard_controller.press('shift')
            keyboard_controller.press('v')
            keyboard_controller.release('v') 
            keyboard_controller.release('shift')  
            return         
    except Exception as e:
        print(f"An error occurred: {e}")

def is_terminal_active():
    hwnd = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(hwnd)
    return 'cmd.exe' in window_title or 'PowerShell' in window_title or 'Terminal' in window_title

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.middle:
        if is_terminal_active(): #needs to check double click here 
            pasting_with_terminal()
        else: #needs to release after clicking 
            hwnd = win32gui.GetForegroundWindow()
            win32gui.SetForegroundWindow(hwnd)
            pasting()
    


# Set up the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()