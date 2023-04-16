import os
from tkinter import ttk, filedialog, StringVar, messagebox, OptionMenu
from image_converter import start_conversion
from tkinter.font import Font
from tkinterdnd2 import *


def create_gui():
    window = TkinterDnD.Tk()
    window.title("图片格式转换器")
    window.geometry("500x230")  # 设置窗口大小
    custom_font = Font(family="微软雅黑", size=10, weight="bold")

    button_style = ttk.Style()
    button_style.configure("TButton", font=custom_font)

    menu_style = ttk.Style()

    menu_style.configure("Custom.TMenubutton",
                         background="#e1e1e1",
                         font=custom_font)
    menu_style.configure("Custom.TEntry", font=custom_font)

    ttk.Label(window, text="输入文件夹:", font=custom_font).grid(row=0, column=0, padx=5, pady=5, sticky="E")
    ttk.Label(window, text="输出文件夹:", font=custom_font).grid(row=1, column=0, padx=5, pady=5, sticky="E")
    ttk.Label(window, text="输出格式:", font=custom_font).grid(row=3, column=0, padx=5, pady=5, sticky="E")

    input_folder_var = StringVar()
    output_folder_var = StringVar()
    status_var = StringVar()
    status_var.set("请选择路径及目标格式(支持拖放)")

    input_entry = ttk.Entry(window, textvariable=input_folder_var, style="Custom.TEntry")
    input_entry.grid(row=0, column=1, padx=5, pady=5, sticky="WE")
    input_entry.drop_target_register(DND_FILES, DND_TEXT)
    input_entry.dnd_bind('<<Drop>>', lambda event: on_dnd_drop(event, input_folder_var))

    output_entry = ttk.Entry(window, textvariable=output_folder_var, style="Custom.TEntry")
    output_entry.grid(row=1, column=1, padx=5, pady=5, sticky="WE")
    output_entry.drop_target_register(DND_FILES, DND_TEXT)
    output_entry.dnd_bind('<<Drop>>', lambda event: on_dnd_drop(event, output_folder_var))

    formats = ["请选择格式", "JPG", "JPEG", "PNG", "GIF", "BMP", "ICO", "TIFF", "WEBP"]

    output_format_var = StringVar()
    output_format_var.set(formats[0])  # 将默认值设置为 "JPG"
    output_format_menu = ttk.OptionMenu(window, output_format_var, *formats, style="Custom.TMenubutton")
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
        grid(row=6,
             column=0,
             columnspan=3,
             padx=5,
             pady=5,
             sticky="S")

    progress_bar = ttk.Progressbar(window, length=400, mode='determinate')
    progress_bar.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="WE")

    status_label = ttk.Label(window, textvariable=status_var, font=custom_font, anchor="center")
    status_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="WE")

    window.columnconfigure(1, weight=1)
    window.mainloop()


def browse_folder(folder_var):
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)


def on_dnd_drop(event, folder_var):
    folder_path = event.data
    if os.path.isdir(folder_path):
        folder_var.set(folder_path)
    else:
        messagebox.showwarning("无效的文件夹", "请拖放一个文件夹。")

    return event.action
