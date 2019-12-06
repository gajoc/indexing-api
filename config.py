config = {
    'selenium': {
        'chrome': {
            'driverPath': 'bin/chromedriver',
            'experimentalOptions': {
                'debuggerAddress': '127.0.0.1:9222',
            }
        }
    },
    'common': {
        'storage_dir': 'data',
    }
}

user_config = {
    'fields': ('surname', 'name', 'birth_date', 'birth_place', 'scan_link', 'save'),
    'click_button': "span[class='next pager-icon fs-civ-circle-chevron-right enabled']",
}
