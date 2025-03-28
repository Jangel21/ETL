from colorama import init, Fore  #pip install colorama
import ETL

init() # Inicializar colorama

def mostrar_menu(): # Opciones básicas del menú
    print("\nSYSTEMA ETL")
    print("1) Cargar datos")
    print("2) Aplicar limpieza y transformación")
    print("3) Guardar datos")
    print("4) Salir")

def cargar_datos(): # Cargar los datos del dataset
    print("Datos cargados correctamente")

def limpieza_transformacion():
    while True:
        print("\nQue desea hacer?")  # Lo de "Función X" se va a modificar 
        print("1) Función 1")
        print("2) Función 2")
        print("3) Función 3")
        print("4) Función 4")
        print("5) Función 5")
        print("6) Función 6")
        print("7) Función 7")
        print("8) Función 8")
        print("9) Función 9")
        print("10) Función 10")
        print("11) Función 11")
        print("12) Función 12")
        print("13) Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Función 1")  # Lo de "Función X" se va a modificar 
        elif opcion == "2":
            print("Función 2")
        elif opcion == "3":
            print("Función 3")
        elif opcion == "4":
            print("Función 4")
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
            print("\nLa opción seleccionada es inválida, inténtelo de nuevo :(")

def guardar_datos(): # Guardar las modificaciones en el formato deseado
    while True:
        print("\nEn qué formato desearía guardar los cambios? (CSV, EXCEL o JSON)")
        print("1) CSV")
        print("2) EXCEL")
        print("3) JSON")
        print("4) Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Función para guardar en CSV")
        elif opcion == "2":
            print("Función para guardar en EXCEL")     
        elif opcion == "3":
            print("Función para guardar en JSON")
        elif opcion == "4":
            break  # Se finaliza la ejecución
        else:
            print("\nLa opción seleccionada es inválida, inténtelo de nuevo :(")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_datos()
        elif opcion == "2":
            limpieza_transformacion()
        elif opcion == "3":
            guardar_datos()
        elif opcion == "4":
            print("\nHasta la proxima :D")
            break  # Se finaliza la ejecución
        else:
            print("\nLa opción seleccionada es inválida, inténtelo de nuevo :(")

if __name__ == "__main__":
    main()