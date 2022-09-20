from . import parser
import json, sys


def main():
    conf = parser.parse_conf(sys.argv[1])
    dump(conf)


def dump(obj):
    json.dump(obj, sys.stdout, indent=2, default=str)


if __name__ == '__main__':
    main()
