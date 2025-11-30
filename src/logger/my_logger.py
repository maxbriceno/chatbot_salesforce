#* This file contains the logger service that is used to log levelling deb ug prints.

from colorama import Fore, Style, init

init(autoreset=True)

class ColorEnum:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE

class MyLogger:
    _ident_string = "    "
    _instance = None

    def __init__(self):
        self.ident_level = 0

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MyLogger()
        return cls._instance
        
    def log(self, message: str, level: int = 0, color=ColorEnum.YELLOW) -> None:
        indent = MyLogger._ident_string * level
        print(f"{color}{indent}{message}{Style.RESET_ALL}")