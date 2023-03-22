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
temperatureTk = float(input('Ingrese el valor de la temperatura característica Tk: '))

# Recopilando el valor de la frecuencia
frequency = float(input('Ingrese el valor de la frecuencia expresado en Hz: '))

#Recopilando el valor de permeabilidad relativa del material conductor
relativePermeability = float(input('Ingrese el valor de la permeabilidad relativa del material conductor: '))

# Recopilando el valor de n
n = int(input('Ingrese el valor de n: '))

# Recopilando el valor de la distancia de la línea
distance = float(input('Ingrese la distancia de la línea en km: '))

#############################################################################################
#                                     Área de cálculos                                      #
#############################################################################################
# Calculando el valor de C
c = (2*math.pi*frequency*relativePermeability)/(resistorDC*10**4)

# Calculando el valor de Rac
resistorAC = resistorDC*(1+c**2/12 -c**4/180)

# Calculando la resistencia por fase
racfase = resistorAC/n

# Calculando la resistencia total por la longitud de la línea
rACTotal = racfase*distance

# Mostrando el resultado 
print(f"El valor de la resistencia en AC a {temperatureMax} grados por fase es {racfase} Ω/km y la resistencia total debido a la longitud de la línea de {distance} es {rACTotal} Ω")

