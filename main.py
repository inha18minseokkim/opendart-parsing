import xml.etree.ElementTree as elemTree
import re
from bs4 import BeautifulSoup
from loguru import logger
import os
from amountparser import parseAmountFromXml
from infoParser import parseCompanyNameFromXml
from ratioParser import parseRatioFromXml

if __name__ == "__main__":
    # logger.info(parseRatioFromXml('20211102000141.xml'))
    # exit(0)
    folderPath = './reports'
    fileNames = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
    for fileName in fileNames:
        try:
            logger.info(f"{fileName:20}/{parseCompanyNameFromXml(fileName):10}")
            logger.info(parseAmountFromXml(fileName))
            logger.info(parseRatioFromXml(fileName))
        except UnicodeDecodeError as e:
            logger.error(fileName +"  "+ "UnicodeDecodeError")
        except IndexError as e:
            logger.error(fileName +"  " + "indexError")