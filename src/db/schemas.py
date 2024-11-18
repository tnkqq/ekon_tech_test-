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


class STraficSearch(BaseModel):
    customer: Optional[int] = None
    ip: Optional[str] = None
    before: Optional[datetime] = None
    after: Optional[datetime] = None


class STraficAdd(BaseModel):
    customer_id: int
    ip: str
    date: Optional[datetime] = None
    received_trafic: int


class STrafic(STraficAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)
