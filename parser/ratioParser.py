import sys
import re
from bs4 import BeautifulSoup
from loguru import logger

def parseNumber(target: str) -> float:
    try:
        return float(target.replace("%", "").strip())
    except:
        logger.error(target)
        return float(target[0:target.find('%')])

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
    for i in range(len(trLi)):
        #logger.info(trLi[i])
        if '청약' in trLi[i].text and ('증거금율' in trLi[i].text or '증거금률' in trLi[i].text) and ('%' in trLi[i].text):
            return trLi[i].text
    return "못찾음"
def parseRatioFromXml(xmlName):
    targetXmlFilePath = f"../resources/reports/{xmlName}"
    codedXmlFile = ""
    try:
        with open(targetXmlFilePath, 'r', encoding='utf-8') as f:
            codedXmlFile = '\n'.join(f.readlines())
    except:
        with open(targetXmlFilePath, 'r', encoding='euc-kr') as f:
            codedXmlFile = '\n'.join(f.readlines())
    codedXmlFile = codedXmlFile.replace("th","td").replace("TH","TD")
    ele = BeautifulSoup(codedXmlFile, 'lxml')
    for pTag in ele.findAll('p'):
        pTag.replace_with(pTag.text)
    trLi = ele.findAll('tr')
    #logger.info(trLi)
    #print(len(trLi))
    for idx in range(len(trLi)):
        curTr = trLi[idx]
        #print(curTr)
        if len(curTr.findAll('td')) == 4 and '증거금' in curTr.findAll('td')[3].text.strip():
            #logger.info(curTr.text)
            try:
                return parseNumber(trLi[idx+1].findAll('td')[3].text)
            except:
                logger.error(trLi[idx + 1].findAll('td')[3].text)

        if len(curTr.findAll('td')) == 5 and '증거금' in curTr.findAll('td')[4].text.strip():
            #logger.info(curTr.text)
            try:
                return parseNumber(trLi[idx+1].findAll('td')[4].text)
            except:
                logger.error(trLi[idx+1].findAll('td')[4].text)

    return parseStatement(xmlName)
if __name__ == "__main__":
    #"20230413001207.xml"
    logger.info(parseRatioFromXml(sys.argv[1]))