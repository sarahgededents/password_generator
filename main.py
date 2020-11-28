import center_tk_window
from ui.generate_password import GeneratePassword
from ttkthemes import ThemedTk

def make_root_window():
    root = ThemedTk(theme="arc")
    root.title("Password Generator")
    GeneratePassword(root)
    root.resizable(False, False)
    return root

def main():
    root = make_root_window()
    center_tk_window.center_on_screen(root)
    root.mainloop()


if __name__ == '__main__':
    main()