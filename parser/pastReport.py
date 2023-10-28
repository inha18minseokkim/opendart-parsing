from db.dbClient import getCorpCodeByCorpName
from loguru import logger
from datetime import datetime, timedelta
from db.declaration import crtfc_key
import requests

ENDPOINT = "https://opendart.fss.or.kr/api/estkRs.json"
def loadPastReportReceptNumber(corpName: str,dmdFrcsStartDt: str):
    targetCorpCode = getCorpCodeByCorpName(corpName)[0].corpCode
    logger.debug(f"{corpName} 의 기업코드 : {targetCorpCode}")

    beginDate = (datetime.strptime(dmdFrcsStartDt,"%Y%m%d")-timedelta(days=365)).strftime("%Y%m%d")
    endDate = datetime.now().strftime("%Y%m%d")
    logger.debug(f"해당 기업의 수요예측시작일자 - 1년 전일 기준으로 리포트 목록 조회 시작 : {beginDate} ~ {endDate}")
    requestParam = {
        "crtfc_key": crtfc_key,
        "corp_code" : targetCorpCode,
        "bgn_de" : beginDate,
        "end_de" : endDate
    }
    response = requests.get(ENDPOINT,params=requestParam)
    if response.status_code == 200 and response.json()['status'] == '000':
        responseData = response.json()
        logger.debug(responseData)
        return responseData['group'][0]['list'][0]['rcept_no']
    else:
        logger.error(f"{corpName}에 대한 정보 가져오기 실패")
        return ""


if __name__ == "__main__":
    logger.debug(loadPastReportReceptNumber("에이치케이이노엔","20210722"))