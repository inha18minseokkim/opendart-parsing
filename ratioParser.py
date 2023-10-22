import xml.etree.ElementTree as elemTree
import re
from bs4 import BeautifulSoup
from loguru import logger
import os

def parseRatioFromXml(xmlName):
    targetXmlFilePath = f"./reports/{xmlName}"
    codedXmlFile = ""
    try:
        with open(targetXmlFilePath, 'r', encoding='utf-8') as f:
            codedXmlFile = '\n'.join(f.readlines())
    except:
        with open(targetXmlFilePath, 'r', encoding='euc-kr') as f:
            codedXmlFile = '\n'.join(f.readlines())
    #codedXmlFile = codedXmlFile.replace("th","td").replace("TH","TD")
    ele = BeautifulSoup(codedXmlFile, 'lxml')
    for pTag in ele.findAll('p'):
        pTag.replace_with(pTag.text)
    trLi = ele.findAll('tr')
    for idx in range(len(trLi)):
        curTr = trLi[idx]
        #logger.info(curTr.findAll('th'))
        if len(curTr.findAll('th')) == 4 and '증거금' in curTr.findAll('th')[3].text.strip():
            #logger.info(curTr.text)
            return float(trLi[idx+1].findAll('td')[3].text.replace("%","").strip())
        if len(curTr.findAll('td')) == 4 and '증거금' in curTr.findAll('td')[3].text.strip():
            #logger.info(curTr.text)
            return float(trLi[idx+1].findAll('td')[3].text.replace("%","").strip())
        if len(curTr.findAll('th')) == 5 and '증거금' in curTr.findAll('th')[4].text.strip():
            # logger.info(curTr.text)
            return float(trLi[idx + 1].findAll('td')[4].text.replace("%","").strip())
        if len(curTr.findAll('td')) == 5 and '증거금' in curTr.findAll('td')[4].text.strip():
            # logger.info(curTr.text)
            return float(trLi[idx + 1].findAll('td')[4].text.replace("%","").strip())

#
# if __name__ == "__main__":
#     # logger.info(parseRatioFromXml('20221111000250.xml'))
#     # exit(0)
#     folderPath = './reports'
#     fileNames = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
#     for fileName in fileNames:
#         try:
#             logger.info(f"{fileName:20}/{parseCompanyNameFromXml(fileName):10}")
#             logger.info(parseRatioFromXml(fileName))
#         except UnicodeDecodeError as e:
#             logger.error(fileName +"  "+ "UnicodeDecodeError")
#         except IndexError as e:
#             logger.error(fileName +"  " + "indexError")