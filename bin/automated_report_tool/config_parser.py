import configparser


class LocalConfigParser:

    def __init__(self, config_file):
        self.__config = configparser.ConfigParser()
        self.__config.read(config_file)

    def get_config(self, prop):
        if self.__config.has_option("Path", prop):
            return self.__config.get("Path", prop)
        else:
            return ""

