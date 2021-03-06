# -*- coding: utf-8 -*-
import owl
from mock import patch
from nose import tools
import errno


@patch('getpass.getuser')
def test_destinations(mock_user):
    """This test checks if Owl can return the real path of all files in
    ~/Owl directory. The return of owl.path.destinations should
    be a generator of 2-tuples containing the path of the file inside Owl's
    folder, and the real path of that same file.
    """
    mock_user.return_value = 'bar'
    walk_output = ('/home/bar/Owl/home/__me__/.vim', [], ['.vimrc', '.gvimrc'])
    expected = [
        ('/home/bar/Owl/home/__me__/.vim/.vimrc', '/home/bar/.vim/.vimrc'),
        ('/home/bar/Owl/home/__me__/.vim/.gvimrc', '/home/bar/.vim/.gvimrc')
    ]

    tools.assert_equal(list(owl.path.destinations(walk_output)), expected)


@patch('os.symlink')
def test_path_symlink(mock_os_symlink):
    """path.symlink should return nothing (i.e. None) if the symlink was
    succesfully created. Some exception inherited from owl.exceptions.BaseError
    will be raise if there's something wrong.
    """
    mock_os_symlink.return_value = None
    _input = ('/home/bar/Owl/home/__me__/.vim/.vimrc', '/home/bar/.vim/.vimrc')

    owl.path.symlink(*_input)

    mock_os_symlink.assert_called_with(*_input)


@patch('os.symlink')
def test_symlinking_when_file_exists(mock_os_symlink):
    _input = ('/home/bar/Owl/home/__me__/.vim/.gvimrc', '/home/bar/.vim/.gvimrc')
    mock_os_symlink.side_effect = OSError(errno.EEXIST, 'File exists')

    tools.assert_raises(owl.exceptions.FileExists, owl.path.symlink, *_input)

    mock_os_symlink.assert_called_with(*_input)


@patch('os.symlink')
def test_symlinking_when_theres_no_directory(mock_os_symlink):
    """The goal here is check if path.symlink raises the right error when
    the destination path does not exist.
    """
    _input = ('/home/bar/Owl/etc/httpd/httpd.conf', '/etc/httpd/httpd.conf')
    mock_os_symlink.side_effect = OSError(errno.ENOENT, 'No such file or directory')

    tools.assert_raises(owl.exceptions.NoSuchFileOrDirectory, owl.path.symlink, *_input)

    mock_os_symlink.assert_called_with(*_input)

