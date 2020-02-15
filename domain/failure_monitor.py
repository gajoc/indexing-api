from contextlib import ContextDecorator

from utils.logger import GeneiLogger


class ControllerFailureMonitor(ContextDecorator):

    def __init__(self, controller):
        self.controller = controller

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        exc_name, _, _ = exc
        if exc_name:
            self.controller.before_exit()
            GeneiLogger.get_logger(__name__).exception(exc)
        return False
