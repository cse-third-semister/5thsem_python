"""
22-  Write a program that begins by reading a temperature from the user in degrees Celsius. Then your
 program should display the equivalent temperature in degrees Fahrenheit and degrees Kelvin. The
 calculations needed to convert between different units of temperature can be found on the Internet.
"""


celsius = float(input("Enter the temperature in degrees Celsius: "))


fahrenheit = (celsius * 9/5) + 32


kelvin = celsius + 273.15


print(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")
print(f"Temperature in Kelvin: {kelvin:.2f} K")



# Enter the temperature in degrees Celsius: 20
# Temperature in Fahrenheit: 68.00 °F
# Temperature in Kelvin: 293.15 K