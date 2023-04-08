from gui import create_gui
from ttkthemes import ThemedTk


def main():
    window = ThemedTk(theme="breeze")  # 使用 "breeze" 主题
    # window.iconbitmap("your_icon.ico")  # 设置窗口图标
    window.title("图片格式转换器")
    window.geometry("500x250")  # 设置窗口大小

    # 调用 create_gui 函数创建图形界面
    create_gui(window)

    # 运行主循环
    window.mainloop()


if __name__ == "__main__":
    main()
