"""
Module for registering commands within the package

Author: flare561
"""
registered_commands = {}
__all__ = ["registered_commands", "command"]


class Command:
    def __init__(self, function, *, nsfw=False, hidden=False):
        self.function = function
        self.nsfw = nsfw
        self.hidden = hidden

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

    def __repr__(self):
        return (f"{self.function} nsfw: {self.nsfw} "
                f"hidden: {self.hidden} help: {self.help}")

    @property
    def help(self):
        return self.function.__doc__


def command(name, *, nsfw=False, hidden=False):
    def wrapper(f):
        registered_commands[name] = Command(f, nsfw=nsfw, hidden=hidden)
        return f
    return wrapper
