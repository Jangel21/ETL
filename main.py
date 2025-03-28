from colorama import init, Fore  #pip install colorama
import ETL

init(autoreset=True) # Inicializar colorama 

def mostrar_menu(): # Opciones básicas del menú
    print(f"{Fore.YELLOW}\n   SYSTEMA ETL\n")
    print(f"{Fore.GREEN}1) Cargar datos")
    print(f"{Fore.GREEN}2) Aplicar limpieza y transformación")
    print(f"{Fore.GREEN}3) Guardar datos")
    print(f"{Fore.GREEN}4) Salir")

def cargar_datos(): # Cargar los datos del dataset
    print("\nDatos cargados correctamente\n")

def limpieza_transformacion():
    while True:
        print(f"{Fore.LIGHTBLUE_EX}\nQue desea hacer?\n")  # Lo de "Función X" se va a modificar 
        print(f"{Fore.GREEN}1) Función 1")
        print(f"{Fore.GREEN}2) Función 2")
        print(f"{Fore.GREEN}3) Función 3")
        print(f"{Fore.GREEN}4) Función 4")
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
            print(f"{Fore.RED}\nLa opción seleccionada es inválida, inténtelo de nuevo :(\n")

def guardar_datos(): # Guardar las modificaciones en el formato deseado
    while True:
        print(f"{Fore.LIGHTBLUE_EX}\nEn qué formato desearía guardar los cambios? (CSV, EXCEL o JSON)\n")
        print(f"{Fore.GREEN}1) CSV")
        print(f"{Fore.GREEN}2) EXCEL")
        print(f"{Fore.GREEN}3) JSON")
        print(f"{Fore.GREEN}4) Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\nFunción para guardar en CSV")
        elif opcion == "2":
            print("\nFunción para guardar en EXCEL")     
        elif opcion == "3":
            print("\nFunción para guardar en JSON")
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
            limpieza_transformacion()
        elif opcion == "3":
            guardar_datos()
        elif opcion == "4":
            print(f"{Fore.LIGHTMAGENTA_EX}\nHasta la proxima :D\n")
            break  # Se finaliza la ejecución
        else:
            print(f"{Fore.RED}\nLa opción seleccionada es inválida, inténtelo de nuevo :(")

if __name__ == "__main__":
    main()