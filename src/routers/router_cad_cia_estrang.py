from typing import List

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from src.models.model_cad_cia_estrang import CadCiaEstrang

router = APIRouter()


@router.get("/cadciaestrang", status_code=status.HTTP_200_OK, response_model=List[CadCiaEstrang])
def get_cadciaaberta():
    cia_estrang = CadCiaEstrang()
    return [cia_estrang]


@router.get("/cadciaestrang/{cnpj}", status_code=status.HTTP_200_OK, response_model=CadCiaEstrang)
def get_cadciaaberta_cnpj(cnpj: str):
    cia_estrang = CadCiaEstrang()
    return cia_estrang
