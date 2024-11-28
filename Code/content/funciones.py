# funciones.py
# Aquí se encuentra la primera opción (lista de campeones)
# además, también está la función de comparar los campeones.

# Aquí se iban a compilar todas las funciones, pero se volvería extenso y laberíntico.
# Como versión final, solo quedó la lista y la comparación.

from colorama import init, Fore
import os
import time

init(autoreset=True)

## Funciones utilizadas para mostrar los campeones.

def mostrar_campeones(campeones_lista):
    total_campeones = len(campeones_lista)
    campeones_por_pagina = 9
    pagina_actual = 0

    while True:
        # Calcular los índices de los campeones a mostrar en esta página
        inicio = pagina_actual * campeones_por_pagina
        fin = inicio + campeones_por_pagina
        campeones_pagina = campeones_lista[inicio:fin]

        # Mostrar campeones de la página actual
        os.system('cls')
        from art.ascii import title_lvl_champ
        print(Fore.CYAN + title_lvl_champ)
        print(Fore.CYAN + "\n--- Lista de Campeones ---")
        for i, campeon in enumerate(campeones_pagina, start=1):
            print(Fore.CYAN + f"[{i}]" + Fore.WHITE + f" {campeon['nombre']} -" + Fore.CYAN + " Rol: " + Fore.WHITE + f"{campeon['rol']}")

        # Mensajes para navegación y búsqueda
        print(Fore.BLUE + "\nOpciones:")
        if pagina_actual > 0:
            print(Fore.CYAN + "[P]" + Fore.WHITE + " - Página anterior")
        if fin < total_campeones:
            print(Fore.CYAN + "[N]" + Fore.WHITE + " - Página siguiente")
        print(Fore.LIGHTCYAN_EX + "[B]" + Fore.WHITE + " - Buscar un campeón por nombre")
        print(Fore.LIGHTRED_EX + "[Q]" + Fore.WHITE + " - Salir")

        # Obtener entrada del usuario
        opcion = input(Fore.CYAN + "\nSeleccione una opción: " + Fore.WHITE).strip().lower()

        if opcion == 'p' and pagina_actual > 0:
            pagina_actual -= 1
        elif opcion == 'n' and fin < total_campeones:
            pagina_actual += 1
        elif opcion == 'b':
            # Opción de búsqueda
            nombre_busqueda = input(Fore.LIGHTCYAN_EX + "Introduce el nombre del campeón: " + Fore.WHITE).strip().lower()
            campeon_encontrado = None
            for campeon in campeones_lista:
                if campeon['nombre'].lower() == nombre_busqueda:
                    campeon_encontrado = campeon
                    break

            if campeon_encontrado:
                mostrar_detalles_campeon(campeon_encontrado)
            else:
                print(Fore.RED + f"[X] CAMPEÓN " + Fore.LIGHTRED_EX + f"{nombre_busqueda}" + Fore.RED + " NO ENCONTRADO." + Fore.WHITE + " Intenta nuevamente.")
                time.sleep(1)
        elif opcion == 'q':
            break
        elif opcion.isdigit():
            seleccion = int(opcion)
            if 1 <= seleccion <= len(campeones_pagina):
                campeon_seleccionado = campeones_pagina[seleccion - 1]
                mostrar_detalles_campeon(campeon_seleccionado)
            else: 
                print(Fore.RED + "[X] OPCIÓN INVÁLIDA." + Fore.WHITE + " El número seleccionado no corresponde a un campeón en esta página.")
                time.sleep(0.5)
        else:
            print(Fore.RED + "[X] OPCIÓN INVÁLIDA." + Fore.WHITE + " Intenta nuevamente.")
            time.sleep(0.5)

def mostrar_detalles_campeon(campeon): # Muestra la información del personaje en profundidad
    # La información obtenida se proporciona por datos_campeones.py
    os.system('cls')
    from art.ascii import champlist_details_title
    print(Fore.CYAN + champlist_details_title)
    print(Fore.CYAN + f"\n--- Detalles de {campeon['nombre']} (Nivel 1) ---")
    print(Fore.LIGHTCYAN_EX + f"Rol: " + Fore.WHITE + f"{campeon['rol']}")
    print(Fore.LIGHTCYAN_EX + f"Vida: " + Fore.WHITE + f"{campeon['vida']}")
    print(Fore.LIGHTCYAN_EX + f"Daño de ataque: " + Fore.WHITE + f"{campeon['daño_de_ataque']}")
    print(Fore.LIGHTCYAN_EX + f"Armadura: " + Fore.WHITE + f"{campeon['armadura']}")
    print(Fore.LIGHTCYAN_EX + f"Resistencia mágica: " + Fore.WHITE + f"{campeon['resistencia_magica']}")
    print(Fore.LIGHTCYAN_EX + f"Velocidad de ataque: " + Fore.WHITE + f"{campeon['velocidad_de_ataque']}")
    print(Fore.LIGHTCYAN_EX + "Habilidades:")
    for habilidad in campeon["habilidades"]:
        print(Fore.LIGHTYELLOW_EX + f"  - {habilidad}")
    print(Fore.LIGHTCYAN_EX + f"Porcentaje de victoria: " + Fore.WHITE + f"{campeon['porcentaje_victoria']}%")
    print(Fore.LIGHTCYAN_EX + f"Porcentaje de baneo: " + Fore.WHITE + f"{campeon['porcentaje_de_baneo']}%\n")
    
    # Pausa para que el usuario vea los detalles antes de volver a la lista
    input(Fore.LIGHTYELLOW_EX + "\nPresiona [ENTER] para volver a la lista de campeones.")

## Funciones utilizadas para la comparación de campeones.

def calcular_reduccion_defensa(defensa): 
    # Se mantuvo solo la defensa (sin resist. mágica) debido a que no hay una
    # nivelación de daño como Poder de Habilidad (daño mágico) en las estadísticas
    # de los campeones en la página oficial.
    return defensa / (100 + defensa)

def seleccionar_campeon_comparar(campeones_lista):
    os.system('cls')
    total_campeones = len(campeones_lista)
    pagina_actual = 0  # Página inicial
    campeon_seleccionado = None

    while campeon_seleccionado is None:
        inicio = pagina_actual * 9
        fin = inicio + 9
        campeones_pagina = campeones_lista[inicio:fin]

        os.system('cls')
        from art.ascii import title_comp_champ
        print(Fore.CYAN + title_comp_champ)
        print(Fore.CYAN + f"\n--- Página {pagina_actual + 1} ---\n")
        for i, campeon in enumerate(campeones_pagina, start=1):
            print(Fore.CYAN + f"[{i}]" + Fore.WHITE + f" {campeon['nombre']} -" + Fore.CYAN + " Rol: " + Fore.WHITE + f"{campeon['rol']}")

        # Mensaje para seleccionar un campeón o navegar
        print(Fore.LIGHTBLUE_EX + "\nSelecciona un número para elegir un campeón.")
        print(Fore.LIGHTCYAN_EX + "[B]" + Fore.WHITE + " - Buscar un campeón por nombre")
        if inicio + 9 < total_campeones:
            print(Fore.CYAN + "[N]" + Fore.WHITE + " - Página siguiente")
        if pagina_actual > 0:
            print(Fore.CYAN + "[P]" + Fore.WHITE + " - Página anterior")
        print(Fore.LIGHTRED_EX + "[Q]" + Fore.WHITE + " - Salir")

        # Obtener entrada del usuario
        opcion = input(Fore.LIGHTYELLOW_EX + "Opción: " + Fore.WHITE).strip().lower()

        # Opción de búsqueda
        if opcion == 'b':
            nombre_busqueda = input(Fore.LIGHTCYAN_EX + "Introduce el nombre del campeón: " + Fore.WHITE).strip().lower()
            campeon_encontrado = None
            for campeon in campeones_lista:
                if campeon['nombre'].lower() == nombre_busqueda:
                    campeon_encontrado = campeon
                    break
            if campeon_encontrado:
                campeon_seleccionado = campeon_encontrado
                print(Fore.LIGHTYELLOW_EX + "\nHas seleccionado a " + Fore.WHITE + f" {campeon_seleccionado['nombre']}.")
            else:
                print(Fore.LIGHTRED_EX + "[X] CAMPEÓN " + Fore.RED + f"{nombre_busqueda}" + Fore.LIGHTRED_EX + " NO ENCONTRADO." + Fore.WHITE + " Intenta nuevamente.")
                time.sleep(1)
        # Navegación entre páginas
        elif opcion == "n" and inicio + 9 < total_campeones:
            pagina_actual += 1
        elif opcion == "p" and pagina_actual > 0:
            pagina_actual -= 1
        elif opcion == "q":
            break
        # Selección de campeón por número
        elif opcion.isdigit() and 1 <= int(opcion) <= len(campeones_pagina):
            indice = inicio + int(opcion) - 1
            campeon_seleccionado = campeones_lista[indice]
            print(Fore.LIGHTYELLOW_EX + "\nHas seleccionado a " + Fore.WHITE + f"{campeon_seleccionado['nombre']}.")
        else:
            print(Fore.RED + "[X] OPCIÓN INVÁLIDA." + Fore.WHITE + " Intenta nuevamente.")
            time.sleep(1)

    return campeon_seleccionado

def comparar_campeones(campeones_lista): # Selección y comparación
    print(Fore.LIGHTYELLOW_EX + "\nSelecciona el primer campeón para la comparación.")
    time.sleep(1)
    campeon1 = seleccionar_campeon_comparar(campeones_lista)

    if campeon1 is None:
        print(Fore.RED + "[X] " + Fore.LIGHTRED_EX + "OPERACIÓN DE COMPARACIÓN CANCELADA.")
        time.sleep(1)
        return

    print(Fore.LIGHTYELLOW_EX + "\nSelecciona el segundo campeón para la comparación.")
    time.sleep(1)
    campeon2 = seleccionar_campeon_comparar(campeones_lista)

    if campeon2 is None:
        print(Fore.RED + "[X] " + Fore.LIGHTRED_EX + "OPERACIÓN DE COMPARACIÓN CANCELADA.")
        time.sleep(1)
        return

    if campeon1 and campeon2: # Una vez seleccionados (campeon1 y campeon2 tienen valores)
        os.system('cls')
        from art.ascii import comparation_details_title
        print(Fore.CYAN + comparation_details_title)
        print(Fore.LIGHTCYAN_EX + "\n--- Comparación entre " + Fore.LIGHTYELLOW_EX + f"{campeon1['nombre']}" + Fore.WHITE + " y " +  Fore.LIGHTYELLOW_EX + f"{campeon2['nombre']}" + Fore.LIGHTCYAN_EX + " ---")

        # Comparación de Ratio de Victoria
        if campeon1['porcentaje_victoria'] > campeon2['porcentaje_victoria']:
            print(Fore.LIGHTMAGENTA_EX + f"{campeon1['nombre']}" + Fore.WHITE + f" tiene un mayor ratio de victoria ({campeon1['porcentaje_victoria']}%) comparado con " + Fore.LIGHTMAGENTA_EX + f"{campeon2['nombre']}" + Fore.WHITE + f" ({campeon2['porcentaje_victoria']}%).")
        elif campeon1['porcentaje_victoria'] < campeon2['porcentaje_victoria']:
            print(Fore.LIGHTMAGENTA_EX + f"{campeon2['nombre']}" + Fore.WHITE + f"tiene un mayor ratio de victoria ({campeon2['porcentaje_victoria']}%) comparado con " + Fore.LIGHTMAGENTA_EX + f"{campeon1['nombre']}" + Fore.WHITE + f" ({campeon1['porcentaje_victoria']}%).")
        else:
            print(Fore.LIGHTGREEN_EX + "Ambos campeones tienen el mismo ratio de victoria" + Fore.WHITE + f"({campeon1['porcentaje_victoria']}%).")

        # Comparación de Daño de Ataque con Resistencia
        reduccion_ataque_campeon1 = campeon2['daño_de_ataque'] * (1 - calcular_reduccion_defensa(campeon1['armadura']))
        reduccion_ataque_campeon2 = campeon1['daño_de_ataque'] * (1 - calcular_reduccion_defensa(campeon2['armadura']))

        print(Fore.LIGHTMAGENTA_EX + f"{campeon1['nombre']} " + Fore.WHITE + f"recibirá aproximadamente {reduccion_ataque_campeon1:.2f} de daño de ataque reducido de " + Fore.LIGHTMAGENTA_EX + f"{campeon2['nombre']}.")
        print(Fore.LIGHTMAGENTA_EX + f"{campeon2['nombre']} " + Fore.WHITE + f"recibirá aproximadamente {reduccion_ataque_campeon2:.2f} de daño de ataque reducido de " + Fore.LIGHTMAGENTA_EX + f"{campeon1['nombre']}.")
        
        # Comparación de Ban Rate
        if campeon1['porcentaje_de_baneo'] > campeon2['porcentaje_de_baneo']:
            print(Fore.LIGHTMAGENTA_EX + f"{campeon1['nombre']}" + Fore.WHITE + f" es más temido en el meta (Ban Rate: {campeon1['porcentaje_de_baneo']}%) comparado con " + Fore.LIGHTMAGENTA_EX + f"{campeon2['nombre']}" + Fore.WHITE + f" ({campeon2['porcentaje_de_baneo']}%).")
        elif campeon1['porcentaje_de_baneo'] < campeon2['porcentaje_de_baneo']:
            print(Fore.LIGHTMAGENTA_EX + f"{campeon2['nombre']}" + Fore.WHITE + f" es más temido en el meta (Ban Rate: {campeon2['porcentaje_de_baneo']}%) comparado con " + Fore.LIGHTMAGENTA_EX + f"{campeon1['nombre']}" + Fore.WHITE + f" ({campeon1['porcentaje_de_baneo']}%).")
        else:
            print(Fore.LIGHTGREEN_EX + "Ambos campeones tienen el mismo Ban Rate " + Fore.WHITE + f"({campeon1['porcentaje_de_baneo']}%).")

        # Puntaje Combinado
        puntaje_campeon1 = (
            (campeon1['porcentaje_victoria'] * 2)+
            (100 / ( 1 + campeon2['daño_de_ataque'] * (1 - calcular_reduccion_defensa(campeon1['armadura']))))+
            (campeon1['armadura']) +
            (campeon1['vida']) +
            (campeon1['nivel_de_poder'])
        )

        puntaje_campeon2 = (
            (campeon2['porcentaje_victoria'] * 2)+
            (100 / ( 1 + campeon1['daño_de_ataque'] * (1 - calcular_reduccion_defensa(campeon2['armadura']))))+
            (campeon2['armadura']) +
            (campeon2['vida']) +
            (campeon2['nivel_de_poder'])
        )

        if puntaje_campeon1 > puntaje_campeon2:
            print(Fore.LIGHTMAGENTA_EX + f"{campeon1['nombre']}" + Fore.WHITE + f" tiene un puntaje combinado superior ({puntaje_campeon1:.2f}) en comparación con " + Fore.LIGHTMAGENTA_EX + f"{campeon2['nombre']}" + Fore.WHITE + f" ({puntaje_campeon2:.2f}).")
        elif puntaje_campeon1 < puntaje_campeon2:
            print(Fore.LIGHTMAGENTA_EX + f"{campeon2['nombre']}" + Fore.WHITE + f" tiene un puntaje combinado superior ({puntaje_campeon2:.2f}) en comparación con " + Fore.LIGHTMAGENTA_EX + f"{campeon1['nombre']}" + Fore.WHITE + f" ({puntaje_campeon1:.2f}).")
        else:
            print(Fore.LIGHTGREEN_EX + f"Ambos campeones tienen el mismo puntaje combinado " + Fore.WHITE + f"({puntaje_campeon1:.2f}).")
            
        input(Fore.LIGHTYELLOW_EX + "\nPresiona [ENTER] para volver a la lista de campeones.")

    else:
        print(Fore.RED + "[X]" + Fore.WHITE + "No se pudo realizar la comparación debido a una selección incorrecta.")
        time.sleep(1)