import os

os.system('cls')

# Recopilando el valor de la resistividad del material en Ωm
resistivity = float(input('Ingrese el valor de la resistividad en Ωm: '))

# Recopilando la distancia
distance = float(input('Ingrese el valor de la longitud de la línea en metros: '))

# Recopilando el área transversal del conductor en metros cuadrados
area_conductor = float(input('Ingrese el valor del área del conductor en metros cuadrados: '))

#############################################################################################
#                                     Área de cálculos                                      #
#############################################################################################

# Calculando el valor de la resistencia
resistor = (resistivity*distance)/area_conductor

# Mostrando el resultado
print(f"El valor de la resistencia para la línea de {distance} m con resistividad de {resistivity} es de {resistor} Ω")