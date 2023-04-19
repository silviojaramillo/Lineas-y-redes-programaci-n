import os

os.system('cls')

# Recopilando los valores de la resistencia
resistor1 = float(input('Ingrese el valor de la resistencia a referir en Ω/km: '))

# Recopilando la temperatura de la resistencia a referir
temperature1 = float(input('Ingrese el valor de la temperatura en grados para la que resistencia a referir es igual a: {} Ohms: '.format(resistor1)))

# Recopilando el valor de la temperatura a la que se desea referir la resistencia
temperature2 = float(input('Ingrese el valor de la temperatura de operación: '))

# Recopilando la temperatura característica del material conductor
temperature_k = float(input('Ingrese el valor de la temperatura característica del conductor: '))

temperature_end = resistor1*((temperature_k + temperature2)/(temperature_k + temperature1))

# Mostrando el valor de la temperatura final
print(f"El valor de la resistencia a referir ({resistor1}) referida a {temperature2} grados es {round(temperature_end,6)} Ω/km")