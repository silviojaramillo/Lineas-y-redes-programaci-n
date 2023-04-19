import os
import math

# Método que limpia la consola cada vez que se ejecuta el programa
os.system('cls')

# Recopilando los valores de la resistencia en dc
resistorDC = float(input('Ingrese el valor de la Resistencia en corriente continua (DC): '))


# Recopilando el valor de la frecuencia
frequency = float(input('Ingrese el valor de la frecuencia expresado en Hz: '))

#Recopilando el valor de permeabilidad relativa del material conductor
relativePermeability = float(input('Ingrese el valor de la permeabilidad relativa del material conductor: '))


#############################################################################################
#                                     Área de cálculos                                      #
#############################################################################################
# Calculando el valor de C
c = (2*math.pi*frequency*relativePermeability)/(resistorDC*10**4)

# Calculando el valor de Rac
resistorAC = resistorDC*(1+c**2/12 -c**4/180)


# Mostrando el resultado 
print(f"El valor de la resistencia en AC es {round(resistorAC,6)} Ω/km")

