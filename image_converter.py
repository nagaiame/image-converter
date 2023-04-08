import os
from PIL import Image


def convert_image(input_path, output_path, output_format=None):
    try:
        image = Image.open(input_path)

        if output_format is None:
            output_format = os.path.splitext(output_path)[1].lstrip('.').upper()

        image.save(output_path, output_format)
        return True

    except Exception as e:
        print(f"转换过程中发生错误: {e}")
        return False


def batch_convert_images(input_folder, output_folder, input_format, output_format):
    if not os.path.exists(input_folder):
        print(f"错误：输入文件夹 {input_folder} 不存在。")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(input_format.lower()):
            input_path = os.path.join(input_folder, filename)
            basename, _ = os.path.splitext(filename)
            output_path = os.path.join(output_folder, f"{basename}.{output_format.lower()}")

            if convert_image(input_path, output_path, output_format):
                print(f"图片 {filename} 已成功转换为 {os.path.basename(output_path)}")


def start_conversion(input_folder_var, output_folder_var, input_format_var, output_format_var, status_var):
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    input_format = input_format_var.get().lower()
    output_format = output_format_var.get().upper()

    if output_format == "JPG":
        output_format = "JPEG"

    if not os.path.exists(input_folder):
        status_var.set("输入文件夹不存在！")
        return

    success_count = 0  # 初始化 success_count 变量

    for file in os.listdir(input_folder):
        if file.lower().endswith(input_format):
            try:
                input_file_path = os.path.join(input_folder, file)
                output_file_name = os.path.splitext(file)[0] + "." + output_format.lower()
                output_file_path = os.path.join(output_folder, output_file_name)

                img = Image.open(input_file_path)

                if output_format == "JPEG" and img.mode == "RGBA":
                    img = img.convert("RGB")

                img.save(output_file_path, output_format)
                success_count += 1  # 图像转换成功，递增 success_count
            except Exception as e:
                status_var.set(f"转换过程中发生错误: {e}")
                return

    status_var.set(f"已成功转换 {success_count} 个文件！")
