import pathlib

def parse_config():
    config_path = pathlib.Path("config")

    if config_path.is_file() and config_path.exists():
        
        config_text = open("config").readlines()
        lines_which_are_not_comment = [line.strip() for line in config_text if (not line.startswith("#")) and line.strip()!=""]
        
        variables_values = {

            variable.strip():value.strip()
            for variable,value in [line.split("=") for line in lines_which_are_not_comment]
        }

        return variables_values

    else:
        raise FileNotFoundError("Config file could not be found.")

