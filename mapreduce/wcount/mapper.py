import glob
import sys
print("HOLA")

"""
Mapper de MaxTemp
Obtenido de http://exponentis.es/
"""

folder = sys.stdin.read()
print(folder)

for file in glob.glob(folder, recursive=True):
    print(file)

#     # Por cada medida calculamos los pares <anyo, temp>
# for linea in sys.stdin:
#     linea = linea.strip()
#     anyo, mes, temp = linea.split("\t", 2)
#     print("%s\t%s" % (anyo, temp))
