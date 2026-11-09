#Logica principal , más llamados a mis funciones
import os
os.system("cls")
from functions import *

#variables o flujo de mi proyecto
anio_actual = 2026
nombre = "Benja"



#Lllamado a mis funciones
saludar()
print("********")
obtener_nombre(nombre)
print("********")
retorno_anio = obtener_anio(anio_actual)
print(f" El año actual es: {retorno_anio}")
print("********")

