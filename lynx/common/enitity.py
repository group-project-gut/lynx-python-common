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
        return self.Exported(type=type(self).__name__, args=self.serialize())
