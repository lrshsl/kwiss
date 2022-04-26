from __future__ import annotations

import os
import posixpath
import ntpath
from typing import Optional, Sequence, NamedTuple
from enum import IntEnum, auto


class QuestionPair(NamedTuple):
    question: str
    answer: str


class Os(IntEnum):
    LINUX = auto()
    WINDOWS = auto()
    MAC_OSX = auto()


class Path:
    def __init__(
            self,
            path: 'Path' | str | Sequence[str]
    ) -> None:
        """ A class to easily and uniformed handle paths """
        if isinstance(path, Path):
            self.path = path.path
        elif isinstance(path, Sequence):
            self.path = path
        else:
            self.path_as_string = Path.extract_path(path)

    @staticmethod
    def extract_path(
            path: str,
            separator: Optional[str]
    ) -> list[str]:
        """ Return argument 'path' split up on specified 'separator' """
        if separator:
            return path.split(separator)
        if '\\' in path:
            return path.split('\\')
        if '/' in path:
            return path.split('/')
        return path

    @staticmethod
    def get_path(path, _os: Optional[Os]) -> str:
        """ Join 'path' with separator matching to '_os' """
        if _os in (Os.LINUX, Os.MAC_OSX):
            return posixpath.join(path)
        elif _os is Os.WINDOWS:
            return ntpath.join(path)
        return os.path.join(path)

    def __repr__(self) -> str:
        return f'Path({self.get_path()})'
