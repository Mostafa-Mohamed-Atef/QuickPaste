from pynput import mouse, keyboard
import win32gui

# initializing keyboard controller for pressing ctrlv and ctrlc
keyboard_controller = keyboard.Controller()

# copying function by pressing ctrlc shortcut
def send_ctrl_c():
    try:
        keyboard_controller.press(keyboard.Key.ctrl)
        keyboard_controller.press('c')
        keyboard_controller.release('c')
        keyboard_controller.release(keyboard.Key.ctrl)
            
    except Exception as e:
        print(f"An error occurred: {e}")

def on_click(x, y, button, pressed):
    # for copying from any window it recognizes the window that is on the top priority 
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetForegroundWindow(hwnd)
    send_ctrl_c()
    if button == mouse.Button.middle and pressed:
        try:
            keyboard_controller.press(keyboard.Key.ctrl)
            keyboard_controller.press('v')
            keyboard_controller.release('v')
            keyboard_controller.release(keyboard.Key.ctrl)
            
        except Exception as e:
            print(f"An error occurred: {e}")

# Set up the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()