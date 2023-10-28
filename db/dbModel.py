from sqlalchemy import Column, BIGINT, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CorpCode(Base):
    __tablename__ = "corpCode"
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    corpCode = Column(String(length=8 , collation='utf8mb4_general_ci'),nullable=False)
    corpName = Column(String(length=255 , collation='utf8mb4_general_ci'), nullable=False)
    stockCode = Column(String(length=6 , collation='utf8mb4_general_ci'), nullable=True)
    modifyDate = Column(Date, nullable=True)
    def __init__(self,rb: dict):
        self.corpCode = rb['corp_code']
        self.corpName = rb['corp_name']
        self.stockCode = rb['stock_code']
        self.modifyDate = rb['modify_date']

