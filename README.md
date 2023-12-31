# Flores_Amarillas

Para convertir tu código de Python en un ejecutable que se pueda ejecutar en cualquier 
computadora, puedes utilizar una herramienta como PyInstaller. PyInstaller toma tu script 
de Python y lo empaqueta junto con el intérprete de Python en un ejecutable independiente 
que puede ser ejecutado en máquinas que no tengan Python instalado. Aquí tienes los pasos para hacerlo:

1. Instala PyInstaller si aún no lo tienes instalado. Puedes hacerlo utilizando pip:

pip install pyinstaller

2. Abre una terminal (en Windows, puedes utilizar el símbolo del sistema o PowerShell) 
y navega hasta la ubicación donde se encuentra tu script de Python "Girasol.py".

3. Ejecuta el siguiente comando para crear el ejecutable:

pyinstaller --onefile Girasol.py

Esto le indicará a PyInstaller que cree un ejecutable único (un solo archivo) a partir de 
tu script "Girasol.py". El ejecutable se generará en una carpeta llamada "dist" 
en el mismo directorio donde se encuentra tu script.

4. Una vez que PyInstaller haya terminado de trabajar, podrás encontrar el ejecutable en la 
carpeta "dist". El nombre del ejecutable será el mismo que el nombre de tu script seguido de ".exe" 
en Windows o sin extensión en sistemas Unix/Linux.

5. Copia este ejecutable a la computadora en la que deseas ejecutarlo. Debería poder 
ejecutarlo sin necesidad de tener Python instalado.
