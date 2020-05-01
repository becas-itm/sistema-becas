import re
import hashlib


class Sha1KeyHasher:
    def __init__(self):
        self.spaces_regex = re.compile(r'(\s+)')

    def hash(self, item_name: str):
        item_name = self.clean_item_name(item_name)
        item_name = bytes(item_name, 'utf8')
        hash = hashlib.sha1(item_name)
        return hash.hexdigest()

    def clean_item_name(self, name: str):
        name = name.strip()
        name = name.lower()
        return re.sub(self.spaces_regex, ' ', name)
