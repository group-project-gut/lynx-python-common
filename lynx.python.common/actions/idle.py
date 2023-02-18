from lynx.python.common.actions.action import Action
from lynx.python.common.serializable import Properties
from lynx.python.common.objects.object import Object


class Idle(Action):
    """
    Simple action for idling.
    """
    base: str
    properties: Properties
    object: Object

    def __init__(self, object: Object) -> None:
        super().__init__()
        self.properties.object_id = object.properties.id
        self.object = object

    def execute(self) -> None:
        self.log()
