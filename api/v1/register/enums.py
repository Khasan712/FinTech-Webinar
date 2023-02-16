from enum import Enum


class Course(Enum):
    backend = 'backend'
    frontend = 'frontend'
    mobile = 'mobile'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
