from abc import ABC, abstractmethod

from model.ientity import HumanReadableSchema


class IActionHandler(ABC):

    human_readable_schema = HumanReadableSchema()

    @abstractmethod
    def handle(self, **kwargs):
        pass
