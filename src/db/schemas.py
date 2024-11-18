from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from .models import Trafic


class SCustomerAdd(BaseModel):
    name: str


class SCustomer(SCustomerAdd):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class STraficAdd(BaseModel):
    customer_id: int
    ip: str
    date: Optional[datetime] = None
    received_trafic: Optional[int] = None


class STrafic(STraficAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)
