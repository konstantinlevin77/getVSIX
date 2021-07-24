from parse_config import parse_config
from colorama import Fore

def get_value_from_config(variable_name):
    try:
        config_dict = parse_config()

    except FileNotFoundError:
        print(Fore.CYAN+"Config file could not be find, you can create it typing")
        print(Fore.LIGHTRED_EX+"\tgetvsix create-config")
        print(Fore.RESET)
        return None
    
    result = config_dict.get(variable_name)
    if result is None:
        print(Fore.CYAN + "Value of variable '{}' could not be found".format(variable_name))
        print(Fore.RESET)
        return None

    else:
        return result.strip()
