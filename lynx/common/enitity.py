from dataclasses import dataclass

from lynx.common.serializable import Serializable


# Right now it just represents common root
# for both `Object` and `Action`
class Entity(Serializable):
    @dataclass
    class Exported(Serializable):
        type: str = ""
        args: str = ""

    def export(self) -> Exported:
        return self.Exported(type=type(self).__name__, args=super().serialize())

    def serialize(self) -> str:
        return self.export().serialize()

    @classmethod
    def deserialize(cls, json_string: str):  # TODO: returning `Self` was not working
        from lynx.common.actions.move import Move
        from lynx.common.object import Object

        exported_entity = cls.Exported.deserialize(json_string)
        entity_type = locals()[exported_entity.type]
        entity = entity_type().populate(exported_entity.args)
        return entity
