from __future__ import annotations
from typing import List

from mountain import Mountain

class MountainOrganiser:

    def __init__(self) -> None:
        raise NotImplementedError()

    def cur_position(self, mountain: Mountain) -> int:
        raise NotImplementedError()

    def add_mountains(self, mountains: List[Mountain]) -> None:
        raise NotImplementedError()
