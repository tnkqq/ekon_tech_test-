from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends

from db.orm import TraficORM
from db.schemas import STrafic, STraficAdd

router = APIRouter(prefix="/trafic")


@router.get("", name="trafic:get-trafic")
async def get_trafic(
    after: datetime | None = None,
    before: datetime | None = None,
    customer: int | None = None,
    ip: str | None = None,
) -> dict:
    traifc: list[STrafic] = await TraficORM.get_trafic(
        after=after, before=before, customer=customer, ip=ip
    )

    trafic_sum = sum([_.received_trafic for _ in traifc])

    return {"trafic": trafic_sum}


@router.post("", name="trafic:post-trafic")
async def create_trafic(trafic: Annotated[STraficAdd, Depends()]) -> STrafic:
    trafic = await TraficORM.insert_trafic(trafic)
    return trafic
