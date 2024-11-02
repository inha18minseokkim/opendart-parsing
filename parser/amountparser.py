import sys
import re
from bs4 import BeautifulSoup
from loguru import logger
def parseAmountFromXml(xmlName):
    targetXmlFilePath = f"../resources/reports/{xmlName}"
    codedXmlFile = ""
    try:
        with open(targetXmlFilePath, 'r', encoding='utf-8') as f:
            codedXmlFile = '\n'.join(f.readlines())
    except:
        with open(targetXmlFilePath, 'r', encoding='euc-kr') as f:
            codedXmlFile = '\n'.join(f.readlines())
    codedXmlFile = codedXmlFile.replace("TH","TD").replace("th","td")
    ele = BeautifulSoup(codedXmlFile,'lxml')
    for pTag in ele.findAll('p'):
        pTag.replace_with(pTag.text)


    trLi = ele.findAll('tr')
    flag = False
    resArr = []
    for idx in range(len(trLi)):
        curTr = trLi[idx]

        if len(curTr.findAll('td')) != 0 \
                and (curTr.findAll('td')[0].text.strip() == '청약주식수' or curTr.findAll('td')[0].text.strip() == '청약증권수' or curTr.findAll('td')[0].text.strip() == '구분')\
                and ('단위' in curTr.findAll('td')[1].text.strip() and '청약' in curTr.findAll('td')[1].text.strip()):
            try:
                tmpArr = []
                tmpArr.append(f'{ele.find("title").text:20}')
                first = trLi[idx + 1].findAll('td')[0].text.strip().replace('\n', ' ').replace(' ','')
                tmpArr.append(f'{first:30}')
                second = trLi[idx + 1].findAll('td')[1].text.strip().replace('\n', ' ').replace(' ','')
                tmpArr.append(f'{second:30}')
                # return tmpArr
            except:
                logger.error(xmlName +" 오류")
            resArr += tmpArr
    resArr.append(f'{ele.find("title").text:20}')
    resAmount = []
    for r in resArr:
        logger.info(r)
        amount = parse_amount(r.strip())
        if amount is not None:
            resAmount.append(amount)
    return resAmount

def parse_amount(value):
    # 숫자와 "주" 패턴을 매칭하고 숫자만 추출
    match = re.search(r'(\d+)주', value)
    if match:
        return int(match.group(1))
    return None  # "주"가 포함되지 않은 경우 None 반환

if __name__ == "__main__":
    #"20230413001207.xml"
    logger.info(min(parseAmountFromXml(sys.argv[1])))