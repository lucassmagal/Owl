# -*- coding: utf-8 -*-
import owl
from mock import patch
from nose import tools


@patch('getpass.getuser')
def test_destinations(mock_user):
    """This test checks if Owl can return the real path of all files in
    ~/.owl directory. The return of owl.path.destinations should
    be a generator of 2-tuples containing the path of the file inside Owl's
    folder, and the real path of that same file.
    """
    mock_user.return_value = 'bar'
    walk_output = ('/home/bar/.owl/home/__me__/.vim', [], ['.vimrc', '.gvimrc'])
    expected = [
        ('/home/bar/.owl/home/__me__/.vim/.vimrc', '/home/bar/.vim/.vimrc'),
        ('/home/bar/.owl/home/__me__/.vim/.gvimrc', '/home/bar/.vim/.gvimrc')
    ]

    tools.assert_equal(list(owl.path.destinations(walk_output)), expected)


@patch('os.symlink')
def test_path_symlink(mock_os_symlink):
    """path.symlink should return nothing (i.e. None) if the symlink was
    succesfully created. Some exception inherited from owl.exceptions.BaseError
    will be raise if there's something wrong.
    """
    mock_os_symlink.return_value = None
    _input = ('/home/bar/.owl/home/__me__/.vim/.vimrc', '/home/bar/.vim/.vimrc')

    owl.path.symlink(*_input)

    mock_os_symlink.assert_called_with(*_input)


@patch('os.symlink')
def test_symlinking_when_file_exists(mock_os_symlink):
    _input = ('/home/bar/.owl/home/__me__/.vim/.gvimrc', '/home/bar/.vim/.gvimrc')
    mock_os_symlink.side_effect = OSError(17, 'File exists')

    with tools.assert_raises(owl.exceptions.FileExists):
        owl.path.symlink(*_input)

    mock_os_symlink.assert_called_with(*_input)
