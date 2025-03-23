# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Enum, ForeignKey, Integer, Numeric, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Cliente(Base):
    __tablename__ = 'Cliente'

    Id_Cliente = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Cliente_Id_Cliente_seq\"'::regclass)"))
    Nombre = Column(String(25))
    Apellido = Column(String(30))
    Telefono = Column(String(15))
    Correo = Column(String(35))
    RFC = Column(String(14))


class Festividade(Base):
    __tablename__ = 'Festividades'

    Id_Festividad = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Festividades_Id_Festividad_seq\"'::regclass)"))
    Día = Column(DateTime)
    Nombre = Column(String(20))


class Inmobiliario(Base):
    __tablename__ = 'Inmobiliario'

    Id_Inmobiliario = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Inmobiliario_Id_Inmobiliario_seq\"'::regclass)"))
    Nombre = Column(String(20))
    Cantidad = Column(Integer)
    Disponible = Column(Integer)


class Moneda(Base):
    __tablename__ = 'Moneda'

    Id_Moneda = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Moneda_Id_Moneda_seq\"'::regclass)"))
    Codigo = Column(String(5))
    Tasa_Cambio = Column(Numeric(5, 2))


class Personal(Base):
    __tablename__ = 'Personal'

    Id_Personal = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Personal_Id_Personal_seq\"'::regclass)"))
    Nombre = Column(String(25))
    Apellido = Column(String(30))
    Sueldo = Column(Numeric(8, 2))
    Rol = Column(Enum('ME', 'CO', 'CF', 'CM', 'RC', 'SC', name='Rol'))


class Platillo(Base):
    __tablename__ = 'Platillo'

    Id_Platillo = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Platillo_Id_Platillo_seq\"'::regclass)"))
    Nombre = Column(String(25))
    Descripcion = Column(String(72))
    Precio = Column(Numeric(5, 2))
    Tipo = Column(Enum('BE', 'CM', 'PS', 'SK', name='PlatilloT'))


class ReporteMensual(Base):
    __tablename__ = 'Reporte_Mensual'

    Id_Reporte = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Reporte_Mensual_Id_Reporte_seq\"'::regclass)"))
    Total_Eventos = Column(Integer)
    Total_Ganancia = Column(Numeric(12, 2))
    Total_Invitados = Column(Integer)
    Mes = Column(Date)


class Salon(Base):
    __tablename__ = 'Salon'

    Id_Salon = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Salon_Id_Salon_seq\"'::regclass)"))
    Nombre = Column(String(30))
    Disponibilidad = Column(Boolean)
    Capacidad = Column(Integer)
    Ubicacion = Column(String(30))


t_evento_reservacion = Table(
    'evento_reservacion', metadata,
    Column('Id_Evento', Integer),
    Column('Fecha_Evento', DateTime),
    Column('Duracion', Integer),
    Column('Id_Salon', Integer)
)


t_horas_trabajadas_por_empleado = Table(
    'horas_trabajadas_por_empleado', metadata,
    Column('Id_Evento_Fk', Integer),
    Column('Id_Personal_Fk', Integer),
    Column('Nombre', String(25)),
    Column('Apellido', String(30)),
    Column('total_horas_trabajadas', Numeric)
)


t_vista_sueldo = Table(
    'vista_sueldo', metadata,
    Column('Id_Evento_Fk', Integer),
    Column('Id_Personal', Integer),
    Column('Nombre', String(25)),
    Column('Apellido', String(30)),
    Column('horas_trabajadas', Numeric),
    Column('sueldo_total', Numeric)
)


class Evento(Base):
    __tablename__ = 'Evento'

    Id_Evento = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Evento_Id_Evento_seq\"'::regclass)"))
    Fecha = Column(DateTime)
    Nombre = Column(String(30))
    Descripcion = Column(String(72))
    Num_Invitados = Column(Integer)
    Id_Cliente_Fk = Column(ForeignKey(
        'Cliente.Id_Cliente', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    Id_Salon_Fk = Column(ForeignKey(
        'Salon.Id_Salon', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    Categoria = Column(Enum('CO', 'BD', 'RC', 'CP',
                       'CA', 'EX', name='EventoT'))
    Duracion = Column(Integer)

    Cliente = relationship('Cliente')
    Salon = relationship('Salon')


class CambioRol(Base):
    __tablename__ = 'Cambio_Rol'

    Id_Cambio = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Cambio_Rol_Id_Cambio_seq\"'::regclass)"))
    Hora_Inicio = Column(DateTime)
    Hora_Final = Column(DateTime)
    Id_Personal_Fk = Column(ForeignKey(
        'Personal.Id_Personal', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    Id_Evento_Fk = Column(ForeignKey(
        'Evento.Id_Evento', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    Rol = Column(Enum('ME', 'CO', 'CF', 'CM', 'RC', 'SC', name='Rol'))

    Evento = relationship('Evento')
    Personal = relationship('Personal')


class Extra(Base):
    __tablename__ = 'Extra'

    Id_Extra = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Extra_Id_Extra_seq\"'::regclass)"))
    Nombre = Column(String(20))
    Descripcion = Column(String(50))
    Precio = Column(Numeric(10, 2))
    Id_Evento_Fk = Column(ForeignKey(
        'Evento.Id_Evento', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    Tipo = Column(Enum('MV', 'CG', 'DT', 'ET', 'OR', name='ExtraT'))

    Evento = relationship('Evento')


class Modificacion(Base):
    __tablename__ = 'Modificacion'

    Id_Modificacion = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Modificacion_Id_Modificacion_seq\"'::regclass)"))
    Fecha = Column(DateTime)
    Nombre = Column(String(30))
    Descripcion = Column(String(72))
    Categoria = Column(String(20))
    Num_Invitados = Column(Integer)
    Fecha_Modificacion = Column(DateTime)
    Id_Evento_Fk = Column(ForeignKey(
        'Evento.Id_Evento', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    Evento = relationship('Evento')


class Reservacion(Base):
    __tablename__ = 'Reservacion'

    Id_Reservacion = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Reservacion_Id_Reservacion_seq\"'::regclass)"))
    Fecha_Solicitud = Column(DateTime)
    Fecha_Evento = Column(DateTime)
    Fecha_Cancelacion = Column(DateTime)
    Id_Evento_Fk = Column(ForeignKey(
        'Evento.Id_Evento', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    Evento = relationship('Evento')


class ServicioComida(Base):
    __tablename__ = 'Servicio_Comida'

    Id_Servicio = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Servicio_Comida_Id_Servicio_seq\"'::regclass)"))
    Cantidad = Column(Integer)
    Id_Evento_Fk = Column(ForeignKey(
        'Evento.Id_Evento', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    Id_Platillo_Fk = Column(ForeignKey(
        'Platillo.Id_Platillo', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    Evento = relationship('Evento')
    Platillo = relationship('Platillo')


class ServicioInmobiliario(Base):
    __tablename__ = 'Servicio_Inmobiliario'

    Id_Servicio = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Servicio_Inmobiliario_Id_Servicio_seq\"'::regclass)"))
    Cantidad = Column(Integer)
    Id_Evento_Fk = Column(ForeignKey(
        'Evento.Id_Evento', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    Id_Inmobiliario_Fk = Column(ForeignKey(
        'Inmobiliario.Id_Inmobiliario', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    Evento = relationship('Evento')
    Inmobiliario = relationship('Inmobiliario')


class Factura(Base):
    __tablename__ = 'Factura'

    Id_Factura = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Factura_Id_Factura_seq\"'::regclass)"))
    Total_Pagar = Column(Numeric(10, 2))
    Fecha = Column(DateTime)
    Descuento = Column(Numeric(10, 2))
    Id_Cliente_Fk = Column(ForeignKey(
        'Cliente.Id_Cliente', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Id_Reservacion_Fk = Column(ForeignKey('Reservacion.Id_Reservacion',
                               ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Id_Moneda_Fk = Column(ForeignKey(
        'Moneda.Id_Moneda', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Total_Pagar_Descuento = Column(Numeric(10, 2))

    Cliente = relationship('Cliente')
    Moneda = relationship('Moneda')
    Reservacion = relationship('Reservacion')


class FacturaPersonal(Base):
    __tablename__ = 'Factura_Personal'

    Id_FacturaPersonal = Column(Integer, primary_key=True, server_default=text(
        "nextval('\"Factura_Personal_Id_FacturaPersonal_seq\"'::regclass)"))
    Horas_Trabajadas = Column(Numeric(5, 2))
    Sueldo_Total = Column(Numeric(8, 2))
    Id_Factura_Fk = Column(ForeignKey(
        'Factura.Id_Factura', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    Id_Personal_Fk = Column(ForeignKey(
        'Personal.Id_Personal', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    Factura = relationship('Factura')
    Personal = relationship('Personal')