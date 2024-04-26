import io


class Files:
    def __init__(self):
        pass

    @staticmethod
    def to_blob_format(file_path):
        file_object = open(file_path, "rb")
        binary_file = file_object.read()
        return binary_file

    @staticmethod
    def from_blob_format(binary_file):
        file_stream = io.BytesIO(binary_file)
        file = file_stream.read()
        return file
