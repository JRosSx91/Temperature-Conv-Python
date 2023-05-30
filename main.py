def converter_cel(x):
    return (x - 32.0) * 5.0 / 9.0


def converter_fahr(x):
    return x * 9.0 / 5.0 + 32.0


def converter_kelvin_to_cel(x):
    return x - 273.15


def converter_cel_to_kelvin(x):
    return x + 273.15


def converter_fahr_to_rankine(x):
    return x + 459.67


def converter_rankine_to_fahr(x):
    return x - 459.67


def print_temp_message(temp, scale):
    message = {
        "Celsius": "That's really cold!❄️" if temp < 0.0 else "That's really hot!🔥" if temp >= 30.0 else "That's a moderate temperature.",
        "Fahrenheit": "That's really cold!❄️" if temp < 32.0 else "That's really hot!🔥" if temp >= 86.0 else "That's a moderate temperature.",
        "Kelvin": "That's really cold!❄️" if temp < 273.15 else "That's really hot!🔥" if temp >= 303.15 else "That's a moderate temperature.",
        "Rankine": "That's really cold!❄️" if temp < 491.67 else "That's really hot!🔥" if temp >= 545.67 else "That's a moderate temperature.",
    }.get(scale, "Invalid scale.")
    print(
        f"The converted temperature is {temp:.2f} degrees {scale}. {message}")
