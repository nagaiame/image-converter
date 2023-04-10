from gui import create_gui
from ttkthemes import ThemedTk


def main():
    window = ThemedTk(theme="breeze")  # 使用 "breeze" 主题
    create_gui(window)  # 调用 create_gui 函数创建图形界面


if __name__ == "__main__":
    main()
