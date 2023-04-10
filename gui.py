from tkinter import ttk, filedialog, StringVar
from image_converter import start_conversion
from tkinter.font import Font


def create_gui(window):
    window.title("图片格式转换器")
    window.geometry("500x230")  # 设置窗口大小
    custom_font = Font(family="微软雅黑", size=10, weight="bold")

    # 设置按钮样式
    button_style = ttk.Style()
    button_style.configure("Custom.TButton", font=custom_font)

    ttk.Label(window, text="输入文件夹:", font=custom_font).grid(row=0, column=0, padx=5, pady=5, sticky="E")
    ttk.Label(window, text="输出文件夹:", font=custom_font).grid(row=1, column=0, padx=5, pady=5, sticky="E")
    ttk.Label(window, text="输出格式:", font=custom_font).grid(row=3, column=0, padx=5, pady=5, sticky="E")

    input_folder_var = StringVar()
    output_folder_var = StringVar()
    status_var = StringVar()
    status_var.set("请选择路径及目标格式")

    ttk.Entry(window, textvariable=input_folder_var).grid(row=0, column=1, padx=5, pady=5, sticky="WE")
    ttk.Entry(window, textvariable=output_folder_var).grid(row=1, column=1, padx=5, pady=5, sticky="WE")

    formats = ["JPG", "JPEG", "PNG", "GIF", "BMP", "ICO", "TIFF", "WEBP"]

    output_format_var = StringVar()
    output_format_var.set(formats[0])
    output_format_menu = ttk.OptionMenu(window, output_format_var, *formats)
    output_format_menu.grid(row=3, column=1, padx=5, pady=5, sticky="WE")

    ttk.Button(window, text="浏览", command=lambda: browse_folder(input_folder_var), style="Custom.TButton"). \
        grid(row=0,
             column=2,
             padx=5,
             pady=5,
             sticky="W")
    ttk.Button(window, text="浏览", command=lambda: browse_folder(output_folder_var), style="Custom.TButton"). \
        grid(row=1,
             column=2,
             padx=5,
             pady=5,
             sticky="W")
    ttk.Button(window, text="开始转换",
               command=lambda: start_conversion(input_folder_var, output_folder_var,
                                                output_format_var, status_var, progress_bar),
               style="Custom.TButton"). \
        grid(row=4,
             column=0,
             columnspan=3,
             padx=5,
             pady=5,
             sticky="WE")

    # 添加进度条
    progress_bar = ttk.Progressbar(window, length=400, mode='determinate')
    progress_bar.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="WE")

    status_label = ttk.Label(window, textvariable=status_var, font=custom_font, anchor="center")
    status_label.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky="WE")

    window.columnconfigure(1, weight=1)
    window.mainloop()


def browse_folder(folder_var):
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)
