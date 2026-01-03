# variables

location = "Oslo"
temperature = -11
wind_velocity = 19
wind_direction = "South-West"

print(f"Today, the temperature in {location} is {temperature} degrees Celcius.")

# temperature logic
if temperature >= 40:
    print("It's very hot today.")
    print("Don't forget to drink water!")
elif temperature > 30: 
    print("It's a hot day.")
    print("Enjoy the. sun!")
elif temperature >= 20:
    print("The weather is relatively nice.")
    print("Time for a picnic!")
elif temperature > 10:
    print("It's a little cold.")
    print("Watch out for the breeze!")
elif temperature < 10 and temperature > 0:
    print("It's a cold day.")
    print("Bring a jacket!")
elif temperature < 0:
    print("It's a very cold day.")
    print("Might be best to stay at home...")

print("-")

print(f"Wind speed is at {wind_velocity} km/h, towards the {wind_direction} direction.")

# wind logic
if wind_velocity > 30:
    print("Extreme winds are expected today.")
elif wind_velocity > 20:
    print("It's a windy day.")
elif wind_velocity < 20 and wind_velocity > 10:
    print("It's a little windy.")
elif wind_velocity < 10:
    print("No significant winds today.")

print("-")

# result
print("Code executed successfully.")