import xml.etree.ElementTree as elemTree
import re
from bs4 import BeautifulSoup
from loguru import logger
import os
def parseCompanyNameFromXml(xmlName):
    targetXmlFilePath = f"./resources/reports/{xmlName}"
    codedXmlFile = ""
    try:
        with open(targetXmlFilePath, 'r', encoding='utf-8') as f:
            codedXmlFile = '\n'.join(f.readlines())
    except:
        with open(targetXmlFilePath, 'r', encoding='euc-kr') as f:
            codedXmlFile = '\n'.join(f.readlines())
    ele = BeautifulSoup(codedXmlFile,'lxml')
    return ele.find('company-name').text.replace("주식회사","").replace("(주)","").replace("㈜","").strip()

