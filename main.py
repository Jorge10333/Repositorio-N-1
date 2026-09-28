from paciente import Paciente

pacientes:list[Paciente] = [
    Paciente("11.111.111-1", "Luis Arriagada", 40, "Isapre"),
    Paciente("2.222.222-2", "Paola Pardo", 40, "Fonasa")
    ]

def leer_numero(mensaje: str) -> int:
    while True:
        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def menu() -> int:
    print("Clinica")
    print("1.- Agregar paciente")
    print("2.- Editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Imprimir un paciente")
    print("5.- Imprimir todos los pacientes")
    print("0.- Salir")
    opcion = leer_numero("Seleccione una opción: ")
    return opcion

def agregar_paciente() -> None:
    rut = input("Ingrese el RUT del paciente:")
    nombre = input("Ingrese el nombre del paciente:")
    edad = leer_numero("Ingrese la edad del paciente:")
    print("Previsiones disponibles: ")
    print("1.- Fonasa")
    print("2.- Isapre")
    print("3.- Particular")
    print("4.- Otro")
    print("0.- Salir")
    prevision = leer_numero("Seleccione una previsión: ")
    if prevision == 1:
        prevision = "Fonasa"
    elif prevision == 2:
        prevision = "Isapre"
    elif prevision == 3:
        prevision = "Particular"
    elif prevision == 4:
        prevision = "Otro"
    else:
        prevision = ""
        print("Opcion no valida")
        return
    pacientes.append(Paciente(rut, nombre, edad, prevision))

def imprimir_pacientes() -> None:
    for paciente in pacientes:
        print(paciente)
    else:
        print("No hay pacientes registrados.")

def buscar_paciente() -> Paciente | None: 
    rut = input("Ingrese el RUT del paciente a buscar: ")
    for paciente in pacientes:
        if paciente.rut == rut:
            return paciente
    return None

def imprimir_paciente() -> None: 
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
    else:
        print("Paciente no encontrado.")

def eliminar_paciente() -> None:
    paciente=buscar_paciente()
    if paciente:
        pacientes.remove(paciente)
        print("Paciente eliminado.")
    else:
        print("Paciente no encontrado.")

def editar_paciente() -> None:
    paciente=buscar_paciente()
    if paciente:
        print("Menu edición")
        print("1.- Editar nombre")
        print("2.- Editar edad")
        print("3.- Editar previsión")
        opcion = leer_numero("Seleccione una opción: ")
        if opcion == 1:
            print(f"Nombre actual: {paciente.nombre}")
            nombre = input("Ingresenuevo nombre: ") 
            paciente.nombre = nombre
        elif opcion == 2: 
            print(f"La edad actual es: {paciente.edad}")
            edad = leer_numero("Ingrese nueva edad: ")
            paciente.edad = edad 
        elif opcion == 3:
            print(f"La previsión actual es: {paciente.prevision}")
            print("Previsiones disponibles: ")
            print("1.- Fonasa")
            print("2.- Isapre")
            print("3.- Particular")
            print("4.- Otro")
            prevision = leer_numero("Seleccione una previsión: ")
            if prevision == 1:
                paciente.prevision = "Fonasa"
            elif prevision == 2:
                paciente.prevision = "Isapre"
            elif prevision == 3:
                paciente.prevision = "Particular"
            elif prevision == 4:
                paciente.prevision = "Otro"
            else:
                print("No se realizaron cambios en la previsión.")
    else:
        print("Paciente no encontrado.")

def main()->None:
    while True:
        op=menu()
        if op==1:
            print("Agregando paciente")
            agregar_paciente() 
        elif op==2:
            print("Editando paciente")
            editar_paciente()
        elif op==3:
            print("Eliminando paciente")
            eliminar_paciente()
        elif op==4:
            print("Imprimiendo un paciente")
            imprimir_paciente()
        elif op==5:
            print("Imprimiendo todos los pacientes")
            imprimir_pacientes() 
        elif op==0:
            print("Saliendo del programa")
            break
        

if __name__ == "__main__":
    main()


#Link codigo original
#https://github.com/larriag13/01-poos-n2p1c1.git