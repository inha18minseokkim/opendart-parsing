import xml.etree.ElementTree as elemTree
import re
from bs4 import BeautifulSoup
from loguru import logger
import os

def parseAmountNumberfromString(text):
    # 10주 << 이거 파싱할거
    pattern = r'(\d+)'

    # Using re.search to find the pattern in the text
    match = re.search(pattern, text)

    # Extracting the percentage value if a match is found
    if match:
        amountValue = int(match.group(1))
        #print(text, amountValue)
        return amountValue  # Output: 50
    else:
        raise Exception("주식수량 변환 실패")
def parseAmountFromXml(xmlName):
    targetXmlFilePath = f"./reports/{xmlName}"
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
    # for spanTag in ele.findAll('span'):
    #     spanTag.replace_with(spanTag.text)

    trLi = ele.findAll('tr')
    flag = False
    resArr = []
    for idx in range(len(trLi)):
        curTr = trLi[idx]

        # if len(curTr.findAll('th')) != 0 \
        #         and (curTr.findAll('th')[0].text.strip() == '청약주식수' or curTr.findAll('th')[0].text.strip() == '청약증권수' )\
        #         and curTr.findAll('th')[1].text.strip() == '청약단위':
        #     try:
        #         tmpArr = []
        #         tmpArr.append(f'{ele.find("title").text:20}')
        #         first = trLi[idx + 1].findAll('td')[0].text.strip().replace('\n', ' ').replace(' ','')
        #         tmpArr.append(f'{first:30}')
        #         second = trLi[idx+1].findAll('td')[1].text.strip().replace('\n',' ').replace(' ','')
        #         tmpArr.append(f'{second:30}')
        #         return tmpArr
        #     except:
        #         logger.error(xmlName + " 오류")

        if len(curTr.findAll('td')) != 0 and (curTr.findAll('td')[0].text.strip() == '청약주식수' or curTr.findAll('td')[0].text.strip() == '청약증권수')\
                and curTr.findAll('td')[1].text.strip() == '청약단위':
            try:
                tmpArr = []
                tmpArr.append(f'{ele.find("title").text:20}')
                first = trLi[idx + 1].findAll('td')[0].text.strip().replace('\n', ' ').replace(' ','')
                tmpArr.append(f'{first:30}')
                second = trLi[idx + 1].findAll('td')[1].text.strip().replace('\n', ' ').replace(' ','')
                tmpArr.append(f'{second:30}')
                return tmpArr
            except:
                logger.error(xmlName +" 오류")

    resArr.append(f'{ele.find("title").text:20}')
    return resArr