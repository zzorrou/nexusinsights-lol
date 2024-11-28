## web.py
# Aquí se obtienen los roles de los campeones, el tier, su porcentaje de victoria y porcentaje de baneo
# actualizados según la página metasrc, la cual obtiene estadísticas de los campeones (a nivel de META)

# Este estaba pensado ser el método de búsqueda para las estadísticas de los campeones
# pero al ser la lista demasiado larga, iba a causar un bajo rendimiento de el programa.

import requests; from bs4 import BeautifulSoup

def obtener_datos_campeones():
    url = "https://www.metasrc.com/lol/las/stats"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    champions = {}

    # Encuentra la tabla y extrae los datos relevantes
    table = soup.find('table')
    for row in table.find_all('tr')[1:]:  # Saltar encabezados
        columns = row.find_all('td')
        if columns:
            nombre = columns[0].find('img')['alt'].split(',')[0].strip()
            rol = columns[1].text.strip()
            tier = columns[2].text.strip()
            win_percent = columns[5].text.strip()  # WIN% en la columna 5
            ban_percent = columns[8].text.strip()   # BAN% en la columna 8
            
            # Mantener solo el campeón con el mayor tier
            if nombre not in champions or tier < champions[nombre]['tier']:
                champions[nombre] = {
                    'rol': rol,
                    'tier': tier,
                    'win_percent': win_percent,
                    'ban_percent': ban_percent
                }
    
    return champions