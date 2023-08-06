from mountain import Mountain

class MountainManager:

    def __init__(self) -> None:
        pass

    def add_mountain(self, mountain: Mountain):
        raise NotImplementedError()

    def remove_mountain(self, mountain: Mountain):
        raise NotImplementedError()

    def edit_mountain(self, old: Mountain, new: Mountain):
        raise NotImplementedError()

    def mountains_with_difficulty(self, diff: int):
        raise NotImplementedError()

    def group_by_difficulty(self):
        raise NotImplementedError()
