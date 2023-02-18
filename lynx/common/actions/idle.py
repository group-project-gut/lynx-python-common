from lynx.common.actions.action import Action
from lynx.common.serializable import Properties
from lynx.common.objects.object import Object


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