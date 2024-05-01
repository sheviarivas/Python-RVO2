#!/usr/bin/env python
 
num_agents = 4
contador = 0

# Abre el archivo en modo lectura
with open('hola.txt', 'r') as archivo:
    # Itera sobre cada línea en el archivo
    for linea in archivo:
        
        # Divide la línea en columnas (suponiendo que están separadas por espacios)
        columnas = linea.split()
        
        # Procesa cada columna
        print("step: " + columnas[0])
        print("time: " + columnas[1])
        for i in range (2, len(columnas), 2):
            print("x: " + columnas[i] + " y: " + columnas[i+1])

    print (archivo)    

# Abrir el archivo en modo lectura
with open('hola.txt', 'r') as archivo:
    # Leer todas las líneas del archivo
    lineas = archivo.readlines()

# Acceder a la línea deseada (por ejemplo, la línea número 5)
linea_deseada = lineas[4]  # El índice es 4 ya que en Python se indexa desde 0
print(linea_deseada)
print(len(lineas))
