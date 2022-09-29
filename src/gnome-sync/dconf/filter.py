from .parser import Directory


"""
Filter the keys in `d` so only the one that exists in `directories` remain
"""
def filter(d: dict, directories: list[Directory]):
    result = []
    for dir in directories:
        target = read_path(d, dir.name)
        if target is None:
            continue
        if dir.keys:
            for key in dir.keys:
                dir.keys[key] = target.get(key)
            result.append(dir)
        else:
            # for dir in Directory.list_from_dict(target, dir.name):
            #     result.append(dir)
            print('Does not work')
    return result


def read_path(d: dict, path):
    target = d
    for level in path.split('/'):
        target = target.get(level + '/')
        if not isinstance(target, dict):
            return None
    return target
