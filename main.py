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


def main():
    print("Welcome to Fº/Cº/K/R converter!")
    print("Please enter the temperature you want to convert:")
    temp = float(input())

    print("What scale is this temperature in? Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin and 'R' for Rankine:")
    scale = input().strip().upper()

    if scale == "F":
        print("Converting to Celsius, Rankine and Kelvin:")
        celsius = converter_cel(temp)
        rankine = converter_fahr_to_rankine(temp)
        kelvin = converter_cel_to_kelvin(celsius)
        print_temp_message(celsius, "Celsius")
        print_temp_message(rankine, "Rankine")
        print_temp_message(kelvin, "Kelvin")
    elif scale == "C":
        print("Converting to Fahrenheit, Kelvin and Rankine:")
        fahr = converter_fahr(temp)
        rankine = converter_fahr_to_rankine(fahr)
        kelvin = converter_cel_to_kelvin(temp)
        print_temp_message(fahr, "Fahrenheit")
        print_temp_message(kelvin, "Kelvin")
        print_temp_message(rankine, "Rankine")
    elif scale == "R":
        print("Converting to Fahrenheit, Celsius and Kelvin:")
        fahr = converter_rankine_to_fahr(temp)
        celsius = converter_cel(fahr)
        kelvin = converter_cel_to_kelvin(celsius)
        print_temp_message(fahr, "Fahrenheit")
        print_temp_message(celsius, "Celsius")
        print_temp_message(kelvin, "Kelvin")
    elif scale == "K":
        print("Converting to Celsius, Fahrenheit and Rankine:")
        celsius = converter_kelvin_to_cel(temp)
        fahr = converter_fahr(celsius)
        rankine = converter_fahr_to_rankine(fahr)
        print_temp_message(celsius, "Celsius")
        print_temp_message(fahr, "Fahrenheit")
        print_temp_message(rankine, "Rankine")
    else:
        print("Invalid scale entered.")
        return

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
