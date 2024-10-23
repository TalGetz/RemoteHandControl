import time

from pywinauto import Desktop

dlg_desktop = Desktop('uia').window(title = "Netflix", visible_only=False)
dlg_desktop.print_control_identifiers()

time.sleep(1)

print(dir(dlg_desktop.Hyperlink11.invoke()))
