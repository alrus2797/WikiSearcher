#!/usr/bin/python
import sys

"""
Reducer de MaxTemp
Obtenido de http://exponentis.es/
"""

subproblema = None
tempMaxima = None

for claveValor in sys.stdin:
    anyo, temp = claveValor.split("\t", 1)

    # convertimos la temp a float
    temp = float(temp)

    # El primer subproblema es el primer anyo de reducer (y la temp máxima de momento también)
    if subproblema == None:
        subproblema = anyo
        tempMaxima = temp

    # si el anyo es del subproblema actual, comprobamos si es la temperatura maxima
    if subproblema == anyo:
        if temp > tempMaxima:
            tempMaxima = temp
    else:  # si ya acabamos con el subproblema, emitimos
        print("%s\t%s" % (subproblema, tempMaxima))

        # Pasamos al siguiente subproblema (de momento la temp es la máxima)
        subproblema = anyo
        tempMaxima = temp

# el anterior bucle no emite el último subproblema
print("%s\t%s" % (subproblema, tempMaxima))
