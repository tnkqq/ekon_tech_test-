import datetime
from http import HTTPStatus

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from .data import InitTestData


class TestTrafic:
    @pytest.mark.asyncio
    async def test_trafic_route_exist(self, app: FastAPI, client: AsyncClient):
        res = await client.get(app.url_path_for("trafic:get-trafic"))
        assert res.status_code == HTTPStatus.OK

    @pytest.mark.asyncio
    async def test_trafic_by_ip(
        self, app: FastAPI, client: AsyncClient, customer_list, trafic_list
    ):
        for ip, exp_result in InitTestData.ip_trafic_data():
            res = await client.get(
                app.url_path_for("trafic:get-trafic"), params={"ip": ip}
            )
            assert sum(res.json().values()) == exp_result
            assert res.status_code == HTTPStatus.OK

    @pytest.mark.asyncio
    async def test_trafic_by_customer(
        self, app: FastAPI, client: AsyncClient, customer_list, trafic_list
    ):
        for customer in InitTestData.customer_test_data.keys():
            res = await client.get(
                app.url_path_for("trafic:get-trafic"),
                params={"customer": customer},
            )
            for x in res.json().keys():
                assert int(x) == customer
                assert res.status_code == HTTPStatus.OK

    @pytest.mark.asyncio
    async def test_trafic_by_timedelta(
        self, app: FastAPI, client: AsyncClient
    ):
        sorted_datetime = InitTestData.sorted_trafics_datetime()
        for index, dt in enumerate(sorted_datetime):
            res = await client.get(
                app.url_path_for("trafic:get-trafic"), params={"before": dt}
            )
            assert len(res.json().values()) == 0
            res = await client.get(
                app.url_path_for("trafic:get-trafic"),
                params={"after": dt + datetime.timedelta(1, 1, 1)},
            )
            assert sum(res.json().values()) == sum(
                [
                    (
                        _.get("trafic", 0)
                        if _.get("date") > dt + datetime.timedelta(1, 1, 1)
                        else 0
                    )
                    for _ in InitTestData.trafic_test_data
                ]
            )
            assert res.status_code == HTTPStatus.OK
