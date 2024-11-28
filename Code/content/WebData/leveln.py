# leveln.py
# Obtiene valores actualizados desde la página
# oficial de la Wiki de League of Legends.
# Este se encuentra más optimizado que web.py en cuanto a la búsqueda

import requests
from bs4 import BeautifulSoup; from colorama import Fore, init

init(autoreset=True)

# Función para limpiar y convertir a entero o flotante
def limpiar_valor(valor):
    try:
        return float(valor.replace(",", "").replace("+", "").strip())
    except ValueError:
        return None

def obtener_estadisticas(campeon):
    url = f"https://wiki.leagueoflegends.com/en-us/{campeon.replace(' ', '_')}"
    
    # Obtener el contenido de la página
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Intentamos extraer los valores necesarios por 'span'
    try:
        vida_base = soup.find('span', {'id': f'Health_{campeon.replace(" ", "_")}'}).text
        vida_sumatoria = soup.find('span', {'id': f'Health_{campeon.replace(" ", "_")}_lvl'}).text
        daño_base = soup.find('span', {'id': f'AttackDamage_{campeon.replace(" ", "_")}'}).text
        daño_sumatorio = soup.find('span', {'id': f'AttackDamage_{campeon.replace(" ", "_")}_lvl'}).text
        armadura_base = soup.find('span', {'id': f'Armor_{campeon.replace(" ", "_")}'}).text
        armadura_sumatoria = soup.find('span', {'id': f'Armor_{campeon.replace(" ", "_")}_lvl'}).text
        resistencia_magica_base = soup.find('span', {'id': f'MagicResist_{campeon.replace(" ", "_")}'}).text
        resistencia_magica_sumatoria = soup.find('span', {'id': f'MagicResist_{campeon.replace(" ", "_")}_lvl'}).text

        # Limpiar y convertir los valores
        if None not in [vida_base, vida_sumatoria, daño_base, daño_sumatorio, armadura_base, armadura_sumatoria, resistencia_magica_base, resistencia_magica_sumatoria]:
            return {
                'campeon': campeon,
                'vida_base': limpiar_valor(vida_base),
                'vida_sumatoria': limpiar_valor(vida_sumatoria),
                'daño_base': limpiar_valor(daño_base),
                'daño_sumatorio': limpiar_valor(daño_sumatorio),
                'armadura_base': limpiar_valor(armadura_base),
                'armadura_sumatoria': limpiar_valor(armadura_sumatoria),
                'resistencia_magica_base': limpiar_valor(resistencia_magica_base),
                'resistencia_magica_sumatoria': limpiar_valor(resistencia_magica_sumatoria),
            }
        else:
            print(Fore.RED + "[ERROR]" + Fore.LIGHTRED_EX + f" No se encontraron algunos datos para {campeon}")
            return None

    except Exception as e:
        print(Fore.RED + "[ERROR]" + Fore.WHITE + " al obtener datos para" + Fore.LIGHTRED_EX + f" {campeon}: {e}")
        return None

def formatear_valor(valor):
    # Si el valor tiene decimales, lo mostramos con 2 decimales, sino, como entero
    if valor.is_integer():
        return str(int(valor))
    else:
        return f"{valor:.2f}"

def mostrar_estadisticas_por_nivel(datos, nivel): # Mostrar las estadísticas
    from art.ascii import champlvl_details_title
    print(Fore.CYAN + champlvl_details_title)
    print(Fore.CYAN + f"--- {datos['campeon']} " + Fore.WHITE + "- Nivel: " + Fore.YELLOW + f"{nivel}" + Fore.CYAN + " ---")
    print(Fore.LIGHTCYAN_EX + "  - Vida: " + Fore.WHITE + f"{formatear_valor(datos['vida_base'] + datos['vida_sumatoria'] * (nivel - 1))}")
    print(Fore.LIGHTCYAN_EX + "  - Daño de Ataque: " + Fore.WHITE + f"{formatear_valor(datos['daño_base'] + datos['daño_sumatorio'] * (nivel - 1))}")
    print(Fore.LIGHTCYAN_EX + "  - Armadura: " + Fore.WHITE + f"{formatear_valor(datos['armadura_base'] + datos['armadura_sumatoria'] * (nivel - 1))}")
    print(Fore.LIGHTCYAN_EX + "  - Resistencia Mágica: " + Fore.WHITE + f"{formatear_valor(datos['resistencia_magica_base'] + datos['resistencia_magica_sumatoria'] * (nivel - 1))}")