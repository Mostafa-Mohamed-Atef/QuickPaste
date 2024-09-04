from pynput import mouse, keyboard
import win32gui
import time
# initializing keyboard controller for pressing ctrlv and ctrlc
keyboard_controller = keyboard.Controller()

# copying function by pressing ctrlc shortcut
def copying():
    try:
        with keyboard_controller.pressed(keyboard.Key.ctrl):
            keyboard_controller.press('c')  
            keyboard_controller.release('c')            
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
    if pressed:
        if button == mouse.Button.left: #needs to check double click here 
            hwnd = win32gui.GetForegroundWindow()
            win32gui.SetForegroundWindow(hwnd)
            copying()
            time.sleep(0.1)
        elif button == mouse.Button.middle: #needs to release after clicking 
            pasting()


# Set up the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()