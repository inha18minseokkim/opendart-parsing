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
