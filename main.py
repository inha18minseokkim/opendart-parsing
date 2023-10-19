import csv
import zipfile
import requests
import time
from loguru import logger
crtfc_key = "bfb1272f4109ed5e959ff0b82b40bb08291ffb45"

class IpoInfo:
    def __init__(self, itmsCdNbr, stckKorNm, dmdFrcsStartDt, dmdFrcsEndDt, sbscStartDt, sbscClsgDt,
                 pymDt, drbcDt, stckLstnDt, lwenScdlPbofAmt, tppoScdlPbofAmt, cnfmPbofAmt, pbofStckCnt,
                 sbscRvlrRt, rprsSpicComNm, jointSpicComNm, rbpeComNm, fssRcipNbr, stckFaceAmt,
                 aissGnrlStckCnt, aissPrtyStckCnt, nmnRrtProxyInstNm, dmdFrcsRvlrRt, oblgDfpnAplctRate):
        self.itmsCdNbr = itmsCdNbr
        self.stckKorNm = stckKorNm
        self.dmdFrcsStartDt = dmdFrcsStartDt
        self.dmdFrcsEndDt = dmdFrcsEndDt
        self.sbscStartDt = sbscStartDt
        self.sbscClsgDt = sbscClsgDt
        self.pymDt = pymDt
        self.drbcDt = drbcDt
        self.stckLstnDt = stckLstnDt
        self.lwenScdlPbofAmt = lwenScdlPbofAmt
        self.tppoScdlPbofAmt = tppoScdlPbofAmt
        self.cnfmPbofAmt = cnfmPbofAmt
        self.pbofStckCnt = pbofStckCnt
        self.sbscRvlrRt = sbscRvlrRt
        self.rprsSpicComNm = rprsSpicComNm
        self.jointSpicComNm = jointSpicComNm
        self.rbpeComNm = rbpeComNm
        self.fssRcipNbr = fssRcipNbr
        self.stckFaceAmt = stckFaceAmt
        self.aissGnrlStckCnt = aissGnrlStckCnt
        self.aissPrtyStckCnt = aissPrtyStckCnt
        self.nmnRrtProxyInstNm = nmnRrtProxyInstNm
        self.dmdFrcsRvlrRt = dmdFrcsRvlrRt
        self.oblgDfpnAplctRate = oblgDfpnAplctRate
    def __str__(self):
        return f"ITMS_CD_NBR: {self.itmsCdNbr}, STCK_KOR_NM: {self.stckKorNm}, DMD_FRCS_START_DT: {self.dmdFrcsStartDt}, DMD_FRCS_END_DT: {self.dmdFrcsEndDt}, SBSC_START_DT: {self.sbscStartDt}, SBSC_CLSG_DT: {self.sbscClsgDt}, PYM_DT: {self.pymDt}, DRBC_DT: {self.drbcDt}, STCK_LSTN_DT: {self.stckLstnDt}, LWEN_SCDL_PBOF_AMT: {self.lwenScdlPbofAmt}, TPPO_SCDL_PBOF_AMT: {self.tppoScdlPbofAmt}, CNFM_PBOF_AMT: {self.cnfmPbofAmt}, PBOF_STCK_CNT: {self.pbofStckCnt}, SBSC_RVLR_RT: {self.sbscRvlrRt}, RPRS_SPIC_COM_NM: {self.rprsSpicComNm}, JOINT_SPIC_COM_NM: {self.jointSpicComNm}, RBPE_COM_NM: {self.rbpeComNm}, FSS_RCIP_NBR: {self.fssRcipNbr}, STCK_FACE_AMT: {self.stckFaceAmt}, AISS_GNRL_STCK_CNT: {self.aissGnrlStckCnt}, AISS_PRTY_STCK_CNT: {self.aissPrtyStckCnt}, NMN_RRT_PROXY_INST_NM: {self.nmnRrtProxyInstNm}, DMD_FRCS_RVLR_RT: {self.dmdFrcsRvlrRt}, OBLG_DFPN_APLCT_RATE: {self.oblgDfpnAplctRate}"

def read_ipo_data(file_path):
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
    zipFilePath = "./reportZips/"+rcept_no+".zip"
    targetXmlFilePath = "./reports"
    try:
        with zipfile.ZipFile(zipFilePath,'r') as f:
            f.extractall(targetXmlFilePath)
    except:
        logger.error(rcept_no + " when extract from zipfile")
def convertXmlData(rcept_no):

    targetXmlFilePath = "./reports"
    try:
        with open(targetXmlFilePath,'r',encoding='euc-kr') as f:
            lines = f.readlines()
        with open(targetXmlFilePath,'w',encoding='utf-8') as f:
            f.writelines(f)
    except:
        logger.error(rcept_no + " when convert euc-kr -> utf-8 from zipfile")



if __name__ == "__main__":
    data = read_ipo_data('./ipo_dat.csv')
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