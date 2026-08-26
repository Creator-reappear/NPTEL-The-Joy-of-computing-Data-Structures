def calculate_temperature_range():
  user_input = input()

  readings = [int(x) for x in user_input.split()]

  if len(readings) <= 1:
    print(0)
  else:
    highest = max(readings)
    lowest = min(readings)
    temp_range = highest - lowest
    print(temp_range)


calculate_temperature_range()
