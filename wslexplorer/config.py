import os
import ruamel.yaml as yaml
from getpass import getuser

default_user = getuser()

DEFAULTS = '''
    user: {user}
    explorer_path: /mnt/c/Windows/explorer.exe
    lxss_path: C:\\Users\\{user}\\AppData\\local\\lxss
    drives: [c, d]
'''.format(user=default_user)

class Config(yaml.comments.CommentedMap):
    def __init__(self, init):
        self.load(init)

    def dump(self):
        return yaml.dump(yaml.comments.CommentedMap(self),
                         Dumper=yaml.RoundTripDumper)

    def load(self, c):
        for key, value in yaml.load(c, Loader=yaml.RoundTripLoader).items():
            self[key] = value

    def save_file(self, filename):
        dirname = os.path.dirname(filename)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(filename, 'w') as f:
            f.write(self.dump())

    def load_file(self, filename):
        with open(filename) as f:
           self.load(f.read())
