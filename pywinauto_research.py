from pywinauto import Desktop

from pywinauto.application import Application
app = Application(backend="uia").start('Netflix.exe')


# app = Desktop(backend="uia").window(title="Netflix", visible_only=False)
print(app.Properties.print_control_identifiers())