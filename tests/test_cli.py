# -*- coding: utf-8 -*-
import owl
import sys
from mock import patch
from nose import tools
from StringIO import StringIO
from contextlib import contextmanager


@contextmanager
def patch_stdout():
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    yield captured

    sys.stdout = old_stdout


def test_run_without_arguments():
    with patch_stdout() as new_stdout:
        owl.cli.run([])
        tools.assert_equal(new_stdout.getvalue(), owl.cli.help() + '\n')


def test_run_check():
    with patch_stdout() as new_stdout:
        owl.cli.run(['check'])
        pass
