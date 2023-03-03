from dataclasses import dataclass
from typing import List, Dict
from lynx.common.object import *
# TODO: we should make the imports less specific
#       now, we must add each class here \/
from lynx.common.actions.move import Move
from lynx.common.serializable import Serializable
from lynx.common.vector import Vector
from lynx.common.enitity import Entity


@dataclass
class Scene(Serializable):
    # We are using separate class for serialization
    @dataclass
    class Exported(Serializable):
        entities: List[Entity.Exported] = field(default_factory=list)

    _entities: List[Entity] = field(default_factory=list)
    objects_map: Dict[Vector, Object] = field(default_factory=dict)

    def export(self) -> Exported:
        exported_entities = [entity.export() for entity in self._entities]
        return self.Exported(exported_entities)

    def serialize(self) -> str:
        return self.export().serialize()

    def populate(self, json_string) -> None:
        exported_scene = self.Exported.deserialize(json_string)
        for exported_entity in exported_scene.entities:
            entity_type = globals()[exported_entity.type]
            entity = entity_type.deserialize(exported_entity.args)
            self.add_entity(entity)

    def add_entity(self, entity: Entity):
        self._entities.append(entity)
        if type(entity) is Object:
            self.objects_map[entity.position] = entity
