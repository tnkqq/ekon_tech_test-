from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.orm import DBManeger
from routers.customers_router import router as customer_router
from routers.trafic_router import router as trafic_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await DBManeger.create_tables()
    yield


def get_application():
    app = FastAPI(lifespan=lifespan)
    app.include_router(trafic_router)
    app.include_router(customer_router)
    return app


app = get_application()
