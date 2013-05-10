# -*- coding: utf-8 -*-
from owl import traverser
from mock import patch
from should_dsl import should


@patch('getpass.getuser')
def test_destinations(mock_user):
    """This test checks if Owl can return the real path of all files in
    ~/.owl directory. The return of owl.traverser.destinations should
    be a generator of 2-tuples containing the path of the file inside Owl's
    folder, and the real path of that same file.
    """
    mock_user.return_value = 'bar'

    walk_output = ('/home/bar/.owl/home/__me__/.vim', [], ['.vimrc', '.gvimrc'])
    expected = [
        ('/home/bar/.owl/home/__me__/.vim/.vimrc', '/home/bar/.vim/.vimrc'),
        ('/home/bar/.owl/home/__me__/.vim/.gvimrc', '/home/bar/.vim/.gvimrc')
    ]
    list(traverser.destinations(walk_output)) |should| equal_to(expected)
