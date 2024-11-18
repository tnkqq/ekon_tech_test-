from typing import Annotated

from fastapi import APIRouter, Depends

from db.orm import CustomerORM
from db.schemas import SCustomer, SCustomerAdd

router = APIRouter(prefix="/customers")


@router.get("", name="customers:get-customer")
async def get_customers() -> list[SCustomer]:
    customers = await CustomerORM.select_customers()
    return customers


@router.post("", name="customers:post-customer")
async def create_customer(customer: Annotated[SCustomerAdd, Depends()]):
    customer = await CustomerORM.insert_customer(customer)
    return {"id": customer}
