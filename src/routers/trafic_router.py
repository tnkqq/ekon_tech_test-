from typing import Annotated, Dict

from fastapi import APIRouter, Depends

from db.orm import TraficORM
from db.schemas import STrafic, STraficAdd, STraficSearch

router = APIRouter(prefix="/trafic")


@router.get("", name="trafic:get-trafic")
async def get_trafic(
    tr: Annotated[STraficSearch, Depends()]
) -> Dict[int, int]:
    traifc: list[STrafic] = await TraficORM.get_trafic(tr)

    users_trafic = {
        k.customer_id: sum(
            [
                _.received_trafic if _.customer_id == k.customer_id else 0
                for _ in traifc
            ]
        )
        for k in traifc
    }

    # trafic_sum = sum([_.received_trafic for _ in traifc])

    return users_trafic


@router.post("", name="trafic:post-trafic")
async def create_trafic(trafic: Annotated[STraficAdd, Depends()]) -> STrafic:
    trafic = await TraficORM.insert_trafic(trafic)
    return trafic
