import sys
import json
from datetime import datetime

#FECHA     HORA  TEMP   HUM   PNM    DD    FF     NOMBRE
#         [HOA]  [°C]   [%]  [hPa]  [gr] [km/hr]
#01082026     0  19.5   94  1004.3  250   13     AEROPARQUE AERO


ruta = sys.argv[1]
registros_json = {}
lineas_invalidas = []


with open(ruta, "r", encoding="latin-1") as archivo:
    datos = archivo.readlines()


for num_linea, linea_sin_modificar in enumerate(datos, start=1):

    if "FECHA" in linea_sin_modificar or "HOA" in linea_sin_modificar:
        continue

    linea = linea_sin_modificar.rstrip("\n")
    
    try:
        if len(linea) != 100:
            raise ValueError("La línea no tiene la longitud esperada")
        
        fecha = linea[0:8].strip()
        hora = linea[8:14].strip()
        temp = linea[14:20].strip()
        hum = linea[20:25].strip()
        pnm = linea[25:33].strip()
        dd = linea[33:38].strip()
        ff = linea[38:43].strip()
        nombre = linea[43:81].strip()
    
    
        temp_val = float(temp) if temp not in ["", "-", "S/D"] else None
        hum_val = int(hum) if hum not in ["", "-", "S/D"] else None
        pnm_val = float(pnm) if pnm not in ["", "-", "S/D"] else None
        dd_val = int(dd) if dd not in ["", "-", "S/D"] else None
        ff_val = int(ff) if ff not in ["", "-", "S/D"] else None
        
        nombre_val = str(nombre)
        fecha_val = datetime.strptime(fecha, "%d%m%Y")
        hora_val = int(hora)

        if not 0 <= hora_val <= 23:
            raise ValueError("La hora está fuera de rango")
            
        if hum_val is not None and not 0 <= hum_val <= 100:
            raise ValueError("La humedad está fuera de rango")
            
        if dd_val is not None and dd_val != 990 and not 0 <= dd_val <= 360:
            raise ValueError("La dirección del viento está fuera de rango")
            
        if ff_val is not None and ff_val < 0:
            raise ValueError("La velocidad del viento no puede ser negativa")


        if not nombre_val in registros_json:
            registros_json[nombre_val] = {
            "fecha" : fecha, 
            "hora" : [hora_val], 
            "temp" : [temp_val], 
            "hum" : [hum_val], 
            "pnm" : [pnm_val], 
            "dd" : [dd_val], 
            "ff" : [ff_val]
                }
        else:
            registros_json[nombre_val]["hora"].append(hora_val)
            registros_json[nombre_val]["temp"].append(temp_val)
            registros_json[nombre_val]["hum"].append(hum_val)
            registros_json[nombre_val]["pnm"].append(pnm_val)
            registros_json[nombre_val]["dd"].append(dd_val)
            registros_json[nombre_val]["ff"].append(ff_val)


    except ValueError as error:
        lineas_invalidas.append({
            "linea_numero" : num_linea,
            "motivo" : str(error),
            "contenido" : linea_sin_modificar.strip()
        })
        

with open("observaciones2.json", "w", encoding="utf-8") as archivo:
    archivo.write("{\n")

    estaciones = list(registros_json.items())

    for i, (nombre, datos) in enumerate(estaciones):
        archivo.write(f'    {json.dumps(nombre, ensure_ascii=False)}: {{\n')

        for j, (clave, valor) in enumerate(datos.items()):
            archivo.write(
                f'        {json.dumps(clave)}: {json.dumps(valor, ensure_ascii=False)}'
            )

            if j < len(datos) - 1:
                archivo.write(",")

            archivo.write("\n")

        archivo.write("    }")

        if i < len(estaciones) - 1:
            archivo.write(",")

        archivo.write("\n")

    archivo.write("}\n")


with open("lineas_invalidas.json", "w", encoding="utf-8") as archivo:
    json.dump(lineas_invalidas, archivo, indent=4, ensure_ascii=False)


print(f"Procesamiento terminado. Estaciones: {len(registros_json)} | Errores: {len(lineas_invalidas)}")

#python archivo.py datohorario20261002.txt