from datetime import datetime

from sqlalchemy import and_, insert, select

from .database import Base, async_session_factory, engine
from .models import Customer, Trafic
from .schemas import (SCustomer, SCustomerAdd, STrafic, STraficAdd,
                      STraficSearch)


class DBManeger:
    @staticmethod
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def drop_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)


class TraficORM:
    @staticmethod
    async def insert_trafic(trafic: STraficAdd):
        async with async_session_factory() as session:
            data = trafic.model_dump()
            tr = Trafic(**data)
            session.add(tr)
            await session.flush()
            await session.commit()
            return tr

    @staticmethod
    async def get_trafic(tr: STraficSearch) -> list[STrafic]:
        async with async_session_factory() as session:
            query = select(Trafic)
            if tr.ip:
                query = query.filter(Trafic.ip == tr.ip)
            if tr.customer:
                query = query.filter(Trafic.customer_id == tr.customer)
            if tr.after:
                query = query.filter(Trafic.date > tr.after)
            if tr.before:
                query = query.filter(Trafic.date < tr.before)
            res = await session.execute(query)
            trafic_models = res.scalars().all()
            return trafic_models


class CustomerORM:
    @staticmethod
    async def insert_customer(customer: SCustomerAdd):
        async with async_session_factory() as session:
            data = customer.model_dump()
            customer = Customer(**data)
            session.add(customer)
            await session.flush()
            await session.commit()
            return customer.id

    @staticmethod
    async def select_customers() -> list[SCustomer]:
        async with async_session_factory() as session:
            query = select(Customer)
            res = await session.execute(query)
            result = res.scalars().all()
            customers = [SCustomer.model_validate(_) for _ in result]
            return customers
