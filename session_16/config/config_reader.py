import os.path

import tomli


class Config:

    def __init__(self):
        self.config = None

    def read_config_file(self, filename=None):
        if not os.path.exists(filename):
            raise FileNotFoundError

        with open(filename, mode="rb") as config_file_handle:
            self.config = tomli.load(config_file_handle)

    def valid_location_code(self, code:str)->bool:
        return code in self.config["locations"]["codes"]
    def read_free_spaces(self, parking_code: str) -> int:
        return self.config["locations"][parking_code]['free_spaces']

    def read_max_spaces(self, parking_code: str) -> int:
        return self.config["locations"][parking_code]['free_spaces']

    def parse_config(self) -> dict:
        return self.config

    def update_spaces(self, parking_code, quantity):
        self.config["locations"][parking_code]['free_spaces'] += quantity

    def __str__(self):
        return str(self.config)
