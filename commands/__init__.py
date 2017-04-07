import os
from .command import *

__all__ = ["registered_commands", "command"]

for name, ext in map(os.path.splitext, os.listdir(os.path.dirname(__file__))):
    if name != '__init__' and ext in [".py", ".pyc", ".pyo"]:
        __all__.append(name)
del name, ext, os

from . import *
