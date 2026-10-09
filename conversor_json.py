import sys
import validaciones

try:
   ruta, salida = validaciones.validar_argumentos(sys.argv)
except ValueError as error:
    print(f"Error: {error}")
    sys.exit(1)

try:
    datos = validaciones.leer_archivo(ruta)
except OSError as error:
    print(f"Error: {error}")
    sys.exit(1)

registros_json, lineas_invalidas, cantidad_registros, cantidad_validos = validaciones.validar_datos(datos)

try:
    validaciones.crear_json(
        salida,
        registros_json,
        lineas_invalidas,
        cantidad_registros,
        cantidad_validos
    )

except OSError as error:
    print(f"Error: {error}")
    sys.exit(1)

print(f"Procesamiento terminado. Cantidad de Registros: {cantidad_registros} | Estaciones: {len(registros_json)} | Lineas Validadas: {cantidad_validos} | Lineas Invalidadas: {len(lineas_invalidas)}")  
