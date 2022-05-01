from src.parser_mod.parser import Parser


class Supervisor:
    def __init__(self, settings: dict[str, str]) -> None:
        self.settings = settings
        print(f'settings for supervisor: {settings}')
