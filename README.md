# TP-Integrador-1
# Procesamiento de datos meteorológicos

## 1) Descripción del proyecto

Este proyecto consiste en un programa desarrollado en Python que procesa archivos de texto con registros meteorológicos del Servicio Meteorológico Nacional (SMN).

El programa lee los datos del archivo de entrada, valida los registros y separa aquellos que son válidos de los que contienen errores. Finalmente, genera un archivo JSON con los resultados del procesamiento y muestra un resumen por consola con la cantidad de registros leídos, válidos e inválidos.

## 2) Requisitos y preparación

Para ejecutar el programa se necesita tener instalado **Python 3**.

No es necesario instalar bibliotecas externas si se utilizan únicamente módulos de la biblioteca estándar de Python.

Los módulos utilizados pueden incluir:

* `sys`: para acceder a los argumentos recibidos desde la terminal.
* `json`: para generar el archivo JSON.
* `os`: para realizar operaciones relacionadas con archivos y rutas.
* `datetime`: para validar las fechas de los registros.

Antes de ejecutar el programa, se debe disponer del archivo de texto con los datos meteorológicos y ubicarlo en una ruta accesible.

## 3) Archivos del proyecto

El proyecto está organizado en módulos para separar las distintas responsabilidades del programa.

* `conversor_json.py`: módulo principal que coordina la ejecución del programa.
* `validaciones.py`: contiene las funciones auxiliares para el procesamiento de los datos, las funciones encargadas de comprobar que los datos meteorológicos cumplan con los criterios de validación, y la generación del archivo de salida.
* `archivo (.txt)`: archivo de entrada que contiene los registros meteorológicos que se desean procesar.

## 4) Ejecución del programa

El programa recibe dos argumentos desde la terminal: la ruta del archivo de entrada y la ruta del archivo JSON de salida.

La ejecución se realiza mediante el siguiente comando:

```bash
python3 conversor_json.py archivo.txt salida.json
```

En Windows también puede utilizarse:

```bash
python conversor_json.py datos.txt salida.json
```

En este ejemplo:

* `archivo.txt` es el archivo de entrada.
* `salida.json` es el archivo que se generará con los resultados.

## 5) Archivo de entrada

El archivo de entrada es un archivo de texto plano (`.txt`) que contiene registros meteorológicos organizados en campos de ancho fijo.

Entre los datos procesados se encuentran:

* **fecha:** fecha de la observación.
* **hora:** hora de la observación.
* **temp:** temperatura registrada.
* **hum:** humedad relativa.
* **pnm:** presión a nivel del mar.
* **dd:** dirección del viento.
* **ff:** velocidad del viento.
* **nombre:** estación meteorológica correspondiente al registro.

El programa ignora las líneas de encabezado y las líneas vacías. Los registros se someten a validaciones de formato y de rango de valores. Cuando un dato no está disponible, puede representarse mediante un valor nulo en el JSON, según las reglas de procesamiento implementadas.

## 6) Archivo de salida

El archivo de salida es un documento JSON (`.json`) que contiene la información obtenida durante el procesamiento.

El documento se organiza en tres secciones principales:

### 6.a) `informacion`

Contiene los datos generales del procesamiento:

* `cantidad_registros`: cantidad total de registros procesados.
* `cantidad_validos`: cantidad de registros que superaron las validaciones.
* `cantidad_invalidos`: cantidad de registros que presentaron errores.

### 6.b) `registros_validos`

Contiene los registros que superaron las validaciones, agrupados por nombre de estación meteorológica.

Cada estación incluye los campos correspondientes a la fecha, la hora, la temperatura, la humedad, la presión a nivel del mar, la dirección del viento y la velocidad del viento.

Los valores de las mediciones se almacenan en listas, de manera que se puedan conservar las observaciones correspondientes a los distintos horarios.

### 6.c) `registros_invalidos`

Contiene una lista con los registros que no superaron las validaciones.

Cada elemento incluye:

* `linea_numero`: número de línea del archivo de entrada.
* `motivo`: descripción del error detectado.
* `contenido`: contenido original de la línea que presentó el error.

De esta manera, es posible identificar los datos que no pudieron procesarse correctamente y conocer el motivo del rechazo.

## 7) Validaciones y manejo de errores

El programa realiza controles sobre los datos meteorológicos, incluyendo el formato de las fechas, el rango de las horas y los límites permitidos para determinadas mediciones.

Los registros que presentan errores se almacenan en la sección `registros_invalidos`, sin interrumpir el procesamiento de los demás registros.

Además, se contemplan errores relacionados con los argumentos de ejecución y con la lectura o escritura de archivos. Cuando ocurre uno de estos problemas, el programa muestra un mensaje explicativo en la terminal.

## 8) Resultados

Al finalizar la ejecución, el programa genera el archivo JSON de salida y muestra un resumen por consola con la cantidad de registros procesados, la catidad de estaciones validadas, la cantidad de registros válidos e inválidos.

El archivo generado permite consultar las observaciones meteorológicas válidas agrupadas por estación y revisar los registros que presentaron errores durante la validación.
