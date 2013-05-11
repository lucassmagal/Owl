# -*- coding: utf-8 -*-


class BaseError(RuntimeError):
    def __init__(self, path):
        self.path = path


class FileExists(BaseError):
    pass


class NoSuchFileOrDirectory(BaseError):
    pass
