from colorama import init, Fore  
import pandas as pd 
from ETL import eliminar_filas, sustituir_valores, convertir_tipo_dato, convertir_fechas, reemplazar_nulos, agrupar_y_calcular, total_personas, ajustar_valores, redondear_valores, ordenar_por_columna, eliminar_duplicados, limpiar_telefonos 

# Requisitos para el funcionamiento del código
# pip install pandas
# pip install colorama
# pip install openpyxl para poder abrir archivo xlsx
# pip install re 

init(autoreset=True) # Inicializar colorama 

def mostrar_menu(): # Opciones básicas del menú
    print(f"{Fore.YELLOW}\n   SYSTEMA ETL\n")
    print(f"{Fore.GREEN}1) Cargar datos")
    print(f"{Fore.GREEN}2) Aplicar limpieza y transformación")
    print(f"{Fore.GREEN}3) Guardar datos")
    print(f"{Fore.GREEN}4) Salir")


def cargar_datos(): # Cargar los datos del dataset
    global df 
    
    while True:
        print(f"{Fore.LIGHTBLUE_EX}\nEn qué formato se encuentra el archivo? (CSV, EXCEL o JSON)\n")
        print(f"{Fore.GREEN}1) CSV")
        print(f"{Fore.GREEN}2) EXCEL")
        print(f"{Fore.GREEN}3) JSON")
        print(f"{Fore.GREEN}4) Atrás")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            archivo = input("Ingrese el nombre del archivo (tambien incluya la entensión .csv): ")
            ruta = r'C:\Users\Josan\ETL\ETL\datasets' + '\\' + archivo + '.csv' #Cambiar la ruta
            try:
                df = pd.read_csv(ruta)  # Se carga el archivo CSV
                print(f"{Fore.YELLOW}\nDatos cargados correctamente :)\n")
                print(df.head(3))  # Muestra las primeras filas para verificar
                return df
            
            except Exception as e:
                print(f"{Fore.RED}Error al cargar: {e}")     
        
        elif opcion == "2":
            archivo = input("Ingrese el nombre del archivo (tambien incluya la entensión .xlsx): ")
            ruta = r'C:\Users\Josan\ETL\ETL\datasets' + '\\' + archivo + '.xlsx' #Cambiar la ruta
            try:
                df = pd.read_excel(ruta)  # Se carga el archivo Excel
                print(f"{Fore.YELLOW}\nDatos cargados correctamente :)\n")
                print(df.head(3))  # Muestra las primeras filas para verificar
                return df
           
            except Exception as e:
                print(f"{Fore.RED}Error al cargar: {e}")
        
        elif opcion == "3":
            archivo = input("Ingrese el nombre del archivo (tambien incluya la entensión .json): ")
            ruta = r'C:\Users\Josan\ETL\ETL\datasets' + '\\' + archivo  + '.json'#Cambiar la ruta
            try:
                df = pd.read_json(ruta)  # Se carga el archivo JSON
                df = pd.json_normalize(df["data"])  # Si los datos están bajo una clave "data"
                print(f"{Fore.YELLOW}\nDatos cargados correctamente :)\n")
                print(df.head(3))  # Muestra las primeras filas para verificar
                return df
           
            except Exception as e:
                print(f"{Fore.RED}Error al cargar: {e}")
        
        elif opcion == "4":
            break  # Se finaliza la ejecución
       
        else:
            print(f"{Fore.RED}\nLa opción seleccionada es inválida, inténtelo de nuevo :(")


def limpieza_transformacion(df):
    while True:
        print(f"{Fore.LIGHTBLUE_EX}\n¿Que desea hacer?\n")  # Lo de "Función X" se va a modificar 
        print(f"{Fore.GREEN} 1) Eliminar filas con valores nulos en ciertas columnas")
        print(f"{Fore.GREEN} 2) Remplazar valores erróneos")
        print(f"{Fore.GREEN} 3) Cambiar tipo de dato de columna")
        print(f"{Fore.GREEN} 4) Convertir fechas")
        print(f"{Fore.GREEN} 5) Remplazar valores nulos")
        print(f"{Fore.GREEN} 6) Agrupar y calcular")
        print(f"{Fore.GREEN} 7) Calcular total de personas")
        print(f"{Fore.GREEN} 8) Ajustar valores min y max")
        print(f"{Fore.GREEN} 9) Redondear valores numéricos")
        print(f"{Fore.GREEN}10) Ordenar por columnas")
        print(f"{Fore.GREEN}11) Identificar y eliminar registros duplicados")
        print(f"{Fore.GREEN}12) Limpiar y formatear números de teléfono")
        print(f"{Fore.GREEN}13) Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print(f"{Fore.YELLOW}Columnas disponibles: {list(df.columns)}")
            columnas = input(f"{Fore.YELLOW}Ingrese las columnas separadas por comas donde desea eliminar filas con valores nulos: ").split(",")
            columnas = [col.strip() for col in columnas]  # Eliminar espacios adicionales

            # Verificar si las columnas ingresadas existen en el DataFrame
            columnas_invalidas = [col for col in columnas if col not in df.columns]
            if columnas_invalidas:
                print(f"{Fore.RED}Las siguientes columnas no existen en el DataFrame: {columnas_invalidas}")
            else:
                df = eliminar_filas(df, columnas)
                print(f"{Fore.GREEN}\nTERMINADO :)")
                print(df.head(10))  # Mostrar las primeras filas para verificar el resultado

        elif opcion == "2":
            columna = input(f"{Fore.YELLOW}Ingrese la columna: ") # Seleccionar columna a modificar
            valores_erroneos = input(f"{Fore.YELLOW}Ingrese los valores erróneos, separados por coma: ").split(",") #Ingresar valores que son incorrectos
            valor_nuevo = input(f"{Fore.YELLOW}Ingrese el valor para sustituir: ") # Ingresar el nuevo valor
            df = sustituir_valores(df, columna, valores_erroneos, valor_nuevo)  # Se sustituyen los valores
            print(f"{Fore.GREEN}\nTERMINADO :)")
            print(df[columna].head(10)) 

        elif opcion == "3":
            columna = input(f"{Fore.YELLOW}Ingrese el nombre de la columna a convertir (int, float o str): ")  # Seleccionar columna a modificar
            print(f"{Fore.YELLOW}\n¿A qué tipo de dato desea convertir?")
            print(f"{Fore.GREEN}1) Entero (int)")
            print(f"{Fore.GREEN}2) Decimal (float)")
            print(f"{Fore.GREEN}3) Texto (str)")
            tipo_dato = input("\nSeleccione una opción: ")

            # Determina el tipo de dato deseado
            if tipo_dato == "1":
                nuevo_tipo = int
            elif tipo_dato == "2":
                nuevo_tipo = float
            elif tipo_dato == "3":
                nuevo_tipo = str
            else:
                print(f"{Fore.RED}\nOpción inválida. Intente de nuevo :(\n")
                continue

            # Convertimos el tipo de dato
            try:
                df = convertir_tipo_dato(df, columna, nuevo_tipo)  # Llamar a la función
                print(f"{Fore.GREEN}\nTERMINADO :)")
            except Exception as e:
                print(f"{Fore.RED}\nError: {e}")

        elif opcion == "4":
            columna = input(f"{Fore.YELLOW}Ingrese el nombre de la columna con fechas: ") # Se ingresa el nombre de la columna a modificar
            df = convertir_fechas(df, columna)  # Se llama la función
            print(f"{Fore.GREEN}\nTERMINADO :) \n")

        elif opcion == "5":
            columna = input(f"{Fore.YELLOW}Ingrese el nombre de la columna a modificar: ")  # Seleccionar columna a modificar
            valor_nuevo = input(f"{Fore.YELLOW}Ingrese el valor para sustituir: ")  # Ingresar el nuevo valor
            df = reemplazar_nulos(df, columna, valor_nuevo)
            print(f"{Fore.GREEN}\nTERMINADO :)")

        elif opcion == "6":
            print(f"{Fore.YELLOW}Columnas disponibles: {list(df.columns)}")
            columna_grupo = input(f"{Fore.YELLOW}Ingrese la columna por la que desea agrupar: ").strip()
            columna_calculo = input(f"{Fore.YELLOW}Ingrese la columna sobre la que desea calcular: ").strip()
            print(f"{Fore.YELLOW}\nOperaciones disponibles: suma, promedio, conteo, max, min")
            operacion = input(f"{Fore.YELLOW}Ingrese la operación que desea realizar: ").strip()

            resultado = agrupar_y_calcular(df, columna_grupo, columna_calculo, operacion)
            if resultado is not None:
                print(f"{Fore.GREEN}\nResultado del agrupamiento y cálculo:\n")
                print(resultado)

        elif opcion == "7":
            df = total_personas(df)  # Llamar a la función
            print(f"{Fore.GREEN}\nTERMINADO :) \n")

        elif opcion == "8":
            try:
                columna = input(f"{Fore.YELLOW}Ingrese el nombre de la columna a ajustar: ")
                min_valor = float(input(f"{Fore.YELLOW}Ingrese el valor mínimo permitido: "))
                max_valor = float(input(f"{Fore.YELLOW}Ingrese el valor máximo permitido: "))

                df = ajustar_valores(df, columna, min_valor, max_valor)  # Llamamos a la función
                print(f"{Fore.GREEN}\nTERMINADO :) \n")

            except Exception as e:
                print(f"{Fore.RED}\nError: {e}\n")

        elif opcion == "9":
            columna = input(f"{Fore.YELLOW}Ingrese el nombre de la columna a redondear: ")  # Seleccionar columna a modificar
            decimales = int(input(f"{Fore.YELLOW}Ingrese el número de decimales a redondear: "))  # Ingresar el número de decimales
            df = redondear_valores(df, columna, decimales)  # Llamar a la función para redondear valores
            print(f"{Fore.GREEN}\nTERMINADO :)")
            print(df.head(10))  # Mostrar las primeras filas para verificar el redondeo

        elif opcion == "10":
            columna = input(f"{Fore.YELLOW}Ingrese el nombre de la columna por la que desea ordenar: ")
            print(f"{Fore.YELLOW}\n¿En qué orden desea ordenar?")
            print(f"{Fore.GREEN}1) Ascendente")
            print(f"{Fore.GREEN}2) Descendente")
            orden = input("\nSeleccione una opción: ")
            ascendente = True if orden == "1" else False

            df = ordenar_por_columna(df, columna, ascendente)
            print(f"{Fore.GREEN}\nTERMINADO :)")
            print(df.head(10))  # Mostrar las primeras filas para verificar el orden

        elif opcion == "11":
            print(f"{Fore.YELLOW}Columnas disponibles: {list(df.columns)}")
            columnas = input(f"{Fore.YELLOW}Ingrese las columnas separadas por comas para eliminar duplicados (o presione Enter para todas): ").split(",")
            columnas = [col.strip() for col in columnas if col.strip()]  # Eliminar espacios adicionales

            if not columnas:
                df = eliminar_duplicados(df)  # Eliminar duplicados en todas las columnas
            else:
                df = eliminar_duplicados(df, columnas=columnas)  # Eliminar duplicados en columnas específicas

            print(f"{Fore.GREEN}\nTERMINADO :)")
            print(df.head(10))  # Mostrar las primeras filas para verificar el resultado      

        elif opcion == "12":
            columna = input(f"{Fore.YELLOW}Ingrese el nombre de la columna con números de teléfono: ")  # Seleccionar columna a modificar
            limpiar_telefonos(df, columna)
            print(f"{Fore.GREEN}\nTERMINADO :)")

        elif opcion == "13":
            break  # Se finaliza la ejecución

        else:
            print(f"{Fore.RED}\nLa opción seleccionada es inválida, inténtelo de nuevo :(\n")
    
    return df

def guardar_datos(): # Guardar las modificaciones en el formato deseado
    global df
    
    while True:
        print(f"{Fore.LIGHTBLUE_EX}\nEn qué formato desearía guardar los cambios? (CSV, EXCEL o JSON)\n")
        print(f"{Fore.GREEN}1) CSV")
        print(f"{Fore.GREEN}2) EXCEL")
        print(f"{Fore.GREEN}3) JSON")
        print(f"{Fore.GREEN}4) Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            archivo = input("\nIngrese el nombre del archivo e incluya la extensión .csv: ")
            try:
                df.to_csv(archivo, index=False)  # Guardar como CSV
                print(f"{Fore.GREEN}\nArchivo guardado :)")
            
            except Exception as e:
                print(f"{Fore.RED}\nError al guardar: {e}")

        elif opcion == "2":
            archivo = input("\nIngrese el nombre del archivo e incluya la extensión .xlsx: ")
            try:
                df.to_excel(archivo, index=False)  # Guardar como Excel
                print(f"{Fore.GREEN}\nArchivo guardado :)")
            
            except Exception as e:
                print(f"{Fore.RED}\nError al guardar: {e}")

        elif opcion == "3":
            archivo = input("\nIngrese el nombre del archivo e incluya la extensión .json: ")
            try:
                df.to_json(archivo, orient="records", lines=True)  # Guardar como JSON
                print(f"{Fore.GREEN}\nArchivo guardado :)")
            
            except Exception as e:
                print(f"{Fore.RED}\nError al guardar: {e}")

        elif opcion == "4":
            break  # Se finaliza la ejecución
       
        else:
            print(f"{Fore.RED}\nLa opción seleccionada es inválida, inténtelo de nuevo :(")

def main():
    global df  
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            cargar_datos()

        elif opcion == "2":
            # Actualiza el DataFrame global después de aplicar transformaciones
            df = limpieza_transformacion(df)

        elif opcion == "3":
            guardar_datos()

        elif opcion == "4":
            print(f"{Fore.LIGHTMAGENTA_EX}\nHasta la próxima :D\n")
            break  # Se finaliza la ejecución

        else:
            print(f"{Fore.RED}\nLa opción seleccionada es inválida, inténtelo de nuevo :(")


if __name__ == "__main__":
    main()