# Requisitos Previos
* Hardware:
   - **Procesador**: Intel Core Pentium o superior. 
   - **Memoria RAM**: 4 GB.
   - **Espacio en disco:** 20 MB disponibles.
* Software:
   - **Python 3.10 o superior.**
   - **Librerías:** colorama, beautifulsoup4, requests, art.
   - **Sistema Operativo:** Windows 10, macOS 10.15 o distribuciones de Linux compatibles con Python.

## Pasos para la Implementación ##
**Clonación del Repositorio:** 
Abra su terminal y ejecute:
> ``git clone https://github.com/zzorrou/nexusinsights-lol.git``
> ``cd nexusinsights-lol/``

## Instalación de Dependencias: ## 
Ejecute el siguiente comando para instalar las librerías necesarias:
> ``pip install -r requirements.txt``
or
> ``py Nexus_Insight.py`` (y seleccionar la opción 1)

## Ejecución del Sistema: ## 
Ejecute el programa con:
> ``python Nexus_Insight.py``

# Manual de Usuario
**Inicio del Programa:** 
Al iniciar, el sistema presentará un menú interactivo con las siguientes opciones:
* **Instalar requerimientos:** Instalará los requerimientos de manera automática para facilitar el trabajo al usuario.
* **Ejecutar el programa:** Permite comenzar y lanzar el programa una vez descargadas las dependencias, mostrando así el menú del programa para comenzar a gestionar y comparar campeones.
* **Leer el** ``README.md``
* **Salir:** Cierra la aplicación de forma segura.

**Ejemplo de Flujo de Uso:**
- Ingrese 1 para **Visualizar Campeones**.
- Ingrese 2 para **Comparar Campeones**. 
- Ingrese 3 para ver la **Evolución por Nivel de Campeones**
- Ingrese 4 para ver las **Estrategias de Equipo**
- Ingrese Q para **Cerrar el Programa.**

# Problemas comunes

``Error: ModuleNotFoundError``
Librerías necesarias no instaladas. Usualmente no ocurre dado a la validación del ``"main.py"``. **Verifique** que ``pip install -r requirements.txt`` se haya ejecutado correctamente.

``Error: FileNotFoundError``
Los archivos esenciales (carpetas como ``\Content`` o ``datos_campeones.py``) no están en el directorio. **Asegúrese** de que los archivos mencionados estén en las carpetas correspondientes del proyecto.

``Salida inesperada al listar campeones.``
El archivo ``datos_campeones.py`` contiene datos mal formateados. Suele ocurrir cuando se modifica dicho archivo y se añaden de manera incorrecta a la lista de campeones. Por defecto no ocurre. **Corrija** la estructura de los datos en el archivo, asegurándose de que sigan el ``formato dictado.``

``No se muestra el menú al ejecutar.``
*Python* no está configurado correctamente en su sistema. **Verifique** su versión de Python con: ``python --version. Use una versión compatible (3.10+).``