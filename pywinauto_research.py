from pywinauto import Desktop

app = Desktop(backend="uia").window(title="Netflix", visible_only=False)
print(app.Properties.print_control_identifiers())