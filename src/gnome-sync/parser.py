#!/usr/bin/env python

from pathlib import Path

SCRIPT_PATH = Path(__file__)
KEYS_PATH = SCRIPT_PATH.parent / 'keys.txt'

class Directory:
    def __init__(self, name: str):
        self.name = name
        self.keys = {}

    def add(self, key: str, value = None):
        self.keys[key] = value

    def __repr__(self):
        cls = self.__class__.__name__
        s = f'<{cls} "{self.name}">'
        if self.keys:
            s += ' ' + str(self.keys)
        return s


def parse_conf(path):
    confs = []
    directory = None

    with Path(path).open() as f:
        while line := f.readline():
            line = line.strip()
            if not line:
                continue
            if line[0] in ['#', ';']:
                continue
            if line[0] == '[':
                if directory:
                    confs.append(directory)
                path = line[1:line.find(']')]
                directory = Directory(path)
                confs.append(directory)
                continue
            elif not directory:
                raise Exception('Encountered a key before a directory')
            key, value = map(str.strip, line.split('='))
            directory.add(key, value)
    return confs
