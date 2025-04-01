import pytest
from temp_k import *

# Параметризованные тесты для основных конвертаций
@pytest.mark.parametrize("celsius, fahrenheit", [
    (0, 32),
    (100, 212),
    (-40, -40),
])
def test_celsius_to_fahrenheit(celsius, fahrenheit):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(fahrenheit)

@pytest.mark.parametrize("fahrenheit, celsius", [
    (32, 0),
    (212, 100),
    (-40, -40),
])
def test_fahrenheit_to_celsius(fahrenheit, celsius):
    assert fahrenheit_to_celsius(fahrenheit) == pytest.approx(celsius)

# Тесты для Кельвина
def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == pytest.approx(273.15)
    assert celsius_to_kelvin(-273.15) == pytest.approx(0)

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == pytest.approx(0)
    assert kelvin_to_celsius(0) == pytest.approx(-273.15)

# Комбинированные конвертации
def test_fahrenheit_to_kelvin():
    assert fahrenheit_to_kelvin(32) == pytest.approx(273.15)

def test_kelvin_to_fahrenheit():
    assert kelvin_to_fahrenheit(273.15) == pytest.approx(32)

# Тесты для основной функции convert_temperature
@pytest.mark.parametrize("value, from_scale, to_scale, expected", [
    (0, 'C', 'F', 32),
    (100, 'C', 'K', 373.15),
    (32, 'F', 'C', 0),
    (273.15, 'K', 'F', 32),
    (10, 'C', 'C', 10),  # Нет конвертации
])
def test_convert_temperature(value, from_scale, to_scale, expected):
    assert convert_temperature(value, from_scale, to_scale) == pytest.approx(expected)

# Тест на ошибку при неправильной шкале
def test_invalid_scale():
    with pytest.raises(ValueError):
        convert_temperature(0, 'X', 'Y')
