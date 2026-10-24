"""  
#verificar la versión
git --version

#configuración inicial (una sola vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tucorreo@ejemplo.com"

#configurar la rama principal
git config --global init.defaultBranch main

###############################################################
Repositorio	        Carpeta del proyecto con historial de versiones
Working directory	Tus archivos tal como están ahora
Staging area	    Zona donde preparas qué cambios irán al próximo commit
Commit	Foto (versión) guardada del proyecto
Branch (rama)	    Línea paralela de desarrollo
Remote	            Copia del repositorio en un servidor (GitHub)
###########################################################

#crear un repositorio local
git init

#conocer el estado de los archivos
git status

#agregar archivos al área de preparación
git add archivo.txt
git add . #agrega todos los archivos

#guardar los cambios en el repositorio local
git commit -m "Mensaje descriptivo de los cambios"

#cambiar el nombre de la rama principal
git branch -M main 

#agregar un  repositorio remoto (GitHub)
git remote add origin https://github.com/doble-b182/calculadora-Upana-ejemplo.git

git push -u origin main

#VER QUE CAMBIO 
git diff

# Descartar cambios no guardados en un archivo
git restore calculadora.py

#verificar el historial de cambios
git log

"""
#Proyecto ejemplo de control de versiones
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

