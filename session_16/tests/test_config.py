import unittest

from session_16.config.config_reader import Config


class TestConfigParsing(unittest.TestCase):

    def setUp(self):
        """ Configure the standard testing data
            This is because we remove the need for repeated code
        """
        self.tcr = Config()
        self.tcr.read_config_file('../config.toml')
        self.config = self.tcr.parse_config()
        self.parking_lot = self.config['location']

    def test_parse_config_has_correct_location_and_spaces(self):
        tcr = Config()  # tcr = TOML Config Reader
        tcr.read_config_file('../config.toml')
        config = tcr.parse_config()
        parking_lot = config['location']

        # Adrian prefers to use variables to make tests more readable
        expected_name = "Moondalup City Square Parking"
        expected_free = 190
        expected_max = 192

        self.assertEqual(expected_name, parking_lot['name'])
        self.assertEqual(expected_free, parking_lot['free_spaces'])
        self.assertEqual(expected_max, parking_lot['max_spaces'])

    def test_valid_location_code(self):
        location_code = 'CAR'
        # tcr is instantiated as part of the setUp method
        valid_code = self.tcr.valid_location_code(location_code)
        self.assertTrue(valid_code, f"{location_code} is not valid")

    def test_read_location_free_spaces(self):
        expected_free_spaces = 15
        location = 'CAR'
        actual_free_spaces = self.tcr.read_free_spaces(location)
        self.assertEqual(expected_free_spaces, actual_free_spaces)

    def test_read_location_max_spaces(self):
        expected_max_spaces = 16
        location = 'CAR'
        actual_max_spaces = self.tcr.read_max_spaces(location)
        self.assertEqual(expected_max_spaces, actual_max_spaces)

    def test_update_spaces_at_location(self):
        location = 'CAR'
        number_cars_entering = 2
        max_spaces = self.tcr.read_free_spaces(location)
        expected_spaces = max_spaces - number_cars_entering

        self.tcr.update_spaces(location, number_cars_entering)
        actual_spaces = self.tcr.read_free_spaces(location)
        self.assertEqual(expected_spaces, actual_spaces)

    def test_cars_entering(self):
        location = "CAR"
        number_entering = 1
        max_spaces = self.tcr.read_free_spaces(location)
        expected_spaces = max_spaces - number_entering
        self.tcr.cars_entering(location, number_entering)

        actual_spaces = self.tcr.read_free_spaces(location)
        self.assertEqual(expected_spaces, actual_spaces)

    def test_cars_exiting(self):
        location = "CAR"
        number_exiting = 1
        max_spaces = self.tcr.read_free_spaces(location)
        expected_spaces = max_spaces + number_exiting
        self.tcr.cars_exiting(location, number_exiting)

        actual_spaces = self.tcr.read_free_spaces(location)
        self.assertEqual(expected_spaces, actual_spaces)
