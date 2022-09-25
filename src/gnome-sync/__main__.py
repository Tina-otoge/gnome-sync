from pathlib import Path
from . import dconf, KEYS_PATH
import json, sys


def main():
    conf = dconf.parser.parse_conf()
    dir = dconf.parser.directories_to_dict(conf)
    keys_to_sync = get_keys_dirs()
    result = dconf.filter(dir, keys_to_sync)
    with Path('./result.conf').open('w') as f:
        dconf.parser.write(f, result)


def dump(obj):
    json.dump(obj, sys.stdout, indent=2, default=str)


def get_keys_dirs():
    with KEYS_PATH.open() as f:
        lines = f.readlines()
    dirs = dconf.parser.parse_conf(lines, has_keys=False)
    return dirs

if __name__ == '__main__':
    main()
