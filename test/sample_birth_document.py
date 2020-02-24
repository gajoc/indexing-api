import json
import pprint

from document import Sex, Legitimation, Language
from document.birth import create_birth_circumstances
from document.utils import create_person, create_document

paternal_grandfather = create_person(names=['josephi'], surnames=[], sex=Sex.MALE)
paternal_grandmother = create_person(names=['maria'], surnames=[], sex=Sex.FEMALE)
a_father = create_person(names=['stanislaus'], surnames=['konopnicki'], sex=Sex.MALE, condition='agr.',
                         father=paternal_grandfather, mother=paternal_grandmother)
maternal_grandfather = create_person(names=['teodori'], surnames=[], sex=Sex.MALE)
maternal_grandmother = create_person(names=['thecla'], surnames=['lisowska'], sex=Sex.FEMALE)
a_mother = create_person(names=['magdalena'], surnames=['hewko'], sex=Sex.FEMALE, father=maternal_grandfather,
                         mother=maternal_grandmother)
a_godfather = create_person(names=['nicolaus'], surnames=['konopnicki'], sex=Sex.MALE)
a_godmother = create_person(names=['anna'], surnames=['oborska'], sex=Sex.FEMALE)
person = create_person(names=['petrus'], surnames=[], sex=Sex.MALE, father=a_father, mother=a_mother)
circumstances = create_birth_circumstances(location='baworów', house_number='183', legitimate=Legitimation.LEGITIMATE,
                                           religion='rom', godfather=a_godfather, godmother=a_godmother)

birth_data = {}
birth_data.update(person)
birth_data.update(circumstances)

a_birth = create_document(origin_language=[Language.LATIN], **birth_data)

pprint.pprint(json.dumps(a_birth, default=str, indent=4))
