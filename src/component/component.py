from abc import ABCMeta

class Component:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self, component_parameter):
        return NotImplemented
