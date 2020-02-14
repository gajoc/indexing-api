from domain.action_handler.iaction_handler import IActionHandler
from utils.storage import Storage


class CopyLastUserInputHandler(IActionHandler):

    def handle(self, storage: Storage, **kwargs):
        entity = storage.get_previous_copied()
        entity.update(**kwargs)
        storage.add(entity)
        human_view = self.human_readable_schema.dump(entity)
        print(human_view)
