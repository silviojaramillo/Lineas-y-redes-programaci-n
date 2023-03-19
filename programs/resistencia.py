import os
import math
os.system('cls')

# Recopilando los valores de la resistencia en dc
resistorDC = float(input('Ingrese el valor de la Resistencia en corriente continua (DC): '))

# Recopilando la temperatura de referencia
temperatureRef = float(input('Ingrese la temperatura de referencia: '))

# Recopilando el valor de la temperatura máxima
temperatureMax = float(input('Ingrese el valor de la temperatura máxima: '))

# Recopilando el valor de Tk
temperatureTk = float(input('Ingrese el valor de Tk: '))

# Recopilando el valor de la frecuencia
frequency = float(input('Ingrese el valor de la frecuencia expresado en Hz: '))

#Recopilando el valor de permeabilidad relativa del material conductor
relativePermeability = float(input('Ingrese el valor de la permeabilidad relativa del material conductor: '))

# Recopilando el valor de n
n = int(input('Ingrese el valor de n: '))

#############################################################################################
#                                     Área de cálculos                                      #
#############################################################################################
# Calculando el valor de C
c = (2*math.pi*frequency*relativePermeability)/(resistorDC*10**4)

# Calculando el valor de Rac
resistorAC = resistorDC*(1+c**2/12 -c**4/180)

racfase = resistorAC/n

# Mostrando el resultado
print(f"El valor de la resistencia en AC es {racfase}")

