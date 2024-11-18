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
            assert res.json().get("trafic") == exp_result
            assert res.status_code == HTTPStatus.OK

    @pytest.mark.asyncio
    async def test_trafic_by_customer(
        self, app: FastAPI, client: AsyncClient, customer_list, trafic_list
    ):
        for customer, exp_result in InitTestData.customer_trafic_data():
            res = await client.get(
                app.url_path_for("trafic:get-trafic"),
                params={"customer": customer},
            )
            assert res.json().get("trafic") == exp_result
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
            assert res.json().get("trafic") == 0
            res = await client.get(
                app.url_path_for("trafic:get-trafic"),
                params={"after": dt + datetime.timedelta(1, 1, 1)},
            )
            assert res.json().get("trafic") == sum(
                [
                    (
                        _.get("trafic", 0)
                        if _.get("date") > dt + datetime.timedelta(1, 1, 1)
                        else 0
                    )
                    for _ in InitTestData.trafic_test_data
                ]
            )
            # res = await client.get(app.url_path_for('trafic:get-trafic'), params={'before': dt+datetime.timedelta(1,1,1), 'after': sorted_datetime[0] - datetime.datetime(1, 1, 1)})
            # assert res.json().get('trafic') == sum([_.get('trafic', 0) if (_.get('date') > datetime.strptime(str(sorted_datetime[0] - datetime.datetime(1, 1, 1))) and _.get('date') < dt else 0 for _ in InitTestData.trafic_test_data])
            assert res.status_code == HTTPStatus.OK
