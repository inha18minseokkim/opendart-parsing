from models import CorpCode
from loguru import logger
from dbConnect import conn

def saveDB(tb: CorpCode):
    session = conn.sessionmaker()
    try:
        session.merge(tb)
        session.commit()
    except Exception as e:
        logger.debug("삽입 중 오류 {e}", e=e, exc_info=True)
        session.rollback()
        session.close()
        return {'code': 1}
    logger.debug("삽입완료")