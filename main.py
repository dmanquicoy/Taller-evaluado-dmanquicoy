from operaciones import (
    insertar_sala,
    consultar_salas,
    registrar_reserva,
    consultar_reservas,
    cancelar_reserva,
)

while True:
    print("\n--- SISTEMA DE RESERVAS ---")
    print("1. Registrar sala")
    print("2. Consultar salas")
    print("3. Registrar reserva")
    print("4. Consultar reservas")
    print("5. Cancelar reserva")
    print("0. Salir")
    
    try:
        opcion = int(input("\nOpción: "))
        
        if opcion == 1:
            nombre = input("Nombre: ")
            capacidad = int(input("Capacidad: "))
            insertar_sala(nombre, capacidad)
            
        elif opcion == 2:
            consultar_salas()
            
        elif opcion == 3:
            estudiante = input("Estudiante: ")
            sala_id = int(input("ID de la sala: "))
            fecha = input("Fecha (AAAA-MM-DD): ")
            registrar_reserva(estudiante, sala_id, fecha)
            
        elif opcion == 4:
            consultar_reservas()
            
        elif opcion == 5:
            id_reserva = int(input("ID de la reserva: "))
            cancelar_reserva(id_reserva)
            
        elif opcion == 0:
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no válida")
            
        input("\nPresiona Enter para continuar...")
        
    except ValueError:
        print("Debes ingresar un número válido")
        input("\nPresiona Enter para continuar...")