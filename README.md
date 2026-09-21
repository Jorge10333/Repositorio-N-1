# Repositorio-N-1 
## Luis Arriagada
## markdown
### git clone url_repo .
### git config --global user.name Jorge10333
### git config --global user.email jorgelagos103@gmail.com
### git config --global --list 
### git add . 
### git commit -m "comentario"
### git push origin main

# Repositorio-N-1 
**Autor:** Luis Arriagada  
**Tema:** Comandos básicos de configuración y flujo de trabajo en Git

---

## Guía de Comandos Git

### `git clone url_repo .`
Clona un repositorio remoto en el directorio actual.
* **Detalle:** Al incluir el punto (`.`) al final del comando, el contenido se descarga directamente en la carpeta donde estás ubicado, en lugar de crear una nueva subcarpeta con el nombre del repositorio.

---

### `git config --global user.name "Jorge10333"`
Establece tu nombre de usuario de Git de forma global en tu sistema.
* **Detalle:** La opción `--global` aplica este nombre a todos los repositorios que manejes en tu máquina. Este nombre se asociará a tus commits.

---

### `git config --global user.email "jorgelagos103@gmail.com"`
Configura el correo electrónico del autor a nivel global.
* **Detalle:** Este correo debe coincidir con la cuenta de GitHub (o el servicio Git que uses) para vincular correctamente la autoría de tus cambios.

---

### `git config --global --list`
Muestra en pantalla la lista de todas las configuraciones globales actuales.
* **Detalle:** Permite verificar rápidamente qué nombre de usuario, correo electrónico u otros parámetros están activos en la configuración global de tu sistema.

---

### `git add .`
Añade todos los archivos modificados, creados o eliminados al *Staging Area* (área de preparación).
* **Detalle:** El punto (`.`) le indica a Git que prepare todos los cambios del directorio actual y sus subdirectorios para incluir en el próximo commit.

---

### `git commit -m "comentario"`
Guarda los cambios cargados en el *Staging Area* dentro del historial del repositorio local.
* **Detalle:** La bandera `-m` permite adjuntar un mensaje descriptivo entre comillas que explica brevemente qué cambios o mejoras contiene este commit.