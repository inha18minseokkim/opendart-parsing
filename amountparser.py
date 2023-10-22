import xml.etree.ElementTree as elemTree
import re
from bs4 import BeautifulSoup
from loguru import logger
import os
def parseAmountFromXml(xmlName):
    targetXmlFilePath = f"./reports/{xmlName}"
    codedXmlFile = ""
    try:
        with open(targetXmlFilePath, 'r', encoding='utf-8') as f:
            codedXmlFile = '\n'.join(f.readlines())
    except:
        with open(targetXmlFilePath, 'r', encoding='euc-kr') as f:
            codedXmlFile = '\n'.join(f.readlines())
    #codedXmlFile = codedXmlFile.replace("TH","TD").replace("th","td")
    ele = BeautifulSoup(codedXmlFile,'lxml')
    for pTag in ele.findAll('p'):
        pTag.replace_with(pTag.text)

    trLi = ele.findAll('tr')
    pattern = re.compile(r'.*청약단위.*')
    pattern2 = re.compile(r'.*')
    pattern3 = re.compile(r'.*【.*')
    pattern4 = re.compile(r'.*\[.*')
    flag = False
    resArr = []
    for idx in range(len(trLi)):
        curTr = trLi[idx]
        # if len(curTr.findAll('td')) == 1 \
        #         and pattern.search(curTr.find('td').text) \
        #         and (pattern3.search(curTr.find('td').text) or (pattern4.search(curTr.find('td').text))
        #             or curTr.find('td').text.strip() == '청약주식별 청약단위'):
        #     resArr.append(curTr.find('td').text.strip().replace('\n',' '))

        if len(curTr.findAll('th')) != 0 \
                and (curTr.findAll('th')[0].text.strip() == '청약주식수' or curTr.findAll('th')[0].text.strip() == '청약증권수' )\
                and curTr.findAll('th')[1].text.strip() == '청약단위':
            try:
                tmpArr = []
                tmpArr.append(f'{ele.find("title").text:20}')
                first = trLi[idx + 1].findAll('td')[0].text.strip().replace('\n', ' ').replace(' ','')
                tmpArr.append(f'{first:30}')
                second = trLi[idx+1].findAll('td')[1].text.strip().replace('\n',' ').replace(' ','')
                tmpArr.append(f'{second:30}')
                return tmpArr
            except:
                logger.error(xmlName + " 오류")
                #logger.error(curTr)
                #logger.error(curTr.findAll('td'))
                #logger.error(trLi[idx+1])
        if len(curTr.findAll('td')) != 0 and curTr.findAll('td')[0].text.strip() == '청약주식수' and curTr.findAll('td')[1].text.strip() == '청약단위':
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
                #logger.error(curTr)
                #logger.error(trLi[idx+1])
    resArr.append(f'{ele.find("title").text:20}')
    return resArr



# if __name__ == "__main__":
#     # logger.info(parseRatioFromXml('20221111000250.xml'))
#     # exit(0)
#     folderPath = './reports'
#     fileNames = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
#     for fileName in fileNames:
#         try:
#             logger.info(f"{fileName:20}/{parseCompanyNameFromXml(fileName):10}")
#             logger.info('@'.join(parseAmountFromXml(fileName)))
#             logger.info(parseRatioFromXml(fileName))
#         except UnicodeDecodeError as e:
#             logger.error(fileName +"  "+ "UnicodeDecodeError")
#         except IndexError as e:
#             logger.error(fileName +"  " + "indexError")