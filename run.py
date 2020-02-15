import json

from create import create_app
from utils.constants import GenealogyService


config = json.load(open("config.json", encoding="utf-8"))
app = create_app(service=GenealogyService.FAMILY_SEARCH, config=config)
app.run()
