"""
qmatch

Usage:
  qmatch match <question>
  qmatch -h | --help
  qmatch --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  qmatch m "I understand clearly what I need to do to be successful in my current role"

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/davislf2/qmatch-cli
"""

from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION

import qmatch.commands


def main():
    """Main CLI entrypoint."""
    options = docopt(__doc__, version=VERSION)
    find_command(options)


def find_command(options):
    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(qmatch.commands, k) and v:
            module = getattr(qmatch.commands, k)
            qmatch.commands = getmembers(module, isclass)
            command = [
                command[1] for command in qmatch.commands
                if command[0] != 'Base'
            ][0]
            command = command(options)
            command.run()
