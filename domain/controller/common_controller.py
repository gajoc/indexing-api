from abc import abstractmethod

from domain.controller.icontroller import IController
from utils.constants import UserAction


class CommonController(IController):

    def __init__(self):
        pass

    @property
    @abstractmethod
    def user_prompt_info(self):
        pass

    @abstractmethod
    def wait_for_user_action(self) -> UserAction:
        pass

    def before_exit(self) -> None:
        self._storage.dump()
