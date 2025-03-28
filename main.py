from colorama import init, Fore  #pip install colorama
import pandas as pd #pip install pandas
import os 
from ETL import sustituir_valores,convertir_tipo_dato, convertir_fechas


# pip install openpyxl para poder abrir archivo xlsx

init(autoreset=True) # Inicializar colorama 

def mostrar_menu(): # Opciones básicas del menú
    print(f"{Fore.YELLOW}\n   SYSTEMA ETL\n")
    print(f"{Fore.GREEN}1) Cargar datos")
    print(f"{Fore.GREEN}2) Aplicar limpieza y transformación")
    print(f"{Fore.GREEN}3) Guardar datos")
    print(f"{Fore.GREEN}4) Salir")

def cargar_datos(): # Cargar los datos del dataset
    global df #definimos df cómo global para que podamos usar df en las otras funciones
    while True:
        print(f"{Fore.LIGHTBLUE_EX}\nEn qué formato se encuentra el archivo? (CSV, EXCEL o JSON)\n")
        print(f"{Fore.GREEN}1) CSV")
        print(f"{Fore.GREEN}2) EXCEL")
        print(f"{Fore.GREEN}3) JSON")
        print(f"{Fore.GREEN}4) Atrás")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            archivo = input("Ingrese el nombre del archivo (tambien incluya la entensión .csv): ")
            ruta = r'C:\Users\Citlali Hermosillo\OneDrive\Escritorio\6° Semestre\Almacenes de Datos\ETL\ETL\datasets' + '\\' + archivo  #Cambiar la ruta
            try:
                df = pd.read_csv(ruta)  # Se carga el archivo CSV
                print(f"{Fore.YELLOW}\nDatos cargados correctamente :)\n")
                print(df.head(3))  # Muestra las primeras filas para verificar
                return df
            except Exception as e:
                print(f"{Fore.RED}Error al cargar: {e}")
        elif opcion == "2":
            archivo = input("Ingrese el nombre del archivo (tambien incluya la entensión .xlsx): ")
            ruta = r'C:\Users\Citlali Hermosillo\OneDrive\Escritorio\6° Semestre\Almacenes de Datos\ETL\ETL\datasets' + '\\' + archivo  #Cambiar la ruta
            try:
                df = pd.read_excel(ruta)  # Se carga el archivo Excel
                print(f"{Fore.YELLOW}\nDatos cargados correctamente :)\n")
                print(df.head(3))  # Muestra las primeras filas para verificar
                return df
            except Exception as e:
                print(f"{Fore.RED}Error al cargar: {e}")
        elif opcion == "3":
            archivo = input("Ingrese el nombre del archivo (tambien incluya la entensión .json): ")
            ruta = r'C:\Users\Citlali Hermosillo\OneDrive\Escritorio\6° Semestre\Almacenes de Datos\ETL\ETL\datasets' + '\\' + archivo  #Cambiar la ruta
            try:
                df = pd.read_json(ruta)  # Se carga el archivo JSON
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
        print(f"{Fore.LIGHTBLUE_EX}\nQue desea hacer?\n")  # Lo de "Función X" se va a modificar 
        print(f"{Fore.GREEN}1) Función 1")
        print(f"{Fore.GREEN}2) Remplazar valores erróneos")
        print(f"{Fore.GREEN}3) Cambiar tipo de dato de columna")
        print(f"{Fore.GREEN}4) Convertir fechas")
        print(f"{Fore.GREEN}5) Función 5")
        print(f"{Fore.GREEN}6) Función 6")
        print(f"{Fore.GREEN}7) Función 7")
        print(f"{Fore.GREEN}8) Función 8")
        print(f"{Fore.GREEN}9) Función 9")
        print(f"{Fore.GREEN}10) Función 10")
        print(f"{Fore.GREEN}11) Función 11")
        print(f"{Fore.GREEN}12) Función 12")
        print(f"{Fore.GREEN}13) Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("Función 1")  # Lo de "Función X" se va a modificar 

        elif opcion == "2":
            columna = input(f"{Fore.YELLOW}Ingrese la columna: ") # Seleccionar columna a modificar
            valores_erroneos = input(f"{Fore.YELLOW}Ingrese los valores erróneos, separados por coma: ").split(",") #Ingresar valores que son incorrectos
            valor_nuevo = input(f"{Fore.YELLOW}Ingrese el valor para sustituir: ") # Ingresar el nuevo valor
            df = sustituir_valores(df, columna, valores_erroneos, valor_nuevo)  # Se sustituyen los valores
            print(f"{Fore.GREEN}\nTERMINADO :)")

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
            print("Función 5")

        elif opcion == "6":
            print("Función 6")

        elif opcion == "7":
            print("Función 7")

        elif opcion == "8":
            print("Función 8")

        elif opcion == "9":
            print("Función 9")

        elif opcion == "10":
            print("Función 10")

        elif opcion == "11":
            print("Función 11")     

        elif opcion == "12":
            print("Función 12")

        elif opcion == "13":
            break  # Se finaliza la ejecución
        else:
            print(f"{Fore.RED}\nLa opción seleccionada es inválida, inténtelo de nuevo :(\n")
    return df

def guardar_datos(): # Guardar las modificaciones en el formato deseado
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
                print(f"{Fore.RED}\nEError al guardar: {e}")

        elif opcion == "4":
            break  # Se finaliza la ejecución
        else:
            print(f"{Fore.RED}\nLa opción seleccionada es inválida, inténtelo de nuevo :(")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            cargar_datos()
        elif opcion == "2":
            limpieza_transformacion(df)
        elif opcion == "3":
            guardar_datos()
        elif opcion == "4":
            print(f"{Fore.LIGHTMAGENTA_EX}\nHasta la proxima :D\n")
            break  # Se finaliza la ejecución
        else:
            print(f"{Fore.RED}\nLa opción seleccionada es inválida, inténtelo de nuevo :(")

if __name__ == "__main__":
    main()