import typing as t

from .parser import Directory


def filter(directories: list[Directory], filters: list[Directory]):
    """
    Filter the keys in `directories` so only the one that exists in `filters`
    remain
    """
    directories_by_name = {d.name: d for d in directories}
    result = []
    for filter_directory in filters:
        name = filter_directory.name
        if filter_directory.name.endswith("/"):
            directory = find_startswith(directories_by_name, name)
        else:
            directory = directories_by_name.get(name)
        if not directory:
            continue
        if filter_directory.keys:
            directory.keys = {
                rule: directory.keys[rule]
                for rule in filter_directory.keys
                if rule in directory.keys
            }
        result.append(directory)
    return result


def find_startswith(d: dict[str, t.Any], search: str):
    """
    Returns the value of a dictionary where the key starts with the string `search`
    """
    for name in d:
        if name.startswith(search):
            return d[name]
    return None
