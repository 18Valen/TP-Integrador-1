import sys
import json

#FECHA     HORA  TEMP   HUM   PNM    DD    FF     NOMBRE
#         [HOA]  [°C]   [%]  [hPa]  [gr] [km/hr]
#01082026     0  19.5   94  1004.3  250   13     AEROPARQUE AERO

ruta = sys.argv[1]
registros_json = {}
lineas_invalidas = []

with open(ruta, "r") as archivo:
    datos = archivo.readlines()

datos = [linea for linea in datos if "FECHA" not in linea and "HOA" not in linea]

for linea in datos:

    linea = linea.strip().split(maxsplit=7)
    if len(linea) == 8:
        fecha, hora, temp, hum, pnm, dd, ff, nombre = linea
        
        try:
            fecha_val = int(fecha)
            hora_val = int(hora)
            temp_val = float(temp)
            hum_val = int(hum)
            pnm_val = float(pnm)
            dd_val = int(dd)
            ff_val = int(ff)
            nombre_val = str(nombre)


            if not nombre in registros_json:
                registros_json[nombre] = {
                "fecha" : fecha, "hora" : [hora], "temp" : [temp], "hum" : [hum], "pnm" : [pnm], "dd" : [dd], "ff" : [ff]
                }
            else:
                registros_json[nombre]["hora"].append(hora)
                registros_json[nombre]["temp"].append(temp)
                registros_json[nombre]["hum"].append(hum)
                registros_json[nombre]["pnm"].append(pnm)
                registros_json[nombre]["dd"].append(dd)
                registros_json[nombre]["ff"].append(ff)


        except ValueError:
            lineas_invalidas.append(linea)


print(lineas_invalidas)

print()

with open("observaciones.json", "w") as archivo:
    json.dump(registros_json, archivo, indent=4)

# python archivo.py datohorario20261002.txt