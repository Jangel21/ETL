from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models import Cliente, Personal, Salon, Evento, Platillo

# Change this with your own url
DATABASE_URL = "postgresql://postgres:12345@localhost:5432/Servicios_Hotel"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# OPERACIONES DE 5 TABLAS

# Tabla Cliente
def Insert_Cliente():
    Id_Cliente = int(input("Ingrese el ID: "))
    Nombre = input("Ingrese el nombre:")
    Apellido = input("Ingrese el apellido:")
    Telefono = int(input("Ingrese el número de teléfono:"))
    Correo = input("Ingrese el correo electrónico: ")
    RFC = input("Ingrese el RFC: ")

    cliente = Cliente(Id_Cliente=Id_Cliente, Nombre=Nombre, Apellido=Apellido, Telefono=Telefono, Correo=Correo, RFC=RFC)
    session.add(cliente)
    session.commit()
    print("Cliente agregado correctamente :)")

def Delete_Cliente():
    id = int(input("Ingrese el ID del cliente a eliminar: "))
    cliente = session.get(Cliente, id)

    if cliente:
        session.delete(cliente)
        session.commit()
        print("Cliente Eliminado Correctamente :)")
    else:
        print("El cliente no se encontró")

def Update_Cliente():
    id = int(input("Ingrese el ID del cliente a Modificar: "))
    cliente = session.get(Cliente, id)

    if cliente:
        cliente.Nombre = input("Ingrese el nuevo nombre: ")
        cliente.Apellido = input("Ingrese el nuevo apellido: ")
        cliente.Telefono = int(input("Ingrese el nuevo número de teléfono: "))
        cliente.Correo = input("Ingrese el nuevo correo electrónico: ")
        cliente.RFC = input("Ingrese el nuevo RFC: ")
        session.commit()
        print("Cliente actualizado Correctamente :)")
    else:
        print("El cliente no se encontró")

def Get_Cliente():
    id = int(input("Ingrese el ID del cliente a Buscar: "))
    cliente = session.get(Cliente, id)

    if cliente:
        print(cliente.Id_Cliente, cliente.Nombre, cliente.Apellido, cliente.Telefono, cliente.Correo, cliente.RFC)
    else:
        print("El cliente no se encontró")

def Get_Clientes():
    clientes = session.query(Cliente).all()
    for cliente in clientes:
        print(cliente.Id_Cliente, cliente.Nombre, cliente.Apellido, cliente.Telefono, cliente.Correo, cliente.RFC)

# Tabla Personal
def Insert_Personal():
    Id_Personal = int(input("Ingrese el ID: "))
    Nombre = input("Ingrese el nombre:")
    Apellido = input("Ingrese el apellido:")
    Sueldo = int(input("Ingrese el sueldo:"))
    Rol = input("Ingrese el rol(ME, CO, CF, CM, RC, SC):")

    personal = Personal(Id_Personal=Id_Personal, Nombre=Nombre, Apellido=Apellido, Sueldo=Sueldo, Rol=Rol)
    session.add(personal)
    session.commit()
    print("Personal agregado correctamente :)")

def Delete_Personal():
    id = int(input("Ingrese el ID del personal a eliminar: "))
    personal = session.get(Personal, id)

    if personal:
        session.delete(personal)
        session.commit()
        print("Personal Eliminado Correctamente :)")
    else:
        print("El personal no se encontró")

def Update_Personal():
    id = int(input("Ingrese el ID del personal a Modificar: "))
    personal = session.get(Personal, id)

    if personal:
        personal.Nombre = input("Ingrese el nuevo nombre: ")
        personal.Apellido = input("Ingrese el nuevo apellido: ")
        personal.Sueldo = int(input("Ingrese el nuevo sueldo: "))
        personal.Rol = input("Ingrese el nuevo rol(ME, CO, CF, CM, RC, SC): ")
        session.commit()
        print("Personal actualizado Correctamente :)")
    else:
        print("El personal no se encontró")

def Get_Personal():
    id = int(input("Ingrese el ID del personal a Buscar: "))
    personal = session.get(Personal, id)

    if personal:
        print(personal.Id_Personal, personal.Nombre, personal.Apellido, personal.Sueldo, personal.Rol)
    else:
        print("El personal no se encontró")

def Get_Personales():
    personales = session.query(Personal).all()
    for personal in personales:
        print(personal.Id_Personal, personal.Nombre, personal.Apellido, personal.Sueldo, personal.Rol)

#Tabla Salon
def Insert_Salon():
    Id_Salon = int(input("Ingrese el ID: "))
    Nombre = input("Ingrese el nombre:")
    Disponibilidad_input = input("Esta disponible? (si/no): ")
    Disponibilidad = Disponibilidad_input in ["si", "sí"]

    Capacidad = int(input("Ingrese la capacidad máxima de personas:"))
    Ubicacion = input("Ingrese la ubicacion:")

    salon = Salon(Id_Salon=Id_Salon, Nombre=Nombre, Disponibilidad=Disponibilidad, Capacidad=Capacidad, Ubicacion=Ubicacion)
    session.add(salon)
    session.commit()
    print("Salon agregado correctamente :)")

def Delete_Salon():
    id = int(input("Ingrese el ID del salon a eliminar: "))
    salon = session.get(Salon, id)

    if salon:
        session.delete(salon)
        session.commit()
        print("Salon Eliminado Correctamente :)")
    else:
        print("El salon no se encontró")

def Update_Salon():
    id = int(input("Ingrese el ID del salon a Modificar: "))
    salon = session.get(Salon, id)

    if salon:
        salon.Nombre = input("Ingrese el nuevo nombre: ")
        Disponibilidad_input = input("Esta disponible? (si/no): ")
        salon.Disponibilidad = Disponibilidad_input in ["si", "sí"]

        salon.Capacidad = int(input("Ingrese la nueva capacidad máxima de personas: "))
        salon.Ubicacion = input("Ingrese la nueva ubicacion: ")
        session.commit()
        print("Salon actualizado Correctamente :)")
    else:
        print("El salon no se encontró")

def Get_Salon():
    id = int(input("Ingrese el ID del salon a Buscar: "))
    salon = session.get(Salon, id)

    if salon:
        print(salon.Id_Salon, salon.Nombre, salon.Disponibilidad, salon.Capacidad, salon.Ubicacion)
    else:
        print("El salon no se encontró")

def Get_Salones():
    salones = session.query(Salon).all()
    for salon in salones:
        print(salon.Id_Salon, salon.Nombre, salon.Disponibilidad, salon.Capacidad, salon.Ubicacion)

#Tabla Evento
def Insert_Evento():
    Id_Evento = int(input("Ingrese el ID: "))

    Fecha = input("Ingrese la fecha (YYYY-MM-DD HH:MM:SS): ") 
    try:
        Fecha = datetime.strptime(Fecha, "%Y-%m-%d %H:%M:%S") 
    except ValueError:
        print("Formato de fecha incorrecto. Usa: YYYY-MM-DD HH:MM:SS")
        return
    
    Nombre = input("Ingrese el nombre:")
    Descripcion = input("Ingrese la descripcion:")
    Num_Invitados = int(input("Ingrese el numero de invitados:"))
    Id_Cliente_Fk = int(input("Ingrese el id del cliente:"))
    Id_Salon_Fk = int(input("Ingrese el id del salon:"))
    Categoria = input("Ingrese la categoria(CO, BD, RC, CP, CA, EX):")
    Duracion = int(input("Ingrese la duracion del evento(horas):"))
    

    evento = Evento(Id_Evento=Id_Evento, Fecha=Fecha, Nombre=Nombre, Descripcion=Descripcion, Num_Invitados=Num_Invitados, Id_Cliente_Fk=Id_Cliente_Fk, 
                  Id_Salon_Fk=Id_Salon_Fk,Categoria=Categoria, Duracion=Duracion)
    session.add(evento)
    session.commit()
    print("Salon agregado correctamente :)")   

def Delete_Evento():
    id = int(input("Ingrese el ID del evento a eliminar: "))
    evento = session.get(Evento, id)

    if evento:
        session.delete(evento)
        session.commit()
        print("Evento Eliminado Correctamente :)")
    else:
        print("El evento no se encontró")     

def Update_Evento():
    id = int(input("Ingrese el ID del evento a Modificar: "))
    evento = session.get(Evento, id)

    if evento:
        Fecha = input("Ingrese la nueva fecha (YYYY-MM-DD HH:MM:SS): ") 
        try:
            evento.Fecha = datetime.strptime(Fecha, "%Y-%m-%d %H:%M:%S") 
        except ValueError:
            print("Formato de fecha incorrecto. Usa: YYYY-MM-DD HH:MM:SS")
            return

        evento.Nombre = input("Ingrese el nuevo nombre: ")
        evento.Descripcion = input("Ingrese la nueva descripcion: ")
        evento.Num_Invitados = int(input("Ingrese el nuevo numero de invitados: "))
        evento.Id_Cliente_Fk = int(input("Ingrese el nuevo id del cliente:"))
        evento.Id_Salon_Fk = int(input("Ingrese el nuevo id del salon:"))
        evento.Categoria = input("Ingrese la nueva categoria(CO, BD, RC, CP, CA, EX):")
        evento.Duracion = int(input("Ingrese la nueva duracion del evento(horas):"))
        
        session.commit()
        print("Evento actualizado Correctamente :)")
    else:
        print("El Evento no se encontró")

def Get_Evento():
    id = int(input("Ingrese el ID del evento a Buscar: "))
    evento = session.get(Evento, id)

    if evento:
        print(evento.Id_Evento, evento.Fecha, evento.Nombre, evento.Descripcion, evento.Num_Invitados, evento.Id_Cliente_Fk, evento.Id_Salon_Fk, 
              evento.Categoria, evento.Duracion)
    else:
        print("El evento no se encontró")

def Get_Eventos():
    eventos = session.query(Evento).all()
    for evento in eventos:
        print(evento.Id_Evento, evento.Fecha, evento.Nombre, evento.Descripcion, evento.Num_Invitados, evento.Id_Cliente_Fk, evento.Id_Salon_Fk, 
              evento.Categoria, evento.Duracion)

#Tabla Platillo
def Insert_Platillo():
    Id_Platillo = int(input("Ingrese el ID: "))
    Nombre = input("Ingrese el nombre:")
    Descripcion = input("Ingrese la Descripcion:")
    Precio = int(input("Ingrese el precio:"))
    Tipo = input("Ingrese el tipo(BE, CM, PS, SK): ")

    platillo = Platillo(Id_Platillo=Id_Platillo, Nombre=Nombre, Descripcion=Descripcion, Precio=Precio, Tipo=Tipo)
    session.add(platillo)
    session.commit()
    print("Platillo agregado correctamente :)")

def Delete_Platillo():
    id = int(input("Ingrese el ID del platillo a eliminar: "))
    platillo = session.get(Platillo, id)

    if platillo:
        session.delete(platillo)
        session.commit()
        print("Platillo Eliminado Correctamente :)")
    else:
        print("El platillo no se encontró")

def Update_Platillo():
    id = int(input("Ingrese el ID del Platillo a Modificar: "))
    platillo = session.get(Platillo, id)

    if platillo:
        platillo.Nombre = input("Ingrese el nuevo nombre: ")
        platillo.Descripcion = input("Ingrese la nueva descripcion: ")
        platillo.TPrecio = int(input("Ingrese el nuevo precio: "))
        platillo.Tipo = input("Ingrese el nuevo tipo(BE, CM, PS, SK): ")
        session.commit()
        print("Platillo actualizado Correctamente :)")
    else:
        print("El platillo no se encontró")

def Get_Platillo():
    id = int(input("Ingrese el ID del platillo a Buscar: "))
    platillo = session.get(Platillo, id)

    if platillo:
        print(platillo.Id_Platillo, platillo.Nombre, platillo.Descripcion, platillo.Precio, platillo.Tipo)
    else:
        print("El platillo no se encontró")

def Get_Platillos():
    platillos = session.query(Platillo).all()
    for platillo in platillos:
        print(platillo.Id_Platillo, platillo.Nombre, platillo.Descripcion, platillo.Precio, platillo.Tipo)