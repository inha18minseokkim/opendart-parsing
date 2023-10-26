from loguru import logger
import os
from parser.amountparser import parseAmountFromXml, parseAmountNumberfromString
from parser.infoParser import parseCompanyNameFromXml
from parser.ratioParser import parseRatioFromXml,parseNumberFromStatement
from parser.fileReceiveAndConvert import read_ipo_data
if __name__ == "__main__":
    # logger.info(parseRatioFromXml('20211102000141.xml'))
    # exit(0)
    folderPath = './reports'
    ipoList = read_ipo_data("./resources/ipo_dat.csv")
    print(len(ipoList))

    for ipoInfo in ipoList:
        company = ipoInfo.fssRcipNbr + ".xml"
        try:
            #기업이름 찾기
            logger.info(f"{company:20}/{parseCompanyNameFromXml(company):10}")
            #청약 주식단위 찾기
            amountList = parseAmountFromXml(company)
            logger.info(amountList)
            if len(amountList) < 3:
                pass
            else :
                logger.info(f"{parseAmountNumberfromString(amountList[1])} {parseAmountNumberfromString(amountList[2])} 중 큰거")
            #비율 찾기
            ratio = parseRatioFromXml(company)
            try:
                logger.info(float(ratio))
            except:
                if(ratio != '못찾음'):
                    logger.error(ratio)
                    logger.info(parseNumberFromStatement(ratio))
                else:
                    logger.info(ratio)
        except UnicodeDecodeError as e:
            logger.error(company + "  " + "UnicodeDecodeError")
        except IndexError as e:
            logger.error(company + "  " + "indexError")