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
