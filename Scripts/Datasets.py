# ==================================================================================================
#    Codes produced by: 
#    - Elham Majd
# ==================================================================================================
#    GitHub:
#    https://github.com/elhammajd/Tumor_Survival_CV
# ==================================================================================================
#    HISTORY:
#    - Creation: OCT/2022
# ==================================================================================================
#    STATEMENT:
#    This file is part of a project entitled "Segmentation of patients with small cell lung cancer into responders and non-responders using the optimal cross-validation technique"
# ==================================================================================================
#pip install Cython
#pip install pyreadstat
from sklearn.decomposition import PCA
import pyreadstat
import pandas as pd
import numpy as np
from functools import reduce
#=============================================[Baseline]=============================================
def dataset(dataset):
    # Read the sas7bdat file
    adsl, meta= pyreadstat.read_sas7bdat('./Data/'+dataset+'/adsl.sas7bdat')
    adsl=pd.DataFrame(adsl)

    base = adsl[['USUBJID' , 'SEX', 'AGEGR1N', 'SMKSTATN', 'WTKG', 'RACEGR1N']]
    base = base.drop_duplicates(keep=False)
    base = base.rename({'SEXN': 'SEX', 'AGEGR1N': 'AGE', 'SMKSTATN': 'SMOKE', 
                        'WTKG': 'WEIGHT', 'RACEGR1N':'RACE'}, axis=1)
    base= base.replace('', pd.NaT)
    base= base.replace('Unknown', pd.NaT)
    base= base.dropna()
    base= base.dropna(how='all')

    base['SEX'].replace({'F':0, 'M':1}, inplace=True)
    base.to_csv('./Results/base_'+dataset+'.csv')
#==========================================[OS]==========================================
    # Read the sas7bdat file
    adtte, meta = pyreadstat.read_sas7bdat('./Data/'+dataset+'/adtte.sas7bdat')
    adtte=pd.DataFrame(adtte)

    os = adtte[['USUBJID', 'CNSR', 'ADY']]
    os = os.drop_duplicates(keep=False)

    os = os.rename({'ADY': 'time'}, axis=1)
    os['event'] = 1-os['CNSR']

    os= os.replace('', pd.NaT)
    os= os.replace('Unknown', pd.NaT)
    os= os.dropna()
    os= os.dropna(how='all')
    os = os[['USUBJID', 'event', 'time']]
    os.to_csv('./Results/os_'+dataset+'.csv')
#===========================================[BOR]=========================================
    # Read the sas7bdat file
    adrs, meta = pyreadstat.read_sas7bdat('./Data/'+dataset+'/adrs.sas7bdat')
    adrs=pd.DataFrame(adrs)

    Best = adrs[adrs['PARAM']=='Best Overall Response ORR']
    Best = Best.drop_duplicates(keep=False)
    BestResp=Best[['USUBJID', 'AVALC']]
    BestResp = BestResp.rename({'AVALC': 'BOR'}, axis=1)
    BestResp['BOR'].replace({'CR':1, 'PR':1, 'SD':0, 'PD':0, 'NE':pd.NaT, 'Unconfirmed PR':pd.NaT,
                            '41':pd.NaT, 'NonCR/NonPD':pd.NaT}, inplace=True)
    BestResp= BestResp.dropna()
    BestResp= BestResp.dropna(how='all')

    BestResp= BestResp.groupby('USUBJID')['BOR'].sum().reset_index()
    BestResp= pd.DataFrame(BestResp)
    BestResp.at[BestResp['BOR'] > 1, 'BORval'] = 1
    BestResp['BORval'] = pd.to_numeric(BestResp['BORval'], errors='coerce').fillna(0).astype(np.int64)
    BestResp=BestResp[['USUBJID', 'BORval']]
    BestResp.to_csv('./Results/BestResp_'+dataset+'.csv')
#===============================================[PCA]===================================
    # Read the sas7bdat file
    dtr, meta = pyreadstat.read_sas7bdat('./Data/'+dataset+'/adtr.sas7bdat')
    dtr=pd.DataFrame(dtr)
    
    if dataset == 'NCT03041311':
        TumorSz=dtr[["USUBJID", "PCHG", "VISITNUM"]]
        SUBJID=(TumorSz[(TumorSz["VISITNUM"]==1215.0) ^ (TumorSz["VISITNUM"]==1415.0) ^ (TumorSz["VISITNUM"]==5002.0)])
        USUBJID= pd.DataFrame(SUBJID["USUBJID"])

        TumorSz=TumorSz.dropna(how='all')
        TumorSz = TumorSz.drop_duplicates(keep=False)
        TumorSz= TumorSz.pivot(columns="VISITNUM", values="PCHG")
        TumorSz=TumorSz.fillna(0)

        # normalize the data before applying the fit method
        TumorSz=(TumorSz - TumorSz.mean()) / TumorSz.std()
        TumorSz=TumorSz[[1215.0,  1415.0, 5002.0]]
        TumorSz = TumorSz.rename({1215.0: "v2", 1415.0: "v2", 5002.0: "v3"}, axis=1)
        
    else:
        TumorSz=dtr[["USUBJID", "PCHG", "AVISITN"]]
        SUBJID=(TumorSz[(TumorSz['AVISITN']==275.0) ^ (TumorSz['AVISITN']==475.0) ^ (TumorSz['AVISITN']==675.0)])
        USUBJID= pd.DataFrame(SUBJID['USUBJID'])

        TumorSz=TumorSz.dropna(how='all')
        TumorSz = TumorSz.drop_duplicates(keep=False)
        TumorSz= TumorSz.pivot(columns='AVISITN', values='PCHG')
        TumorSz=TumorSz.fillna(0)
    
        # normalize the data before applying the fit method
        TumorSz=(TumorSz - TumorSz.mean()) / TumorSz.std()
        TumorSz=TumorSz[[275.0,  475.0, 675.0]]
        TumorSz = TumorSz.rename({275.0: 'v2', 475.0: 'v2', 675.0: 'v3'}, axis=1)

    pca = PCA(n_components=TumorSz.shape[1])
    pca_result=pca.fit(TumorSz)

    # Reformat and view results
    loadings = pd.DataFrame(pca.transform(TumorSz),
    columns=['PC%s' % _ for _ in range(len(TumorSz.columns))],
    index=TumorSz.index)

    loadings['USUBJID']=USUBJID
    loadings=loadings.dropna()
    loadings = loadings.drop_duplicates(keep=False)
    loadings.to_csv('./Results/loadings_'+dataset+'.csv')

    data_frames=[base, os, BestResp, loadings]
    alldata = reduce(lambda  left,right: pd.merge(left,right,on=['USUBJID'],
                                                how='outer'), data_frames).fillna(0)

    alldata.to_csv('./Results/alldata_'+dataset+'.csv')
#=============================================[Dataset]============================================== 
#Enter the name of dataset ('NCT02514447', 'NCT03041311', 'NCT02499770')    
dataset('NCT02514447')
dataset('NCT02499770')
dataset('NCT03041311')
