def convert_temperature(temperature, unit):
  """Converts a temperature to the other two units.

  Args:
    temperature: The temperature value to convert.
    unit: The original unit of measurement ('C', 'F', or 'K').

  Returns:
    A tuple containing the converted temperatures in Celsius, Fahrenheit, and Kelvin.
  """

  if unit == 'C':
    celsius = temperature
    fahrenheit = (9/5) * celsius + 32
    kelvin = celsius + 273.15
  elif unit == 'F':
    fahrenheit = temperature
    celsius = (5/9) * (fahrenheit - 32)
    kelvin = (5/9) * (fahrenheit - 32) + 273.15
  elif unit == 'K':
    kelvin = temperature
    celsius = kelvin - 273.15
    fahrenheit = (9/5) * (kelvin - 273.15) + 32
  else:
    raise ValueError("Invalid unit of measurement. Please use 'C', 'F', or 'K'.")

  return celsius, fahrenheit, kelvin

def main():
  while True:
    try:
      temperature = float(input("Enter the temperature: "))
      unit = input("Enter the unit of measurement (C, F, or K): ").upper()

      celsius, fahrenheit, kelvin = convert_temperature(temperature, unit)

      print(f"Celsius: {celsius:.2f}")
      print(f"Fahrenheit: {fahrenheit:.2f}")
      print(f"Kelvin: {kelvin:.2f}")

      break
    except ValueError:
      print("Invalid input. Please enter a valid number and unit.")

if __name__ == "__main__":
  main()