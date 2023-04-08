from tkinter import ttk, filedialog, StringVar
from image_converter import start_conversion
from tkinter.font import Font


def create_gui(window):
    custom_font = Font(family="微软雅黑", size=10, weight="bold")
    button_style = ttk.Style()
    button_style.configure("Custom.TButton", font=custom_font)  # 设置按钮样式

    ttk.Label(window, text="输入文件夹:", font=custom_font).grid(row=0, column=0, padx=5, pady=5, sticky="E")
    ttk.Label(window, text="输出文件夹:", font=custom_font).grid(row=1, column=0, padx=5, pady=5, sticky="E")
    ttk.Label(window, text="输入格式:", font=custom_font).grid(row=2, column=0, padx=5, pady=5, sticky="E")
    ttk.Label(window, text="输出格式:", font=custom_font).grid(row=3, column=0, padx=5, pady=5, sticky="E")

    input_folder_var = StringVar()
    output_folder_var = StringVar()
    status_var = StringVar()

    ttk.Entry(window, textvariable=input_folder_var).grid(row=0, column=1, padx=5, pady=5, sticky="WE")
    ttk.Entry(window, textvariable=output_folder_var).grid(row=1, column=1, padx=5, pady=5, sticky="WE")

    formats = ["JPG", "JPEG", "PNG", "GIF", "BMP", "ICO", "TIFF", "WEBP"]

    input_format_var = StringVar()
    input_format_var.set(formats[0])
    input_format_menu = ttk.OptionMenu(window, input_format_var, *formats)
    input_format_menu.grid(row=2, column=1, padx=5, pady=5, sticky="WE")

    output_format_var = StringVar()
    output_format_var.set(formats[0])
    output_format_menu = ttk.OptionMenu(window, output_format_var, *formats)
    output_format_menu.grid(row=3, column=1, padx=5, pady=5, sticky="WE")

    ttk.Button(window, text="浏览", command=lambda: browse_folder(input_folder_var), style="Custom.TButton").\
        grid(row=0,
             column=2,
             padx=5,
             pady=5,
             sticky="W")
    ttk.Button(window, text="浏览", command=lambda: browse_folder(output_folder_var), style="Custom.TButton").\
        grid(row=1,
             column=2,
             padx=5,
             pady=5,
             sticky="W")
    ttk.Button(window, text="开始转换",
               command=lambda: start_conversion(input_folder_var, output_folder_var, input_format_var,
                                                output_format_var, status_var), style="Custom.TButton").\
        grid(row=4,
             column=0,
             columnspan=3,
             padx=5,
             pady=5,
             sticky="WE")

    ttk.Label(window, textvariable=status_var, relief="sunken", borderwidth=2, font=custom_font).\
        grid(row=5, column=0,
             columnspan=3,
             padx=5, pady=5,
             sticky="WE")

    window.columnconfigure(1, weight=1)
    window.mainloop()


def browse_folder(folder_var):
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)
