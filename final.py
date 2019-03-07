#!/usr/bin/python -u

# TJCTF 2018 Abyss

from __future__ import print_function
from code import InteractiveConsole
import code
import sys

text_banned = ["__class__", "__base__", "__subclasses__", "_module", "open", "eval", "execfile", "exec", "compile", "repr", "__"]
banned = ["vars", "getattr", "setattr", "delattr", "input", "raw_input", "help", "open", "memoryview", "eval", "exec", "execfile", "super", "file", "reload", "staticmethod", "property", "intern", "coerce", "buffer", "apply"]
text_banned.extend(banned)

global open
open = open
b = __builtins__
for each in b.__dict__.keys():
    if ("__" in each or each in banned) and each != "__name__":
        locals()[each] = b.__dict__[each]  # we save a copy for ourselves
        del b.__dict__[each]

class PseudoFile(object):

    def __init__(self, sh):
        self.sh = sh

    def write(self, s):
        self.sh.write(s)

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    def flush(self):
        pass

    def isatty(self):
        return True


class Shell(code.InteractiveConsole):
    "Wrapper around Python that can filter input/output to the shell"

    def __init__(self):
        code.InteractiveConsole.__init__(self)
        self.thread = None

    def push(self, line):
        for any in text_banned:
            if any in line:
                print("Sorry, '%s' is not allowed." % any)
                sys.stdout.flush()
                return
        return code.InteractiveConsole.push(self, line)

    def raw_input(self, prompt=""):
        print(">>>", end=" ")
        sys.stdout.flush()
        a = ""
        try:
            a = sys.stdin.readline().strip()
        except EOFError:
            pass
        return a

    def runcode(self, _code):
        global open
        org_stdout = sys.stdout
        sys.stdout = PseudoFile(self)
        try:
            exec _code in self.locals
        except SystemExit:
            raise
        except:
            print("The Abyss consumed your error.")
        else:
            if code.softspace(sys.stdout, 0):
                print

        sys.stdout = org_stdout

    def interact(self, banner=None):
        try:
            sys.ps1
        except AttributeError:
            sys.ps1 = ">>> "
        try:
            sys.ps2
        except AttributeError:
            sys.ps2 = "... "
        cprt = 'Type "help", "copyright", "credits" or "license" for more information.'
        if banner is None:
            self.write("Python %s on %s\n%s\n(%s)\n" %
                       (sys.version, sys.platform, cprt,
                        self.__class__.__name__))
        else:
            self.write("%s\n" % str(banner))
        more = 0
        while 1:
            try:
                if more:
                    prompt = sys.ps2
                else:
                    prompt = sys.ps1
                try:
                    line = self.raw_input(prompt)
                    # Can be None if sys.stdin was redefined
                    encoding = getattr(sys.stdin, "encoding", None)
                    if encoding and not isinstance(line, unicode):
                        line = line.decode(encoding)
                except EOFError:
                    self.write("\n")
                    break
                else:
                    more = self.push(line)
            except KeyboardInterrupt:
                self.write("\nKeyboardInterrupt\n")
                self.resetbuffer()
                more = 0

def main():
    banner = "The Abyss stares back."

    shell = Shell()
    shell.locals['__builtins__'] = b
    shell.interact(banner=banner)

if __name__=="__main__":
    main()