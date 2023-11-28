from src.model.countries.definitions import COUNTRY_CURRENCIES, COUNTRY_CAPITAL
from src.model.countries.country import COUNTRIES


def show(option: str) -> dict:
    if option == COUNTRY_CURRENCIES:
        return show_total_uses_coin()
    elif option == COUNTRY_CAPITAL:
        return show_countryes_capitals()   
    else:
        pass


def show_countryes_capitals() -> dict[str, str]:
    result: dict[str, str] = { "name_country" : "name_capital" }
    for country in COUNTRIES:
        if "capital" in country:
            country_name: str = country["name"]["common"]
            country_capital: str = country["capital"][0]
            result[country_name] = country_capital
            print(f"-{country_name}:{country_capital}")
    return result


def show_total_uses_coin() -> dict[str, str]:
    result: dict[str, int] = { "name_coin" : "total_countries_use_it" }
    for country in COUNTRIES:
#        if "currencias" in country:
        country_coin: str = country["currencies"].keys()      
        coin_count: int = 0


        for key in country_coin:
            country_coin = key
            print(country_coin)
            if country_coin == country["currencies"].keys():
                coin_count += 1
            else:
                result[country_coin] = 1

            result[country_coin] = coin_count
            print(result)
        return result
        

        
#             result[country_coin] = +1
#             print(result[country_coin])
#        else:
#            result[country_coin] = 0
#           print("Else")
