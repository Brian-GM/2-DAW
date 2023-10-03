from src.model.countries.definitions import COUNTRY_CURRENCIES, COUNTRY_CAPITAL , COUNTRY_CHOICES
from src.model.countries.country import COUNTRIES

def show(option: str) -> dict:
    if option == COUNTRY_CHOICES:
        result: dict[str] = { "name_coin" : "total_countries_use_it" }
    elif option == COUNTRY_CURRENCIES:
        pass
    elif option == COUNTRY_CAPITAL:
        pass
    else:
        pass