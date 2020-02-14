from abc import ABC, abstractmethod
from typing import Union

from domain.action_handler.iaction_handler import IActionHandler
from utils.constants import UserAction


class IAction(ABC):

    action_handlers = {}

    @abstractmethod
    def execute(self, action: UserAction):
        pass

    @abstractmethod
    def next_action(self, action: UserAction) -> Union[UserAction, None]:
        pass

    def dispatch_action_handler(self, action: UserAction) -> Union[IActionHandler, None]:
        return self.action_handlers.get(action)
