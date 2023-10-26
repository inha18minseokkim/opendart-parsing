import csv
import zipfile
import requests
import time
from loguru import logger

from dto.ipoData import IpoInfo

crtfc_key = "bfb1272f4109ed5e959ff0b82b40bb08291ffb45"


def read_ipo_data(file_path) -> list[IpoInfo]:
    ipo_objects = []
    with open(file_path, 'r', newline='',encoding='utf-8-sig') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            #print(row)
            ipo_object = IpoInfo(
                row['ITMS_CD_NBR'], row['STCK_KOR_NM'], row['DMD_FRCS_START_DT'], row['DMD_FRCS_END_DT'],
                row['SBSC_START_DT'], row['SBSC_CLSG_DT'], row['PYM_DT'], row['DRBC_DT'],
                row['STCK_LSTN_DT'], row['LWEN_SCDL_PBOF_AMT'], row['TPPO_SCDL_PBOF_AMT'],
                row['CNFM_PBOF_AMT'], row['PBOF_STCK_CNT'], row['SBSC_RVLR_RT'], row['RPRS_SPIC_COM_NM'],
                row['JOINT_SPIC_COM_NM'], row['RBPE_COM_NM'], row['FSS_RCIP_NBR'], row['STCK_FACE_AMT'],
                row['AISS_GNRL_STCK_CNT'], row['AISS_PRTY_STCK_CNT'], row['NMN_RRT_PROXY_INST_NM'],
                row['DMD_FRCS_RVLR_RT'], row['OBLG_DFPN_APLCT_RATE']
            )
            ipo_objects.append(ipo_object)
    return ipo_objects

def getFileData(rcept_no):
    endPoint = "https://opendart.fss.or.kr/api/document.xml" \
                +"?crtfc_key="+ crtfc_key + "&rcept_no=" + rcept_no
    logger.info(endPoint)
    response = requests.get(endPoint)
    try:
        with open("./reportZips/"+rcept_no+".zip",'wb') as f:
            f.write(response.content)
    except:
        logger.error(rcept_no +" when download zipfile")

def unzipFileData(rcept_no):
    zipFilePath = "/resources/reportZips/"+rcept_no+".zip"
    targetXmlFilePath = "./reports"
    try:
        with zipfile.ZipFile(zipFilePath,'r') as f:
            f.extractall(targetXmlFilePath)
    except:
        logger.error(rcept_no + " when extract from zipfile")
def convertXmlData(rcept_no):

    targetXmlFilePath = "resources//reports"
    try:
        with open(targetXmlFilePath,'r',encoding='euc-kr') as f:
            lines = f.readlines()
        with open(targetXmlFilePath,'w',encoding='utf-8') as f:
            f.writelines(f)
    except:
        logger.error(rcept_no + " when convert euc-kr -> utf-8 from zipfile")



if __name__ == "__main__":
    data = read_ipo_data('resources/ipo_dat.csv')
    idx = 0
    for ele in data:
        if ele.fssRcipNbr == None or len(ele.fssRcipNbr.strip()) == 0:
            logger.error(ele.stckKorNm)
            continue
        logger.info("금감원접수번호 "+ ele.fssRcipNbr + " 청약시작일" + ele.sbscStartDt)
        getFileData(ele.fssRcipNbr)
        unzipFileData(ele.fssRcipNbr)
        convertXmlData(ele.fssRcipNbr)
        time.sleep(1)