from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CadCiaEstrang(Base):
    __tablename__ = 'cia_estrang_cad'

    id = Column(Integer, primary_key=True)
    AUDITOR = Column(String(100))
    BAIRRO = Column(String(100))
    BAIRRO_RESP = Column(String(100))
    CATEG_REG = Column(String(20))
    CD_CVM = Column(Integer)
    CD_PAIS_FAX = Column(String(8))
    CD_PAIS_TEL = Column(String(8))
    CEP = Column(String(30))
    CEP_RESP = Column(Integer)
    CIDADE = Column(String(50))
    CNPJ = Column(String(20))
    CNPJ_AUDITOR = Column(String(20))
    COMPL = Column(String(100))
    COMPL_RESP = Column(String(100))
    CONTROLE_ACIONARIO = Column(String(30))
    DDD_FAX = Column(String(4))
    DDD_FAX_RESP = Column(String(4))
    DDD_TEL = Column(String(4))
    DDD_TEL_RESP = Column(String(4))
    DENOM_COMERC = Column(String(100))
    DENOM_SOCIAL = Column(String(100))
    DT_CANCEL = Column(Date)
    DT_CONST = Column(Date)
    DT_INI_CATEG = Column(Date)
    DT_INI_RESP = Column(Date)
    DT_INI_SIT = Column(Date)
    DT_INI_SIT_EMISSOR = Column(Date)
    DT_REG = Column(Date)
    EMAIL = Column(String(100))
    EMAIL_RESP = Column(String(100))
    ESTADO = Column(String(50))
    FAX = Column(Numeric(15, 0))
    FAX_RESP = Column(Numeric(15, 0))
    LOGRADOURO = Column(String(100))
    LOGRADOURO_RESP = Column(String(100))
    MOTIVO_CANCEL = Column(String(80))
    MUN_RESP = Column(String(100))
    PAIS = Column(String(100))
    PAIS_ORIGEM = Column(String(100))
    PAIS_RESP = Column(String(100))
    RESP = Column(String(100))
    SETOR_ATIV = Column(String(100))
    SIT = Column(String(40))
    SIT_EMISSOR = Column(String(80))
    TEL = Column(Numeric(15, 0))
    TEL_RESP = Column(Numeric(15, 0))
    TP_ENDER = Column(String(30))
    TP_RESP = Column(String(100))
    UF_RESP = Column(String(2))
