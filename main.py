from pynput import mouse, keyboard
import ctypes
import win32gui
import win32con
import win32api
import win32clipboard

# Get the handle of the active window
hwnd = win32gui.GetForegroundWindow()
# Send Ctrl+C to the active window (to copy selected text)
def send_ctrl_c():
    # Simulate key down for Ctrl
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    # Simulate key press for 'C'
    win32api.keybd_event(0x43, 0, 0, 0)
    # Simulate key release for 'C'
    win32api.keybd_event(0x43, 0, win32con.KEYEVENTF_KEYUP, 0)
    # Simulate key release for Ctrl
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)


# Now, let's read the clipboard

def get_clipboard_text():
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
        data = ""
    finally:
        win32clipboard.CloseClipboard()
    return data

send_ctrl_c()
get_clipboard_text()


# Create a keyboard controller

def on_click(x, y, button, pressed):
    if button == mouse.Button.middle and pressed:
        try:
            keyboard_controller.press(keyboard.Key.ctrl)
            keyboard_controller.press('v')
            keyboard_controller.release('v')
            keyboard_controller.release(keyboard.Key.ctrl)
            
        except Exception as e:
            print(f"An error occurred: {e}")

keyboard_controller = keyboard.Controller()
# Set up the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
