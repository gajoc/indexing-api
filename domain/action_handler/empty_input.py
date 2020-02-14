from domain.action_handler.iaction_handler import IActionHandler
from utils.storage import Storage


class EmptyEntityHandler(IActionHandler):

    def handle(self, storage: Storage, **kwargs):
        entity = {}
        entity.update(**kwargs)
        storage.add(entity)
