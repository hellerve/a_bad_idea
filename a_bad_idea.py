import os
import sys
import imp

LANGS = {}

def add_implementation(name, fun):
    LANGS[name] = fun

def _install_importer():
    """Installs the module finder."""
    sys.meta_path.insert(0, Finder())

class Finder:
    """Custom module finder for #lang files."""
    @classmethod
    def find_module(cls, fullname, path):
        for dirname in sys.path:
            basename = os.path.join(dirname, fullname)
            for extension in LANGS.keys():
                filename = "{}.{}".format(basename, extension)
                if os.path.exists(filename) and not os.path.isdir(filename):
                    lang = _get_lang(filename)
                    if lang and lang == extension:
                        return LangLoader(filename, lang)

class LangLoader:
    """Custom module loader for #lang files."""
    def __init__(self, filename, lang):
        self.filename = filename
        self.lang = lang

    def load_module(self, fullname):
        if fullname in sys.modules:
            mod = sys.modules[fullname]
        else:
            mod = imp.new_module(fullname)
            sys.modules[fullname] = mod
        mod.__file__ = self.filename
        mod.__loader__ = self
        LANGS[self.lang](_get_code(self.filename), mod)
        return mod

def _get_code(filename):
    with open(filename) as f:
        contents = f.read()
    return "\n".join(contents.split("\n")[1:])

def _get_lang(filename):
    with open(filename) as f:
        first_line = f.readline()
    if first_line.startswith("#lang "):
        words = first_line.split(" ")
        return " ".join(words[1:])[:-1]

_install_importer()
