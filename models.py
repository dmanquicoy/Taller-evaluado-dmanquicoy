from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Sala(Base):
    __tablename__ = "salas"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    capacidad: Mapped[int]
    disponible: Mapped[bool] = mapped_column(default=True)
    reservas: Mapped[list["Reserva"]] = relationship(back_populates="sala")


class Reserva(Base):
    __tablename__ = "reservas"
    id: Mapped[int] = mapped_column(primary_key=True)
    estudiante: Mapped[str] = mapped_column(String(100))
    sala_id: Mapped[int] = mapped_column(ForeignKey("salas.id"))
    fecha: Mapped[str] = mapped_column(String(10))
    sala: Mapped["Sala"] = relationship(back_populates="reservas")


engine = create_engine("sqlite:///reservas.db")
Base.metadata.create_all(engine)