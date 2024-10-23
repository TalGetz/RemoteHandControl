from pywinauto import Desktop

dlg_desktop = Desktop(backend="uia").window(title = "Netflix", visible_only=False)
