from abc import abstractmethod, ABC

from domain.failure_monitor import ControllerFailureMonitor
from utils.constants import UserAction


class IGeneiApp(ABC):
    @abstractmethod
    def run(self, **config):
        pass


class GeneiAppSelenium(IGeneiApp):

    def __init__(self, controller):
        self.controller = controller

    def run(self) -> None:
        with ControllerFailureMonitor(self.controller):
            action = None
            while True:
                if not action:
                    action = self.controller.wait_for_user_action()
                if action == UserAction.EXIT:
                    self.controller.before_exit()
                    break
                action = self.controller.execute(action)
