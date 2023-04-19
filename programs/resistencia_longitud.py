import os

os.system('cls')

# Recopilando el valor de la resistencia en Ohms/km
resistor = float(input('Ingrese el valor de la resistencia en Ω/km: '))

# Recopilando la distancia en km
distance = float(input('Ingrese la longitud de la línea en km: '))

#############################################################################################
#                                     Área de cálculos                                      #
#############################################################################################

# Calculando la resistencia de la línea
resistor_total = resistor*distance

# Mostrando los resultados
print(f"El valor de la resistencia en la línea de {distance} km es de {resistor_total} Ω")
