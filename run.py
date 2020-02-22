import json

from create import create_app
from utils.constants import GenealogyService, DEFAULT_ENCODING, DEFAULT_CONFIG_FILE

config = json.load(open(DEFAULT_CONFIG_FILE, encoding=DEFAULT_ENCODING))
app = create_app(service=GenealogyService.FAMILY_SEARCH, config=config)
app.run()
