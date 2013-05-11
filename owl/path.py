# -*- coding: utf-8 -*-
import os
import getpass
import exceptions
import errno


def destinations(path):
    """It returns a generator of 2-tuples containing
    the path of the file inside ~/.owl and the path
    of the destination.

    If there's no files, it'll raise an error.
    """
    dirpath, dirnames, filenames = path

    if not filenames:
        return

    destination_path = dirpath.split('.owl')[1]
    if destination_path.startswith('/home/__me__/'):
        destination_path = destination_path.replace('__me__', getpass.getuser())

    for filename in filenames:
        yield (os.path.join(dirpath, filename),
               os.path.join(destination_path, filename))


def symlink(src, dst):
    try:
        os.symlink(src, dst)
    except OSError as e:
        if e.errno == errno.EEXIST:
            raise exceptions.FileExists(dst)
        else:
            raise exceptions.NoSuchFileOrDirectory(dst)
