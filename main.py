import os

ejemplo_dir = 'C:\\Users\\Juancarlos\\Downloads'

with os.scandir(ejemplo_dir) as ficheros:
    ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
    print(ficheros)