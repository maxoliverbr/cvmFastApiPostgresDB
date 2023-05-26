from pydantic import BaseModel, Field


class CadCiaEstrang(BaseModel):
    AUDITOR: str = Field(max_length=100)
    BAIRRO: str = Field(max_length=100)
    BAIRRO_RESP: str = Field(max_length=100)
    CATEG_REG: str = Field(max_length=20)
    CD_CVM: int
    CD_PAIS_FAX: str = Field(max_length=8)
    CD_PAIS_TEL: str = Field(max_length=8)
    CEP: str = Field(max_length=30)
    CEP_RESP: int
    CIDADE: str = Field(max_length=50)
    CNPJ: str = Field(max_length=20)
    CNPJ_AUDITOR: str = Field(max_length=20)
    COMPL: str = Field(max_length=100)
    COMPL_RESP: str = Field(max_length=100)
    CONTROLE_ACIONARIO: str = Field(max_length=30)
    DDD_FAX: str = Field(max_length=4)
    DDD_FAX_RESP: str = Field(max_length=4)
    DDD_TEL: str = Field(max_length=4)
    DDD_TEL_RESP: str = Field(max_length=4)
    DENOM_COMERC: str = Field(max_length=100)
    DENOM_SOCIAL: str = Field(max_length=100)
    DT_CANCEL: str
    DT_CONST: str
    DT_INI_CATEG: str
    DT_INI_RESP: str
    DT_INI_SIT: str
    DT_INI_SIT_EMISSOR: str
    DT_REG: str
    EMAIL: str = Field(max_length=100)
    EMAIL_RESP: str = Field(max_length=100)
    ESTADO: str = Field(max_length=50)
    FAX: int
    FAX_RESP: int
    LOGRADOURO: str = Field(max_length=100)
    LOGRADOURO_RESP: str = Field(max_length=100)
    MOTIVO_CANCEL: str = Field(max_length=80)
    MUN_RESP: str = Field(max_length=100)
    PAIS: str = Field(max_length=100)
    PAIS_ORIGEM: str = Field(max_length=100)
    PAIS_RESP: str = Field(max_length=100)
    RESP: str = Field(max_length=100)
    SETOR_ATIV: str = Field(max_length=100)
    SIT: str = Field(max_length=40)
    SIT_EMISSOR: str = Field(max_length=80)
    TEL: int
    TEL_RESP: int
    TP_ENDER: str = Field(max_length=30)
    TP_RESP: str = Field(max_length=100)
    UF_RESP: str = Field(max_length=2)
