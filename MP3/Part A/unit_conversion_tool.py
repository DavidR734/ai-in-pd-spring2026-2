def convert_units(value: float, from_unit: str, to_unit: str) -> dict:
    if from_unit == "mm" and to_unit == "inch":
        factor = 1 / 25.4
        value_out = value * factor
    elif from_unit == "inch" and to_unit == "mm":
        factor = 25.4
        value_out = value * factor
    elif from_unit == "psi" and to_unit == "MPa":
        factor = 0.00689476
        value_out = value * factor
    elif from_unit == "MPa" and to_unit == "psi":
        factor = 1 / 0.00689476
        value_out = value * factor
    elif from_unit == "in·lb" and to_unit == "N·m":
        factor = 0.112985
        value_out = value * factor
    elif from_unit == "N·m" and to_unit == "in·lb":
        factor = 1 / 0.112985
        value_out = value * factor
    elif from_unit == "lbf" and to_unit == "N":
        factor = 4.44822
        value_out = value * factor
    elif from_unit == "N" and to_unit == "lbf":
        factor = 1 / 4.44822
        value_out = value * factor
    elif from_unit == "°C" and to_unit == "°F":
        factor = None  # Not a simple multiplier
        value_out = value * 9/5 + 32
    elif from_unit == "°F" and to_unit == "°C":
        factor = None  # Not a simple multiplier
        value_out = (value - 32) * 5/9
    else:
        raise ValueError(f"Unsupported unit conversion: {from_unit} to {to_unit}")

    return {
        "value_in": value,
        "from_unit": from_unit,
        "to_unit": to_unit,
        "value_out": value_out,
        "factor": factor,
    }