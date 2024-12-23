from PIL import Image
import os

def convert_dpi(filename, output_image_path):
    """
    将指定图像的dpi从96转换为300
    :param input_image_path: 输入图像的路径
    :param output_image_path: 输出图像的路径
    """
    image = Image.open(filename)
    # width, height = image.size
    # new_width = int(width * (300 / 96))
    # new_height = int(height * (300 / 96))
    # image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    image.save(output_image_path, dpi=(300, 300), quality=100)


if __name__ == "__main__":
    os.makedirs('300dpi', exist_ok=True)
    for file in os.listdir('./'):
        if file.endswith('.jpg'):
            output_file_path = os.path.join('./300dpi', file)
            convert_dpi(file, output_file_path)