"""  
#verificar la versión
git --version

#configuración inicial (una sola vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tucorreo@ejemplo.com"

#configurar la rama principal
git config --global init.defaultBranch main


Repositorio	        Carpeta del proyecto con historial de versiones
Working directory	Tus archivos tal como están ahora
Staging area	    Zona donde preparas qué cambios irán al próximo commit
Commit	Foto (versión) guardada del proyecto
Branch (rama)	    Línea paralela de desarrollo
Remote	            Copia del repositorio en un servidor (GitHub)


#crear un repositorio local
git init

#conocer el estado de los archivos
git status


"""
#Proyecto ejemplo de control de versiones
class Calculadora:
    def sumar(self, a, b):
        return a + b

