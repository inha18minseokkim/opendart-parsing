import xml.etree.ElementTree as elemTree
import re
from bs4 import BeautifulSoup
from loguru import logger
import os
from amountparser import parseAmountFromXml
from infoParser import parseCompanyNameFromXml
from ratioParser import parseRatioFromXml,parseNumberFromStatement

if __name__ == "__main__":
    # logger.info(parseRatioFromXml('20211102000141.xml'))
    # exit(0)
    folderPath = './reports'
    fileNames = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
    for fileName in fileNames:
        try:
            #기업이름 찾기
            logger.info(f"{fileName:20}/{parseCompanyNameFromXml(fileName):10}")
            #청약 주식단위 찾기
            amountList = parseAmountFromXml(fileName)
            logger.info(amountList)
            #비율 찾기
            ratio = parseRatioFromXml(fileName)
            try:
                logger.info(float(ratio))
            except:
                if(ratio != '못찾음'):
                    logger.error(ratio)
                    logger.info(parseNumberFromStatement(ratio))
                else:
                    logger.info(ratio)
        except UnicodeDecodeError as e:
            logger.error(fileName +"  "+ "UnicodeDecodeError")
        except IndexError as e:
            logger.error(fileName +"  " + "indexError")