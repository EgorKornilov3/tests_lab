def celsius_to_fahrenheit(celsius: float) -> float:
    """Конвертация Цельсия → Фаренгейт"""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Конвертация Фаренгейт → Цельсий"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius: float) -> float:
    """Конвертация Цельсия → Кельвин"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin: float) -> float:
    """Конвертация Кельвин → Цельсий"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Конвертация Фаренгейт → Кельвин"""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Конвертация Кельвин → Фаренгейт"""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature(value: float, from_scale: str, to_scale: str) -> float:
    """
    Основная функция конвертации.
    Поддерживаемые шкалы: 'C' (Цельсий), 'F' (Фаренгейт), 'K' (Кельвин).
    """
    from_scale = from_scale.upper()
    to_scale = to_scale.upper()
    
    if from_scale == to_scale:
        return value
    
    converters = {
        ('C', 'F'): celsius_to_fahrenheit,
        ('F', 'C'): fahrenheit_to_celsius,
        ('C', 'K'): celsius_to_kelvin,
        ('K', 'C'): kelvin_to_celsius,
        ('F', 'K'): fahrenheit_to_kelvin,
        ('K', 'F'): kelvin_to_fahrenheit,
    }
    
    key = (from_scale, to_scale)
    if key in converters:
        return converters[key](value)
    else:
        raise ValueError(f"Неподдерживаемая конвертация: {from_scale} → {to_scale}")
