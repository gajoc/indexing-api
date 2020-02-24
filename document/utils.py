from datetime import datetime
from typing import Union, Dict, List

from document import Language, Sex, DEFAULT_KEY_IN_DOCUMENTS


def create_person(names: List[str],
                  surnames: List[str],
                  sex: Union[Sex, None] = None,
                  condition: Union[str, None] = None,
                  father: Union[Dict, None] = None,
                  mother: Union[Dict, None] = None,
                  key: str = DEFAULT_KEY_IN_DOCUMENTS,
                  **kwargs) -> Dict:
    return {
        "name": [{key: name} for name in names],
        "surname": [{key: surname} for surname in surnames],
        "sex": {key: sex},
        "condition": {key: condition} if condition else condition,
        "father": father,
        "mother": mother,
        **kwargs,
    }


def create_document(origin_language: List[Language],
                    sources: List[Dict] = None,
                    key: str = DEFAULT_KEY_IN_DOCUMENTS,
                    **kwargs,
                    ) -> Dict:
    return {
        "origin_language": origin_language,
        "sources": sources if sources else [],
        "created_utc": datetime.utcnow(),
        **kwargs,
    }
