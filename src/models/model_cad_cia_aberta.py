from pydantic import BaseModel, Field
from typing import Optional


class CadCiaAberta(BaseModel):
    AUDITOR: Optional[str] = Field(min_length=0, max_length=100)
    BAIRRO: Optional[str]
    BAIRRO_RESP: Optional[str]
    CATEG_REG: Optional[str]
    CD_CVM: int
    CEP: Optional[int]
    CEP_RESP: Optional[int]
    CNPJ_AUDITOR: Optional[str]
    CNPJ_CIA: str
    COMPL: Optional[str]
    COMPL_RESP: Optional[str]
    CONTROLE_ACIONARIO: Optional[str]
    DDD_FAX: Optional[str]
    DDD_FAX_RESP: Optional[str]
    DDD_TEL: Optional[str]
    DDD_TEL_RESP: Optional[str]
    DENOM_COMERC: str
    DENOM_SOCIAL: Optional[str]
    DT_CANCEL: Optional[str]
    DT_CONST: Optional[str]
    DT_INI_CATEG: Optional[str]
    DT_INI_RESP: Optional[str]
    DT_INI_SIT: Optional[str]
    DT_INI_SIT_EMISSOR: Optional[str]
    DT_REG: Optional[str]
    EMAIL: Optional[str]
    EMAIL_RESP: Optional[str]
    FAX: Optional[int]
    FAX_RESP: Optional[int]
    LOGRADOURO: Optional[str]
    LOGRADOURO_RESP: Optional[str]
    MOTIVO_CANCEL: Optional[str]
    MUN: Optional[str]
    MUN_RESP: Optional[str]
    PAIS: Optional[str]
    PAIS_RESP: Optional[str]
    RESP: Optional[str]
    SETOR_ATIV: Optional[str]
    SIT: Optional[str]
    SIT_EMISSOR: Optional[str]
    TEL: Optional[int]
    TEL_RESP: Optional[int]
    TP_ENDER: Optional[str]
    TP_MERC: Optional[str]
    TP_RESP: Optional[str]
    UF: Optional[str]
    UF_RESP: Optional[str]
