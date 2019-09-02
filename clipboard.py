import win32clipboard

def get_clipboard():
    win32clipboard.OpenClipboard()
    link = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return link

def set_clipboard(summary):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(summary)
    win32clipboard.CloseClipboard()
