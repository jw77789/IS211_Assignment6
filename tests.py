import unittest
from conversions import *

class TestTemperatureConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        print("Testing convertCelsiusToKelvin...")
        self.assertAlmostEqual(convertCelsiusToKelvin(0), 273.15)
        self.assertAlmostEqual(convertCelsiusToKelvin(100), 373.15)
        self.assertAlmostEqual(convertCelsiusToKelvin(-273.15), 0.0)
        self.assertAlmostEqual(convertCelsiusToKelvin(37), 310.15)
        self.assertAlmostEqual(convertCelsiusToKelvin(-50), 223.15)

    def test_convertCelsiusToFahrenheit(self):
        print("Testing convertCelsiusToFahrenheit...")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(0), 32)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(100), 212)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(-40), -40)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(37), 98.6)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(-50), -58)

if __name__ == "__main__":
    unittest.main()
