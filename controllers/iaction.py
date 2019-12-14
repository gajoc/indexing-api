from abc import ABC, abstractmethod

from utils.constants import UserAction


class IAction(ABC):

    @abstractmethod
    def execute(self, action: UserAction):
        pass
