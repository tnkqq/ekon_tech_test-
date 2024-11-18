import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient


@pytest_asyncio.fixture(scope="function")
async def db():
    from src.db.orm import DBManeger

    await DBManeger.create_tables()
    yield
    await DBManeger.drop_tables()


@pytest.fixture(scope="module")
def app():
    from src.app import app

    return app


@pytest_asyncio.fixture
async def client(app: FastAPI, db):
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client


@pytest_asyncio.fixture()
async def customer_list(client, app):
    from .data import InitTestData

    for customer in InitTestData.customer_test_data.values():
        await client.post(
            app.url_path_for("customers:post-customer"), params=customer
        )


@pytest_asyncio.fixture(scope="function")
async def trafic_list(client, app):
    from .data import InitTestData

    for trafic in InitTestData.trafic_test_data:
        await client.post(
            app.url_path_for("trafic:post-trafic"), params=trafic
        )
