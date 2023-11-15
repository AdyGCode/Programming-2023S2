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
        tcr = Config()
        tcr.read_config_file('../config.toml')
        config = self.tcr.parse_config()
        parking_lot = self.config['location']
        self.assertEqual(parking_lot['name'], "Moondalup City Square Parking", "Name is not correct")
        self.assertEqual(parking_lot['free_spaces'], 190)
        self.assertEqual(parking_lot['max_spaces'], 192)

    def test_valid_location_code(self):
        location_code = 'CAR'
        # tcr is instantiated as part of the setUp method
        valid_code = self.tcr.valid_location_code(location_code)
        self.assertTrue(valid_code)

    def test_read_location_free_spaces(self):
        expected_spaces = 15
        location = 'CAR'
        actual_spaces = self.tcr.read_free_spaces(location)
        self.assertEqual(expected_spaces, actual_spaces)

    def test_read_location_max_spaces(self):
        expected_spaces = 16
        location = 'CAR'
        actual_spaces = self.tcr.read_max_spaces(location)
        self.assertEqual(expected_spaces, actual_spaces)

    def test_update_spaces_at_location(self):
        location = 'CAR'
        number_cars_entering = 2
        expected_spaces = 16 - number_cars_entering
        self.tcr.update_spaces(location, number_cars_entering)
        actual_spaces = self.tcr.read_free_spaces(location)
        self.assertEqual(expected_spaces, actual_spaces)
