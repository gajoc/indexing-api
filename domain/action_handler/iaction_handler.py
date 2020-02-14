from abc import ABC, abstractmethod

from model.human_readable_entity import HumanReadableSchema


class IActionHandler(ABC):

    human_readable_schema = HumanReadableSchema()

    @abstractmethod
    def handle(self, **kwargs):
        pass
