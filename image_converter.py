import os
import tempfile
from tkinter import messagebox

from PIL import Image
import threading


def convert_image(input_path, output_path, output_format=None):
    try:
        image = Image.open(input_path)

        if output_format is None:
            output_format = os.path.splitext(output_path)[1].lstrip('.').upper()

        is_saved = False

        if image.format == "WEBP" and output_format.upper() == "GIF":
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
            temp_png_path = temp_file.name

            image.save(temp_png_path, "PNG")

            temp_file.close()

            image = Image.open(temp_png_path)
            image = image.convert("RGBA")
            image.save(output_path, output_format)
            is_saved = True

            # 删除临时 PNG 文件
            if os.path.exists(temp_png_path):
                os.remove(temp_png_path)

        if not is_saved:
            if output_format == "JPEG" and image.mode != "RGB":
                image = image.convert("RGB")
            image.save(output_path, output_format)

        return True

    except Exception as e:
        print(f"转换过程中发生错误: {e}")
        return False


def start_conversion(input_folder_var, output_folder_var, output_format_var, status_var, progress_bar):
    conversion_thread = threading.Thread(target=start_conversion_threaded, args=(input_folder_var, output_folder_var,
                                                                                 output_format_var, status_var,
                                                                                 progress_bar))
    conversion_thread.start()


def start_conversion_threaded(input_folder_var, output_folder_var, output_format_var, status_var, progress_bar):
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    output_format = output_format_var.get().upper()

    if not os.path.exists(input_folder):
        messagebox.showinfo("提示", "请选择输入文件夹!!")
        return

    if not os.path.exists(output_folder):
        messagebox.showinfo("提示", "请选择输出文件夹!!")
        return

    if output_format == "请选择格式".upper():
        messagebox.showinfo("提示", "请选择输出格式!!")
        return

    if output_format == "JPG":
        output_format = "JPEG"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_list = os.listdir(input_folder)
    total_files = len(file_list)
    success_count = 0

    progress_bar.configure(maximum=total_files, value=0)  # 设置进度条的最大值为 total_files

    for index, file in enumerate(file_list):
        try:
            input_file_path = os.path.join(input_folder, file)
            output_file_name = os.path.splitext(file)[0] + "." + output_format.lower()
            output_file_path = os.path.join(output_folder, output_file_name)

            if convert_image(input_file_path, output_file_path, output_format):
                success_count += 1
                status_var.set(f"已成功转换 {success_count} 个文件！")
                progress_bar.step()  # 每成功转换一个文件，更新进度条

        except Exception as e:
            status_var.set(f"转换过程中发生错误: {e}")
            return

    status_var.set(f"完成，已成功转换 {success_count} 个文件！")
    progress_bar.configure(value=progress_bar.cget('maximum'))  # 保持进度条为满
