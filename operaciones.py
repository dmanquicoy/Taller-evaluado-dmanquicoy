from sqlalchemy import select
from sqlalchemy.orm import Session
from models import engine, Sala, Reserva


def insertar_sala(nombre, capacidad):
    if nombre.strip() == "":
        print("El nombre no puede estar vacío")
        return
    if capacidad <= 0:
        print("La capacidad debe ser mayor que cero")
        return
        
    with Session(engine) as session:
        sala = Sala(nombre=nombre, capacidad=capacidad)
        session.add(sala)
        session.commit() 
    print("Sala registrada")


def consultar_salas():
    with Session(engine) as session:
        salas = session.scalars(select(Sala)).all()
        if not salas:
            print("No hay salas registradas.")
            return
        for s in salas:
            estado = "Disponible" if s.disponible else "No disponible"
            print(f"{s.id} - {s.nombre} - Capacidad: {s.capacidad} - {estado}")


def registrar_reserva(estudiante, sala_id, fecha):
    with Session(engine) as session:
        sala = session.get(Sala, sala_id)
        if sala is None:
            print("La sala no existe")
            return
        if not sala.disponible:
            print("La sala no está disponible")
            return
            
        reserva = Reserva(estudiante=estudiante, sala_id=sala_id, fecha=fecha)
        session.add(reserva)
        sala.disponible = False
        session.commit()
    print("Reserva registrada")


def consultar_reservas():
    with Session(engine) as session:
        reservas = session.scalars(select(Reserva)).all()
        if not reservas:
            print("No hay reservas registradas.")
            return
        for r in reservas:
            print(f"{r.id} - Estudiante: {r.estudiante} - Sala: {r.sala.nombre} - Fecha: {r.fecha}")


def cancelar_reserva(id_reserva):
    with Session(engine) as session:
        reserva = session.get(Reserva, id_reserva)
        if reserva is None:
            print("La reserva no existe")
            return
        reserva.sala.disponible = True
        session.delete(reserva)
        session.commit()
    print("Reserva cancelada")