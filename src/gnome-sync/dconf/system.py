import typing as t
import subprocess


def dump(path: t.Optional[str] = None):
    output = subprocess.run(['dconf', 'dump', path or '/'], capture_output=True)
    return output.stdout.decode()
