from create import create_app
from utils.constants import GenealogyService

config = {
    "storage_dir": "data",
    "storage_entities_limit": 100,
    "browser": {
        "name": "chrome",
        "driverPath": "bin/chromedriver",
        "experimentalOptions": {
            "debuggerAddress": "127.0.0.1:9222",
        }
    }
}

app = create_app(service=GenealogyService.FAMILY_SEARCH, config=config)
app.run()
