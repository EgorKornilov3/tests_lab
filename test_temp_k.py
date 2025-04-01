import allure
import pytest
from temperature_converter import *

@allure.epic("Temperature Converter")
@allure.feature("Basic Conversions")
class TestTemperatureConverter:

    @allure.story("Celsius to Fahrenheit")
    @allure.title("Convert 0°C to 32°F")
    def test_celsius_to_fahrenheit_basic(self):
        with allure.step("Calculate conversion"):
            result = celsius_to_fahrenheit(0)
        with allure.step("Verify result"):
            assert result == 32

    @allure.story("Celsius to Fahrenheit")
    @allure.title("Convert 100°C to 212°F")
    def test_celsius_to_fahrenheit_boiling(self):
        assert celsius_to_fahrenheit(100) == 212

    @allure.story("Edge Cases")
    @allure.title("Absolute zero: -273.15°C to 0K")
    def test_absolute_zero(self):
        with allure.step("Check Kelvin conversion"):
            assert celsius_to_kelvin(-273.15) == pytest.approx(0)
        with allure.step("Check Fahrenheit conversion"):
            assert celsius_to_fahrenheit(-273.15) == pytest.approx(-459.67)

@allure.epic("Temperature Converter")
@allure.feature("Advanced Conversions")
class TestAdvancedScenarios:

    @allure.story("Fahrenheit to Kelvin")
    @pytest.mark.parametrize("fahrenheit, kelvin", [
        (32, 273.15),
        (-459.67, 0)
    ])
    def test_fahrenheit_to_kelvin(self, fahrenheit, kelvin):
        with allure.step(f"Convert {fahrenheit}°F to Kelvin"):
            result = fahrenheit_to_kelvin(fahrenheit)
        with allure.step(f"Verify result ≈ {kelvin}K"):
            assert result == pytest.approx(kelvin, rel=1e-3)

    @allure.story("Error Handling")
    @allure.title("Invalid scale raises ValueError")
    def test_invalid_scale(self):
        with allure.step("Attempt invalid conversion X→Y"):
            with pytest.raises(ValueError):
                convert_temperature(0, "X", "Y")
