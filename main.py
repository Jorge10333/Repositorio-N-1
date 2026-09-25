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

def main()->None:
    while True:
        op=menu()
        if op==1:
            print("Agregando paciente")
            agregar_paciente() 
        elif op==2:
            print("Editando paciente")
        elif op==3:
            print("Eliminando paciente")
        elif op==4:
            print("Imprimiendo un paciente")
        elif op==5:
            print("Imprimiendo todos los pacientes")
        elif op==0:
            print("Saliendo del programa")
            break
        

if __name__ == "__main__":
    main()


#Link codigo original
#https://github.com/larriag13/01-poos-n2p1c1.git