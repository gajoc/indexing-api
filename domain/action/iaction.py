from abc import ABC, abstractmethod
from typing import Union, Dict

from domain.action_handler.iaction_handler import IActionHandler
from utils.constants import UserAction


class IAction(ABC):

    @property
    @abstractmethod
    def action_handlers(self) -> Dict:
        """Inherit as class property"""
        pass

    @property
    @abstractmethod
    def next_actions(self) -> Dict:
        """Inherit as class property"""
        pass

    @abstractmethod
    def execute(self, action: UserAction):
        pass

    def next_action(self, action: UserAction) -> Union[UserAction, None]:
        return self.next_actions.get(action)

    def dispatch_action_handler(self, action: UserAction) -> Union[IActionHandler, None]:
        return self.action_handlers.get(action)
