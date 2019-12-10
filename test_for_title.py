import win32api
import win32gui

trade_main_hwnd = win32gui.FindWindow(0, "FullGenMainFrame")
win32api.PostMessage(trade_main_hwnd, 0x0111, 32860, 0)
