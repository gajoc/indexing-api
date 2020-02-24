from typing import Union, Dict

from document import Legitimation, DEFAULT_KEY_IN_DOCUMENTS


def create_birth_circumstances(location: Union[str, None] = None,
                               house_number: Union[str, None] = None,
                               legitimate: Union[Legitimation, None] = None,
                               religion: str = None,
                               godfather: Union[Dict, None] = None,
                               godmother: Union[Dict, None] = None,
                               key: str = DEFAULT_KEY_IN_DOCUMENTS,
                               **kwargs) -> Dict:
    return {
        "location": {key: location} if location else location,
        "house_number": {key: house_number} if house_number else house_number,
        "legitimate": {key: legitimate} if legitimate else legitimate,
        "religion": {key: religion} if religion else religion,
        "godfather": godfather,
        "godmother": godmother,
        **kwargs,
    }
