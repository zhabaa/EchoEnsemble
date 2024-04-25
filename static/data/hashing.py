import hashlib
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Hashing:
    def __init__(self):
        self.hasher = hashlib.new('sha256')

    def hash_data(self, data: str):
        bytes_data = data.encode()
        self.hasher.update(bytes_data)
        logger.info('Data hashed')
        return self.hasher.hexdigest()
