# infonivel.py
# Aquí se encuentra el sistema ABB y arboles
# además de mostrar en detalle como incrementa
# el poder de los campeones según su nivel.

# Llama a leveln.py para obtener las estadísticas y el escalado por nivel.
from content.WebData.leveln import obtener_estadisticas, mostrar_estadisticas_por_nivel
from content.datos_campeones import campeones_lista
from colorama import init, Fore;import time; import os

init(autoreset=True)

# Clase Nodo que representa un nodo en el árbol binario de búsqueda (ABB)
class Nodo:
    def __init__(self, campeon):
        self.campeon = campeon  # Información del campeón
        self.izquierdo = None  # Nodo izquierdo
        self.derecho = None    # Nodo derecho

# Clase ABB para organizar los campeones por nivel de poder
class ABB:
    def __init__(self):
        self.raiz = None

# Inserta un campeón al árbol.
    def insertar(self, campeon):
        if self.raiz is None:
            self.raiz = Nodo(campeon) # Si está vacío, crea la raíz.
        else:
            self._insertar_recursivo(self.raiz, campeon) # Si no, lo inserta recursivamente.

# Insertar un campeón adecuadamente al árbol de modo recursivo
    def _insertar_recursivo(self, nodo, campeon):
        if campeon['nivel_de_poder'] < nodo.campeon['nivel_de_poder']: # Compara el nivel de poder
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(campeon) # Insertar al izquierdo si es menor.
            else:
                self._insertar_recursivo(nodo.izquierdo, campeon)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(campeon) # Insertar al derecho si es mayor o igual.
            else:
                self._insertar_recursivo(nodo.derecho, campeon)

# Función para encontrar el mínimo en el árbol
    def _encontrar_minimo(self, nodo):
        while nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo

# Función para encontrar los campeones en orden.
    def mostrar_inorder(self):
        campeones = []
        self._mostrar_inorder_recursivo(self.raiz, campeones)
        return campeones

# Recorrido en orden para llenar la lista de campeones de modo recursivo.
    def _mostrar_inorder_recursivo(self, nodo, lista):
        if nodo:
            self._mostrar_inorder_recursivo(nodo.izquierdo, lista)
            lista.append(nodo.campeon)
            self._mostrar_inorder_recursivo(nodo.derecho, lista)

def mostrar_campeones(campeones_lista):
    total_campeones = len(campeones_lista)
    campeones_por_pagina = 9
    pagina_actual = 0

    # Crear el árbol binario de búsqueda
    arbol = ABB()

    # Insertar los campeones en el árbol
    for campeon in campeones_lista:
        arbol.insertar(campeon)

    while True:
        # Calcular los índices de los campeones a mostrar en esta página
        inicio = pagina_actual * campeones_por_pagina
        fin = inicio + campeones_por_pagina
        campeones_pagina = []
        
        # Recorremos el árbol binario en orden para obtener los campeones
        for idx, campeon in enumerate(arbol.mostrar_inorder(), start=1):
            if inicio < idx <= fin:
                campeones_pagina.append(campeon)
        
        os.system('cls')
        from art.ascii import title_lvl_champ
        print(Fore.CYAN + title_lvl_champ)
        print(Fore.CYAN + "\n--- Lista de Campeones ---")
        for i, campeon in enumerate(campeones_pagina, start=1):
            print(Fore.LIGHTCYAN_EX + f"[{i}] " + Fore.WHITE + f"{campeon['nombre']} -" + Fore.LIGHTYELLOW_EX + f" [ Nivel de Poder: {campeon['nivel_de_poder']} ]")

        # Mensajes para navegación y búsqueda
        print(Fore.CYAN + "\nOpciones:")
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
                # Obtener estadísticas del campeón
                datos = obtener_estadisticas(campeon_encontrado['nombre'])
                if datos:
                    # Mostrar estadísticas por nivel
                    nivel = 1
                    while True:
                        os.system('cls')
                        mostrar_estadisticas_por_nivel(datos, nivel)

                        print(Fore.LIGHTBLUE_EX + "\nOpciones:")
                        print(Fore.LIGHTCYAN_EX + "[S]" + Fore.WHITE + " - Mostrar siguiente nivel")
                        print(Fore.LIGHTCYAN_EX + "[V]" + Fore.WHITE + " - Volver a nivel 1")
                        print(Fore.LIGHTCYAN_EX + "[L]" + Fore.WHITE + " - Volver a la lista de campeones")

                        accion = input(Fore.LIGHTYELLOW_EX + "Seleccione una opción: " + Fore.WHITE).strip().lower()

                        if accion == 's':
                            if nivel < 18:
                                nivel += 1
                            else:
                                print(Fore.LIGHTYELLOW_EX + "Ya estás en el nivel máximo (18).")
                                time.sleep(0.6)
                        elif accion == 'v':
                            nivel = 1
                        elif accion == 'l':
                            break
                        else:
                            print(Fore.RED + "[X]" + Fore.LIGHTRED_EX + " OPCIÓN NO VÁLIDA. " + Fore.WHITE + "Por favor elige una opción correcta.")
                            time.sleep(1.2)
            else:
                print(Fore.RED + "[X] Campeón " + Fore.LIGHTRED_EX + f"{nombre_busqueda}" + Fore.RED + " no encontrado." + Fore.WHITE + " Intenta nuevamente.")
                time.sleep(1.2)
        elif opcion == 'q':
            break
        elif opcion.isdigit():
            seleccion = int(opcion)
            if 1 <= seleccion <= len(campeones_pagina):
                campeon_seleccionado = campeones_pagina[seleccion - 1]
                # Obtener estadísticas del campeón
                datos = obtener_estadisticas(campeon_seleccionado['nombre'])
                if datos:
                    # Mostrar estadísticas por nivel
                    nivel = 1
                    while True:
                        os.system('cls')
                        mostrar_estadisticas_por_nivel(datos, nivel)

                        print(Fore.LIGHTBLUE_EX + "\nOpciones:")
                        print(Fore.LIGHTCYAN_EX + "[S]" + Fore.WHITE + " - Mostrar siguiente nivel")
                        print(Fore.LIGHTCYAN_EX + "[V]" + Fore.WHITE + " - Volver a nivel 1")
                        print(Fore.LIGHTCYAN_EX + "[L]" + Fore.WHITE + " - Volver a la lista de campeones")

                        accion = input(Fore.LIGHTYELLOW_EX + "Seleccione una opción: " + Fore.WHITE).strip().lower()

                        if accion == 's':
                            if nivel < 18:
                                nivel += 1
                            else:
                                print(Fore.LIGHTYELLOW_EX + "Ya estás en el nivel máximo (18).")
                                time.sleep(1.2)
                        elif accion == 'v':
                            nivel = 1
                        elif accion == 'l':
                            break
                        else:
                            print(Fore.RED + "[X]" + Fore.LIGHTRED_EX + " OPCIÓN NO VÁLIDA. " + Fore.WHITE + "Por favor elige una opción correcta.")
                            time.sleep(1.2)
            else:
                print(Fore.RED + "[X]" + Fore.LIGHTRED_EX + "OPCIÓN NO VÁLIDA. " + Fore.WHITE + "El número seleccionado no corresponde a un campeón en esta página.")
                time.sleep(1.2) 
        else:
            print(Fore.RED + "[X]" + Fore.LIGHTRED_EX + " OPCIÓN NO VÁLIDA. " + Fore.WHITE + "Por favor elige una opción correcta.")
            time.sleep(1.2)

if __name__ == "__main__":
    mostrar_campeones(campeones_lista)