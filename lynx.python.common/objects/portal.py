from lynx.python.common.actions.log import Log
from lynx.python.common.exec_interrupt import MapExit
from lynx.python.common.point import Point
from lynx.python.common.objects.object import Object
from lynx.python.common.serializable import Properties


class Portal(Object):
    """
    `Object` allowing the player to move to a next `scene`.
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool

    def __init__(self, scene: 'Scene', position: Point = Point(0, 0)) -> None:
        super().__init__(position, scene)
        self.walkable = True

    def on_collision(self, other) -> None:
        Log(type="info", message="Loading next map...").execute()
        self.scene.runtime.next_scene.execute()
        # Stop execution flow of `exec`
        raise MapExit
