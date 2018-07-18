import json


class ConfigLoader:
    def __init__(self, path):
        self.path = path
        self.config = self.load_file(path)

    @classmethod
    def load_file(cls, path):
        with open(path, 'r') as f:
            return json.loads(f.read())
