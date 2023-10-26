import xml.etree.ElementTree as elemTree
import re
from bs4 import BeautifulSoup
from loguru import logger
import os


def parseNumberFromStatement(text: str)-> float:
    # 미래에셋대우㈜의 일반청약자 청약증거금율은 50%입니다
    pattern = r'(\d+)%'

    # Using re.search to find the pattern in the text
    match = re.search(pattern, text)

    # Extracting the percentage value if a match is found
    if match:
        percentage_value = float(match.group(1))
        #print(text, percentage_value)
        return percentage_value  # Output: 50
    else:
        raise Exception("최후의 변환 실패")

def parseNumber(target: str) -> float:
    try:
        return float(target.replace("%", "").strip())
    except:
        logger.error(target)
        return float(target[0:target.find('%')])

def parseStatement(xmlName):
    targetXmlFilePath = f"./resources/reports/{xmlName}"
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
    targetXmlFilePath = f"./resources/reports/{xmlName}"
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
                # return parseStatement(xmlName)
            # return float(trLi[idx+1].findAll('td')[3].text.replace("%","").strip())

        if len(curTr.findAll('td')) == 5 and '증거금' in curTr.findAll('td')[4].text.strip():
            #logger.info(curTr.text)
            try:
                return parseNumber(trLi[idx+1].findAll('td')[4].text)
            except:
                logger.error(trLi[idx+1].findAll('td')[4].text)
                #return parseStatement(xmlName)
            # return float(trLi[idx + 1].findAll('td')[4].text.replace("%","").strip())
    return parseStatement(xmlName)
