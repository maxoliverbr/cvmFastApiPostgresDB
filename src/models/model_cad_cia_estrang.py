from pydantic import BaseModel, Field
from typing import Optional


class CadCiaEstrang(BaseModel):
    AUDITOR: Optional[str] = Field(max_length=100)
    BAIRRO: Optional[str] = Field(max_length=100)
    BAIRRO_RESP: Optional[str] = Field(max_length=100)
    CATEG_REG: Optional[str] = Field(max_length=20)
    CD_CVM: Optional[int]
    CD_PAIS_FAX: Optional[str] = Field(max_length=8)
    CD_PAIS_TEL: Optional[str] = Field(max_length=8)
    CEP: Optional[str] = Field(max_length=30)
    CEP_RESP: Optional[int]
    CIDADE: Optional[str] = Field(max_length=50)
    CNPJ: Optional[str] = Field(max_length=20)
    CNPJ_AUDITOR: Optional[str] = Field(max_length=20)
    COMPL: Optional[str] = Field(max_length=100)
    COMPL_RESP: Optional[str] = Field(max_length=100)
    CONTROLE_ACIONARIO: Optional[str] = Field(max_length=30)
    DDD_FAX: Optional[str] = Field(max_length=4)
    DDD_FAX_RESP: Optional[str] = Field(max_length=4)
    DDD_TEL: Optional[str] = Field(max_length=4)
    DDD_TEL_RESP: Optional[str] = Field(max_length=4)
    DENOM_COMERC: Optional[str] = Field(max_length=100)
    DENOM_SOCIAL: Optional[str] = Field(max_length=100)
    DT_CANCEL: Optional[str]
    DT_CONST: Optional[str]
    DT_INI_CATEG: Optional[str]
    DT_INI_RESP: Optional[str]
    DT_INI_SIT: Optional[str]
    DT_INI_SIT_EMISSOR: Optional[str]
    DT_REG: Optional[str]
    EMAIL: Optional[str] = Field(max_length=100)
    EMAIL_RESP: Optional[str] = Field(max_length=100)
    ESTADO: Optional[str] = Field(max_length=50)
    FAX: Optional[int]
    FAX_RESP: Optional[int]
    LOGRADOURO: Optional[str] = Field(max_length=100)
    LOGRADOURO_RESP: Optional[str] = Field(max_length=100)
    MOTIVO_CANCEL: Optional[str] = Field(max_length=80)
    MUN_RESP: Optional[str] = Field(max_length=100)
    PAIS: Optional[str] = Field(max_length=100)
    PAIS_ORIGEM: Optional[str] = Field(max_length=100)
    PAIS_RESP: Optional[str] = Field(max_length=100)
    RESP: Optional[str] = Field(max_length=100)
    SETOR_ATIV: Optional[str] = Field(max_length=100)
    SIT: Optional[str] = Field(max_length=40)
    SIT_EMISSOR: Optional[str] = Field(max_length=80)
    TEL: Optional[int]
    TEL_RESP: Optional[int]
    TP_ENDER: Optional[str] = Field(max_length=30)
    TP_RESP: Optional[str] = Field(max_length=100)
    UF_RESP: Optional[str] = Field(max_length=2)
