#!/usr/bin/env python

import typing as t
from pathlib import Path

from .system import dump

SCRIPT_PATH = Path(__file__)
KEYS_PATH = SCRIPT_PATH.parent / "keys.txt"


class Directory:
    def __init__(self, name: str):
        self.name = name
        self.keys = {}

    def add(self, key: str, value=None):
        self.keys[key] = value

    def __repr__(self):
        cls = self.__class__.__name__
        s = f'<{cls} "{self.name}">'
        if self.keys:
            s += " " + str(self.keys)
        return s

    def __str__(self):
        """
        Converting a directory to a string yields a result similar to dconf
        """
        s = f"[{self.name}]"
        for key, value in self.keys.items():
            s += f"\n{key}={value}"
        return s


def parse_conf(lines: t.Iterable[str] = None, has_keys=True):
    """
    Reads a dconf dump as an iterable of lines and returns it as a list of
    `Directory` objects
    """
    confs = []
    directory = None

    if lines is None:
        lines = dump().splitlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue
        if line[0] in ["#", ";"]:
            continue

        if line[0] == "[":
            path = line[1 : line.find("]")].strip()
            directory = Directory(path)
            confs.append(directory)
            continue

        if not directory:
            raise Exception("Encountered a key before a directory")

        if has_keys:
            assign_pos = line.find("=")
            if assign_pos < 0:
                raise Exception(f'No assignment on line "{line}", pos = {assign_pos}')
            key = line[:assign_pos].strip()
            value = line[assign_pos + 1 :].strip()
        else:
            key = line
            value = None
        directory.add(key, value)

    return confs


def write(f, directories: list[Directory], add_modelines=True):
    """
    Writes a list of `Directory` objects to a file in a dconf dump-like format
    """
    f.write("\n\n".join(str(x) for x in directories))
    if add_modelines:
        f.write("\n\n# vim: ft=dosini")
