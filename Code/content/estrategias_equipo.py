# estrategias_equipo.py
# Aquí se encuentra la función de grafo/sinergias
# y la búsqueda DFS y BFS de campeones.

from content.datos_campeones import campeones_lista
import os; import time; from colorama import init, Fore

init(autoreset=True)

# Definir las sinergias entre los roles proporcionados
sinergias_roles = {
    'Support': ['Tank', 'Mage', 'Assassin', 'Marksman', 'Fighter'],
    'Marksman': ['Support', 'Tank'],
    'Tank': ['Mage', 'Marksman'],
    'Mage': ['Marksman'],
    'Assassin': ['Mage'],
    'Fighter': ['Marksman', 'Tank']
}

# Crear grafo de sinergias entre campeones
def crear_grafo(campeon_seleccionado, campeones_lista, sinergias_roles):
    grafo = {}
    
    # Extraer los roles del campeón seleccionado
    roles_seleccionados = campeon_seleccionado["rol"].split()

    # Crear lista de campeones con sinergias de los roles seleccionados
    campeones_con_sinergia = []
    
    for campeon in campeones_lista:
        if campeon != campeon_seleccionado:
            # Extraer los roles del campeón
            roles_campeon = campeon["rol"].split()
            # Comprobar si los roles del campeón coinciden con las sinergias de los roles seleccionados
            coincidencias = sum(1 for rol_seleccionado in roles_seleccionados for rol in roles_campeon if rol in sinergias_roles.get(rol_seleccionado, []))
            if coincidencias > 0: # Elabora coincidencias según los roles conformados del seleccionado.
                campeones_con_sinergia.append((campeon["nombre"], coincidencias))
    
    # Ordenar campeones por la cantidad de sinergias más fuertes
    campeones_con_sinergia.sort(key=lambda x: x[1], reverse=True)

    # Construir el grafo de sinergias
    for campeon, coincidencias in campeones_con_sinergia:
        grafo[campeon] = coincidencias
    
    return grafo

# Búsqueda DFS (profundidad)
def dfs(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo)
    print(f"{nodo} - Sinergia: {grafo.get(nodo, 'Sin sinergia')}")
    
    for vecino in grafo:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

# Búsqueda BFS (anchura)
def bfs(grafo, nodo):
    visitados = set()
    cola = [nodo]
    while cola:
        nodo = cola.pop(0)
        if nodo not in visitados:
            print(f"{nodo} - Sinergia: {grafo.get(nodo, 'Sin sinergia')}")
            visitados.add(nodo)
            for vecino in grafo:
                if vecino not in visitados:
                    cola.append(vecino)

# Función para seleccionar el campeón y buscar sinergias
def seleccionar_campeon_y_buscar_sinergia():
    while True: # Función búcle para mostrar el listado
        campeon_seleccionado = mostrar_campeones_por_pagina(campeones_lista) 

        if campeon_seleccionado: 
            print(Fore.LIGHTYELLOW_EX + "\nHas seleccionado a " + Fore.WHITE + f"{campeon_seleccionado['nombre']}" + Fore.LIGHTYELLOW_EX + " con el rol " + Fore.LIGHTBLUE_EX + f"{campeon_seleccionado['rol']}")

            # Crear el grafo de sinergias según el campeón elegido
            grafo = crear_grafo(campeon_seleccionado, campeones_lista, sinergias_roles)

            while True:
                # Preguntar si quiere realizar DFS o BFS
                opcion_busqueda = input("\n¿Quieres realizar una búsqueda " + Fore.LIGHTGREEN_EX + "DFS (profundidad)" + Fore.WHITE + " o " + Fore.LIGHTRED_EX + "BFS (anchura) " + Fore.WHITE + "? (d/b): ").strip().lower()

                if opcion_busqueda == 'd':
                    # Mostrar sinergias usando DFS
                    os.system('cls')
                    print(Fore.LIGHTGREEN_EX + "\nBúsqueda DFS (Profundidad):" + Fore.WHITE)
                    dfs(grafo, campeon_seleccionado["nombre"], set())
                    break

                elif opcion_busqueda == 'b':
                    # Mostrar sinergias usando BFS
                    os.system('cls')
                    print(Fore.LIGHTRED_EX + "\nBúsqueda BFS (Anchura):" + Fore.WHITE)
                    bfs(grafo, campeon_seleccionado["nombre"])
                    break

                else:
                    print(Fore.RED + "\n[X]" + Fore.LIGHTRED_EX + " OPCIÓN NO VÁLIDA." + Fore.WHITE + " Por favor selecciona " + Fore.LIGHTGREEN_EX + "'d' para DFS " + Fore.WHITE + "o" + Fore.LIGHTRED_EX + " 'b' para BFS." + Fore.WHITE)
                    time.sleep(0.6)
                    os.system('cls')

            while True: # Preguntar si quiere realizar otra búsqueda
                continuar = input(Fore.LIGHTYELLOW_EX + "\n¿Quieres realizar otra búsqueda? (s/n): " + Fore.WHITE).strip().lower()
                if continuar == 's':
                    os.system('cls')
                    break  # Volver a la lista de campeones
                elif continuar == 'n':
                    return  # Salir y volver al menú principal
                else:
                    print(Fore.RED + "[X]" + Fore.LIGHTRED_EX + " OPCIÓN NO VÁLIDA. " + Fore.WHITE + "Por favor selecciona 's' para continuar o 'n' para volver al menú principal.")
                    time.sleep(0.6)
        else:
            return  # Si no se selecciona ningún campeón, se vuelve al menú principal

# Función para mostrar campeones por página
def mostrar_campeones_por_pagina(campeones_lista):
    campeones_por_pagina = 9
    total_campeones = len(campeones_lista)
    pagina_actual = 0

    while True:
        os.system('cls')
        # Calcular los índices de los campeones a mostrar en esta página
        inicio = pagina_actual * campeones_por_pagina
        fin = inicio + campeones_por_pagina
        campeones_pagina = campeones_lista[inicio:fin]

        from art.ascii import title_strat_champ
        print(Fore.CYAN + title_strat_champ)
        print(Fore.CYAN + "\n--- Lista de Campeones ---")
        for i, campeon in enumerate(campeones_pagina, start=1):
            print(Fore.CYAN + f"[{i}]" + Fore.WHITE + f" {campeon['nombre']} -" + Fore.CYAN + " Rol: " + Fore.WHITE + f"{campeon['rol']}")

        # Opciones para navegación
        print(Fore.BLUE + "\nOpciones:")
        if pagina_actual > 0:
            print(Fore.CYAN + "[P]" + Fore.WHITE + " - Página anterior")
        if fin < total_campeones:
            print(Fore.CYAN + "[N]" + Fore.WHITE + " - Página siguiente")
        print(Fore.LIGHTRED_EX + "[Q]" + Fore.WHITE + " - Salir")
        
        # Obtener entrada del usuario
        opcion = input(Fore.CYAN + "\nSeleccione una opción: " + Fore.WHITE).strip().lower()

        if opcion == 'p' and pagina_actual > 0:
            pagina_actual -= 1
        elif opcion == 'n' and fin < total_campeones:
            pagina_actual += 1
        elif opcion == 'q':
            return None  # Salir al menú principal
        elif opcion.isdigit():
            seleccion = int(opcion)
            if 1 <= seleccion <= len(campeones_pagina):
                return campeones_pagina[seleccion - 1]
            else:
                print(Fore.RED + "[X] OPCIÓN INVÁLIDA." + Fore.WHITE + " El número seleccionado no corresponde a un campeón en esta página.")
                time.sleep(0.6)
        else:
            print(Fore.RED + "[X] OPCIÓN INVÁLIDA." + Fore.WHITE + " Intenta nuevamente.")
            time.sleep(0.5)

# Llamar a la función principal
if __name__ == "__main__":
        seleccionar_campeon_y_buscar_sinergia()