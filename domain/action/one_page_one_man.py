from typing import Union

from domain.action.iaction import IAction
from domain.action_handler.browser import BrowserHandler
from domain.action_handler.copy_input import CopyLastUserInputHandler
from domain.action_handler.empty_input import EmptyEntityHandler
from domain.action_handler.pop_input import PopPreviousEntity
from domain.action_handler.user_input import CollectUserInputHandler
from utils.constants import UserAction, BrowserAction
from utils.misc import entity_base_data


class OnePageOneManAction(IAction):

    action_handlers = {
        UserAction.DATA_INPUT: CollectUserInputHandler,
        UserAction.NEXT_SCAN: BrowserHandler,
        UserAction.COPY: CopyLastUserInputHandler,
        UserAction.UNREADABLE: EmptyEntityHandler,
        UserAction.PREV_SCAN: PopPreviousEntity
    }

    def __init__(self):
        super().__init__()

    def execute(self, action: UserAction) -> Union[UserAction, None]:
        base_data = entity_base_data(**{
            'scan_link': self._browser.current_url(),
            'info': action,
        })
        args = ()
        kwargs = {}
        if action == UserAction.DATA_INPUT:
            args = (self._input_fields, self._autocomplete, self._storage,)
            kwargs = base_data
        elif action == UserAction.NEXT_SCAN:
            args = (self._browser, BrowserAction.NEXT,)
        elif action == UserAction.COPY:
            args = (self._storage,)
            kwargs = base_data
        elif action == UserAction.UNREADABLE:
            args = (self._storage,)
            kwargs = base_data
        elif action == UserAction.PREV_SCAN:
            args = (self._storage, self._browser, BrowserAction.PREVIOUS)
        else:
            print(f'Nieznana akcja, proszę wybrać jedną z dostępnych akcji.')

        handler = self.dispatch_action_handler(action)
        if handler:
            handler().handle(*args, **kwargs)
        return self.next_action(action)

    def next_action(self, action: UserAction) -> Union[UserAction, None]:
        mapper = {
            UserAction.DATA_INPUT: UserAction.NEXT_SCAN,
            UserAction.NEXT_SCAN: None,
            UserAction.COPY: UserAction.NEXT_SCAN,
            UserAction.UNREADABLE: UserAction.NEXT_SCAN,
            UserAction.PREV_SCAN: None
        }
        return mapper.get(action)
