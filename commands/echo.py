from .command import command


@command(name="echo", nsfw=False, hidden=True)
def echo(target, text, server):
    """Usage ~echo <text> Repeats what you said"""
    print(target, text)


@command(nsfw=True)
def sneko(target, text, server):
    """Usage ~sneko Prints hiss"""
    print(target, "hiss")