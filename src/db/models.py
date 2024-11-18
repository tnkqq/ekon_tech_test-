from datetime import datetime
from typing import Annotated

from pydantic import BaseModel
from sqlalchemy import TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class Trafic(Base):
    __tablename__ = "trafic"
    id: Mapped[intpk]
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id", ondelete="CASCADE")
    )
    ip: Mapped[str]
    date: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    received_trafic: Mapped[int]


class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[intpk]
    name: Mapped[str]
