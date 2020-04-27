import win32api
import win32con
import win32gui
import redis

FullGenMessage = win32gui.RegisterWindowMessage("FullGenReport")
connection = redis.Redis(host="127.0.0.1", port=6379, db=1)


def main():
    hInstance = win32api.GetModuleHandle()
    className = 'SimpleWin32'
    wndClass = win32gui.WNDCLASS()
    wndClass.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
    wndClass.lpfnWndProc = wndProc
    wndClass.hInstance = hInstance
    wndClass.hIcon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
    wndClass.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
    wndClass.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)
    wndClass.lpszClassName = className

    try:
        wndClassAtom = win32gui.RegisterClass(wndClass)
    except Exception as e:
        raise e

    hWindow = win32gui.CreateWindow(
        wndClassAtom,
        'FullGenReport',
        win32con.WS_OVERLAPPEDWINDOW,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        None,
        None,
        hInstance,
        None)

    win32gui.ShowWindow(hWindow, win32con.SW_SHOWNORMAL)
    win32gui.UpdateWindow(hWindow)
    win32gui.PumpMessages()


def wndProc(hWnd, message, wParam, lParam):
    if message == win32con.WM_PAINT:
        hDC, paintStruct = win32gui.BeginPaint(hWnd)
        rect = win32gui.GetClientRect(hWnd)
        win32gui.DrawText(
            hDC,
            'Hello send by Python via Win32!',
            -1,
            rect,
            win32con.DT_SINGLELINE | win32con.DT_CENTER | win32con.DT_VCENTER)

        win32gui.EndPaint(hWnd, paintStruct)
        return 0
    elif message == win32con.WM_DESTROY:
        win32gui.PostQuitMessage(0)
        return 0
    elif message == FullGenMessage:
        connection.set("wParam", str(wParam))
        connection.set("lParam", str(lParam))
        return 0
    else:
        return win32gui.DefWindowProc(hWnd, message, wParam, lParam)


if __name__ == '__main__':
    main()
