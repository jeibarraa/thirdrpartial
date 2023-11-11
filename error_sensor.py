def temperature_sensor_simulation(readings):
  outside = 0

  for _ in range(readings):
      raw_temperature = float(input("Enter a temperature reading in Celcius: "))

      if not (10<= raw_temperature <=40):
          outside += 1
          print(" Warning: Temperature outside expected range!", end=" ")

  percentage_error = (outside / readings) * 100
  print("Summary:" )
  print("Total readings:", readings, end=" ")
  print("REadings outside expected range (10 to 40 degrees Celsius):", outside, end= " ")
  print("Percenatge of readings outside range:",percentage_error, "%")

readings = int(input("Enter the number of temperature readings: "))
temperature_sensor_simulation(readings)
