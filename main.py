from pynput import mouse, keyboard
import win32gui
import time
import win32clipboard
# initializing keyboard controller for pressing ctrlv and ctrlc
keyboard_controller = keyboard.Controller()

def clear_clipboard():
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()
    except Exception as e:
        print(f"An error occurred: {e}")
# copying function by pressing ctrlc shortcut
def copying():
    try:
        with keyboard_controller.pressed(keyboard.Key.ctrl):
            keyboard_controller.press('c')  
            keyboard_controller.release('c')   

        win32clipboard.OpenClipboard()
        formats = []
        current_format = 0
        while True:
            next_format = win32clipboard.EnumClipboardFormats(current_format)
            if next_format == 0:
                break
            formats.append(next_format)
            current_format = next_format
        win32clipboard.CloseClipboard()
        
        if len(formats) > 10:
            clear_clipboard()
    except Exception as e:
        print(f"An error occurred: {e}")


    except Exception as e:
        print(f"An error occurred: {e}")


def pasting():
    try:
        with keyboard_controller.pressed(keyboard.Key.ctrl):
            keyboard_controller.press('v')
            keyboard_controller.release('v')   
            return         
    except Exception as e:
        print(f"An error occurred: {e}")


def on_click(x, y, button, pressed):
    if not pressed:
        if button == mouse.Button.left: #needs to check double click here 
            hwnd = win32gui.GetForegroundWindow()
            win32gui.SetForegroundWindow(hwnd)
            copying()
            time.sleep(0.1)
    elif pressed and button == mouse.Button.middle: #needs to release after clicking 
        pasting()
    


# Set up the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()