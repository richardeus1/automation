import json
EMAIL= []
PROMO_CODES= []
TABS= []
BRANDS= []

def init():
    global EMAIL, PROMO_CODES, TABS, BRANDS
    # read file
    data = None
    with open('settings.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    EMAIL = obj['shoestore']['email']
    PROMO_CODES = obj['shoestore']['promo_codes']
    TABS = obj['shoestore']['tabs']
    BRANDS = obj['shoestore']['brands']
