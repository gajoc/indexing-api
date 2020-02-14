from abc import ABC, abstractmethod
from typing import Union

from utils.constants import UserAction


class IAction(ABC):

    @abstractmethod
    def execute(self, action: UserAction):
        pass

    @abstractmethod
    def next_action(self, action: UserAction) -> Union[UserAction, None]:
        pass
