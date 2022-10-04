import json
import sys
from pathlib import Path

from . import KEYS_PATH, dconf


def main():
    conf = dconf.parser.parse_conf()
    keys_to_sync = get_filter_rules()
    result = dconf.filter(conf, keys_to_sync)
    with Path("./result.conf").open("w") as f:
        dconf.parser.write(f, result)


def get_filter_rules():
    with KEYS_PATH.open() as f:
        lines = f.readlines()
    dirs = dconf.parser.parse_conf(lines, has_keys=False)
    return dirs


if __name__ == "__main__":
    main()
