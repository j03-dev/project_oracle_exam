from typing import Type, Dict


def deserialize(data: Dict, class_type: Type):
    fields = class_type.__annotations__
    class_data = {key: data.get(key) for key in fields}
    instance = class_type(**class_data)
    return instance
