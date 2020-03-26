import enum


@enum.unique
class EntityName(str, enum.Enum):
    ICETEX = 'icetex'

    DAAD = 'daad'


def get_entity_full_name(name):
    ENTITIES_FULL_NAME = {
        EntityName.ICETEX: 'ICETEX',
        EntityName.DAAD: 'Servicio Alemán de Intercambio Académico',
    }

    return ENTITIES_FULL_NAME.get(EntityName(name))
