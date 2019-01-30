from pygal_maps_world.i18n import COUNTRIES

def get_country_code(counrty_name):
    """According to the designated country, return two-letter country code"""
    for code, name in COUNTRIES.items():
        if name == counrty_name:
            return code
        #if not find designated country, return None
        return None

