import os
import math

# Método que limpia la consola cada vez que se ejecuta el programa
os.system('cls')

# Recopilando los valores de la resistencia en dc
resistorDC = float(input('Ingrese el valor de la Resistencia en corriente continua (DC) en Ω/km: '))

# Recopilando el valor de la frecuencia
frequency = float(input('Ingrese el valor de la frecuencia expresado en Hz: '))

#Recopilando el valor de permeabilidad relativa del material conductor
relativePermeability = float(input('Ingrese el valor de la permeabilidad relativa del material conductor: '))

# Recopilando la cantidad de conductores de la línea
conductors = int(input('Ingrese la cantidad de subconductores por línea: '))

# Recopilando la distancia en km
distance = float(input('Ingrese la longitud de la línea en km: '))

#############################################################################################
#                                     Área de cálculos                                      #
#############################################################################################
# Calculando el valor de C
c = (2*math.pi*frequency*relativePermeability)/(resistorDC*10**4)

# Calculando el valor de Rac
resistorAC = resistorDC*(1+c**2/12 -c**4/180)

# Calculando la resistencia de la línea
resistor_total = resistorAC*distance

# Calculando la resistencia por fase
rFase = resistor_total/conductors

# Mostrando el resultado 
print(f"El valor de la resistencia en AC por fase es de {round(rFase,6)} Ω/km")