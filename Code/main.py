# main.py
# Archivo que conecta con el resto de funcionalidades del programa
# Este es el punto principal antes de ejecutarse ayuda a evitar que hayan problemas
# por falta de archivos, libs, etc.

# Libs utilizadas + descargadas (colorama)
import os;import sys;import time;from colorama import init, Fore

init(autoreset=True)

# Ruta de la carpeta 'content' desde el directorio de ejecución
content_folder = os.path.join(os.path.dirname(__file__), 'content')
clases_file = os.path.join(content_folder, 'clases.py')
datos_campeones_file = os.path.join(content_folder, 'datos_campeones.py')
funciones_file = os.path.join(content_folder, 'funciones.py')
infonivel_file = os.path.join(content_folder, 'infonivel.py')
estrategias_equipo_file = os.path.join(content_folder, 'estrategias_equipo.py')
art_folder = os.path.join(os.path.dirname(__file__), 'art')
ascii_file = os.path.join(art_folder, 'ascii.py')


## Validación de archivos empieza aquí 
# Lista de archivos necesarios
archivos_req = [
    datos_campeones_file,
    funciones_file,
    infonivel_file,
    estrategias_equipo_file,
    ascii_file
]

def verificar_archivo(ruta_archivo): # Verifica que los archivos esten correspondientes a su ubicación.
    if not os.path.exists(ruta_archivo):
        print(Fore.RED + "[ERROR]:" + Fore.LIGHTRED_EX + f" El archivo '{ruta_archivo}' no se encuentra en el directorio 'content'.")
        return False
    return True

def verificar_archivos_req(): # Verifica la lista de archivos individualmente
    print(Fore.CYAN + "[INFO] Verificando archivos requeridos...\n")
    archivos_faltantes = []

    for file in archivos_req:
        if verificar_archivo(file):
            print(Fore.LIGHTGREEN_EX + "[OK]" + Fore.WHITE + f" {os.path.basename(file)}")
        else:
            print(Fore.RED + "[ERROR]" + Fore.LIGHTRED_EX + f" {os.path.basename(file)}")
            archivos_faltantes.append(file)

    if archivos_faltantes: # En caso de faltar archivos, notifica
        print(Fore.RED + "[ERROR CRÍTICO]:" + Fore.LIGHTRED_EX + " No se encontraron los siguientes archivos:")
        for faltante in archivos_faltantes:
            print(Fore.LIGHTRED_EX + f"- {os.path.basename(faltante)}")
        print(Fore.YELLOW + "\n  Por favor, asegúrese de que todos los archivos estén completos y en el lugar correcto.")
        time.sleep(5)
        sys.exit(1)

    # En caso contrario, de estar bien procede.
    print(Fore.LIGHTGREEN_EX + "[OK]" + Fore.WHITE + " Todos los archivos requeridos están verificados.")
    time.sleep(1)

def titulo_ventana(title):
    os.system(f"title {title}")

def mostrar_menu(): # Función de Menú.
    from art.ascii import menu_title
    while True:
        os.system('cls')
        print(Fore.CYAN + menu_title)
        print(Fore.CYAN + "\n------ MENÚ PRINCIPAL ------")
        
        print(Fore.CYAN + "[1]" + Fore.WHITE + " Ver lista de campeones.")
        print(Fore.CYAN + "[2]" + Fore.WHITE + " Comparar campeones.")
        print(Fore.CYAN + "[3]" + Fore.WHITE + " Evolución por nivel de Campeones.")
        print(Fore.CYAN + "[4]" + Fore.WHITE + " Estrategias de Equipo.")
        print(Fore.CYAN + "[Q]" + Fore.WHITE + " Salir.")
        
        opcion = input(Fore.WHITE + "Seleccione una opción: ")

        if opcion == '1': # Lista de campeones
            from content.funciones import mostrar_campeones
            mostrar_campeones(campeones_lista) 
        elif opcion == '2': # Comparación de campeones
            from content.funciones import comparar_campeones
            comparar_campeones(campeones_lista) 
        elif opcion == '3': # Evolución por nivel (ABB + nodos)
            from content.infonivel import mostrar_campeones
            mostrar_campeones(campeones_lista) 
        elif opcion == '4': # Sinergias de Campeones (grafo + dfs y bfs)
            from content.estrategias_equipo import seleccionar_campeon_y_buscar_sinergia
            seleccionar_campeon_y_buscar_sinergia()
        elif opcion == 'q': # Cierre de programa
            break
        else: # Validación de opciones
            print(Fore.RED + "[X] Opción inválida." + Fore.WHITE + " Intente nuevamente.")
            time.sleep(0.3)

if __name__ == "__main__":
    verificar_archivos_req() # Función de verif. archivos
    # Actualizar datos de campeones
    from content.datos_campeones import actualizar_datos_campeones, campeones_lista
    actualizar_datos_campeones()  # Llama a la función para actualizar datos
    
    titulo_ventana("- Nexus Insight ... [ Menú Principal ]")
    mostrar_menu()