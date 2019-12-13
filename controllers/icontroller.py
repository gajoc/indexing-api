from abc import ABC, abstractmethod

from utils.constants import UserAction


class IController(ABC):

    @abstractmethod
    def wait_for_user_action(self) -> UserAction:
        pass

    @abstractmethod
    def before_exit(self):
        pass

    @abstractmethod
    def execute(self, action: UserAction):
        pass
