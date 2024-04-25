import io
from PIL import Image


def icon_for_db(image_filename):
    image_file_obj = open(image_filename, "rb")
    image_binary_bytes = image_file_obj.read()
    image_stream = io.BytesIO(image_binary_bytes)
    image_file = Image.open(image_stream)
    return image_file
