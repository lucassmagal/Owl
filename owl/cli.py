# -*- coding: utf-8 -*-
import argparse
import textwrap


def help():
    return textwrap.dedent("""\
    Owl - The simple configfiles manager
    ====================================

    Arguments:
      init        Creates an empty ~/.owl to getting started
      sync        Walks into ~/.owl and create the symlinks
      check       Tries to find problems (like files without proper symlinks)
    """)


def run(args):
    if not args:
        print help()
        return 1

    command = args[0]
    if command == 'check':
        pass
    return 0
