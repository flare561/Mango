from .command import command


@command("echo")
def echo(target, text, server):
    """Usage ~echo <text> Repeats what you said"""
    print(target, text)