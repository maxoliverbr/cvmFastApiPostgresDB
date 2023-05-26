from typing import List

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from src.models.model_cad_cia_aberta import CadCiaAberta

router = APIRouter()


@router.get("/cadciaaberta", status_code=status.HTTP_200_OK, response_model=List[CadCiaAberta])
def get_cadciaaberta():
    cia_aberta = CadCiaAberta()
    return [cia_aberta]


@router.get("/cadciaaberta/{cnpj}", status_code=status.HTTP_200_OK, response_model=CadCiaAberta)
def get_cadciaaberta_cnpj(cnpj: str):
    cia_aberta = CadCiaAberta()
    return cia_aberta
