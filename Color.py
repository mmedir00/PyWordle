class Color:
    def green(texto):
        return "\033[92m{}\033[0m".format(texto)

    def yellow(texto):
        return "\033[93m{}\033[0m".format(texto)

    def grey(texto):
        return "\033[90m{}\033[0m".format(texto)

    def red(texto):
        return "\033[91m{}\033[0m".format(texto)