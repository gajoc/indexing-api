from abc import abstractmethod, ABC

from domain.failure_monitor import ControllerFailureMonitor
from domain.scenario.fs_military_records import FamilySearchMilitaryRecordsVoiceCommand, \
    FamilySearchMilitaryRecordsKeyboardCommand
from utils.constants import UserAction


class IGeneiApp(ABC):
    @abstractmethod
    def run(self, **config):
        pass


class GeneiAppSelenium(IGeneiApp):

    def __init__(self, control_via):
        controller_types = {
            'voice': FamilySearchMilitaryRecordsVoiceCommand,
            'keyboard': FamilySearchMilitaryRecordsKeyboardCommand,

        }
        self.controller = controller_types.get(control_via)()

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
