from gui import create_gui
from ttkthemes import ThemedTk


def main():
    window = ThemedTk(theme="breeze")
    create_gui(window)


if __name__ == "__main__":
    create_gui()
