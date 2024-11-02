import sys
import re
from bs4 import BeautifulSoup
from loguru import logger

def parseStatement(xmlName):
    targetXmlFilePath = f"../resources/reports/{xmlName}"
    codedXmlFile = ""
    try:
        with open(targetXmlFilePath, 'r', encoding='utf-8') as f:
            codedXmlFile = '\n'.join(f.readlines())
    except:
        with open(targetXmlFilePath, 'r', encoding='euc-kr') as f:
            codedXmlFile = '\n'.join(f.readlines())
    ele = BeautifulSoup(codedXmlFile,'lxml')
    for pTag in ele.findAll('p'):
        pTag.replace_with(pTag.text)
    trLi = ele.findAll('td')
    found = []
    for i in range(len(trLi)):
        # if ('취득가액' in trLi[i].text or '공모가액' in trLi[i].text or ('모집' in trLi[i].text and '가액' in trLi[i].text)):
        if (('모집' in trLi[i].text and '가액' in trLi[i].text)):
            found.append(trLi[i+1].text)
    extracted = []
    for f in found:
        e = extract_number_with_won(f)
        if e is not None:
            extracted.append(e)
    return extracted

def extract_number_with_won(value: str):
    # 숫자와 "원"이 포함된 패턴을 매칭
    match = re.search(r'(\d+)원', value.replace(",",""))
    if match:
        return int(match.group(1))
    return None  # "원"이 포함되지 않은 경우 None 반환

if __name__ == "__main__":
    #"20230413001207.xml"
    logger.info(parseStatement(sys.argv[1]))