from typing import Any

def read_file(path: str) -> str:
    """Read file from `path`."""
    with open(path) as f:
        return f.read()

def write_file(path: str, obj: Any) -> None:
    """Write `obj` to path."""
    with open(path, 'w') as f:
        f.write(obj)