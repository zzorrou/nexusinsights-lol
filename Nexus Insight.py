# Nexus_Insight.py
# Archivo principal del programa, verifica que los requisitos estén descargados.
# Además, da un inicio con arte ASCII para mejor visual. 

# Imports de libs (defaults de py)
import time;import sys;import os;import subprocess

def titulo_ventana(title): # Esto solo cambia el título de la ventana
    os.system(f"title {title}")

# Animación de carga
def anim_carga():
    loading_text = "Cargando..."
    animation = ["|", "/", "-", "\\"]
    for i in range(20):
        sys.stdout.write("\r" + loading_text + " " + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.2)
    print("\r" + loading_text + " [COMPLETADO]" + " " * 5)

# Instalación de los requirements.txt
def instalar_reqs():
    print("\nInstalando los requisitos...")
    try:
        # Ejecuta el comando para descargar los requisitos.
        os.system(f"{sys.executable} -m pip install -r requirements.txt")
        print("Requisitos instalados correctamente.")
    except Exception as e:
        print(f"Ocurrió un error durante la instalación de los requisitos: {e}")

# Función para validar que los requisitos estén instalados
def check_reqs():
    try:
        # Obtener lista de pips instalados
        pkg_instalados = subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).decode("utf-8")
        
        # Leer los paquetes requeridos.
        with open('requirements.txt', 'r') as f:
            pkg_necesarios = f.readlines()
        
        # Revisar si cada paquete está instalado
        for pkgs in pkg_necesarios:
            pkgs_name = pkgs.split('==')[0].strip()  # Nombre de los pkgs
            if pkgs_name.lower() not in pkg_instalados.lower():
                return False
        return True
    except Exception as e:
        print(f"Error al verificar los requisitos: {e}")
        return False

# Ejecución del programa inicial (se da una vez que se descargan los requisitos)
def iniciar_programa():
    print("\nIniciando el programa principal...")
    anim_carga()
    try:
        os.system(f"{sys.executable} Code/main.py")
    except Exception as e:
        print(f"Error al ejecutar el programa: {e}")

# Función para abrir el README.md
def abrir_readme():
    print("\nAbriendo README.md...")
    try:
        os.system("notepad README.md" if os.name == "nt" else "open README.md")
        print("README.md abierto correctamente.")
    except Exception as e:
        print(f"Error al abrir README.md: {e}")

# Función para cerrar el programa
def cerrar_programa():
    print("\n[Cerrando el programa...]")
    time.sleep(0.5)
    sys.exit()

# Menú inicial
def main_menu(reqs_instalados):
    while True:
        titulo_ventana("- Nexus Insight ... [ Gestión y Estadísticas de League of Legends ]")
        os.system('color 3')
        arte_ascii = r"""            
       ███████████                      _   __                                
        ██████████  █                  / | / /___   _  __ __  __ _____        
         ████   ██  █████             /  |/ // _ \ | |/_// / / // ___/        
          ███   ██    █████          / /|  //  __/_>  < / /_/ /(__  )         
       █  ███   ██       ████       /_/ |_/_\___//_/|_| \__,_//____/__     __ 
      ██  ███   ██        ████         /  _/____   _____ (_)____ _ / /_   / /_
     ███  ███   ██         ████        / / / __ \ / ___// // __ `// __ \ / __/
     ███  ███   ██          ███      _/ / / / / /(__  )/ // /_/ // / / // /_  
     ███  ███   ██          ███     /___//_/ /_//____//_/ \__, //_/ /_/ \__/  
     ███  ███   ██         ████                          /____/               
      ██  ███   ██             
       █  ███   ███████████████        Trabajo FINAL de Estructura de Datos COM.2
         ████             ████         UNAB 2024 - Alvarez Mauro
        █████████████████████                      Maggi Emiliano
       ████████████████████         
        """
        os.system('cls')
        print(arte_ascii)
        print("\nMenú Principal")
        print("1. Descargar los requisitos (* REQUERIDO)")
    
        if reqs_instalados:
            print("2. Iniciar el programa")
            print("3. Abrir README.md")
            print("4. Cerrar el programa")
        else:
            print("2. Iniciar el programa (Requisitos no instalados)")
            print("3. Abrir README.md")
            print("4. Cerrar el programa")
        
        choice = input("\nSeleccione una opción: ").strip()
        
        if choice == "1":
            instalar_reqs()
            reqs_instalados = check_reqs()  # Actualizar después de instalar
        elif choice == "2" and reqs_instalados:
            iniciar_programa()
        elif choice == "2" and not reqs_instalados:
            print("No se pueden iniciar el programa, los requisitos no están instalados.")
            time.sleep(1)
        elif choice == "3":
            abrir_readme()
        elif choice == "4":
            cerrar_programa()
        else:
            print("Opción inválida, intente nuevamente.")
            time.sleep(0.2)

# Verificación de requisitos antes de mostrar el menú
reqs_instalados = check_reqs()

# Inicio del menú
main_menu(reqs_instalados)