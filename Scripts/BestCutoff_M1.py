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
from csv import writer
import pandas as pd
import statistics as st
import csv as csv

def select_best_cut(dataset):
    f1 = open('./Results/M1_Best_Cutoff_'+dataset+'.csv', 'w') 
    f1.truncate() 
    f1.close()  
    
    cutoff0 = pd.read_csv('./Results/M1_Performance_'+dataset+'.csv')
    cutoff0=pd.DataFrame(cutoff0)
    cutoff1 = cutoff0[~cutoff0['Model'].str.contains('Model')]
    cutoff1=pd.DataFrame(cutoff1)


    Best_Cutoff= cutoff1['F1-score'].max()
    i = cutoff1['F1-score'].astype(float).idxmax()
    Model= cutoff1['Model'][i]

    best_cutoff1=['Model','Best_Cutoff'] 
    dict0= {'Model':Model,'Best_Cutoff':Best_Cutoff} 
    
    with open('./Results/M1_Best_Cutoff_'+dataset+'.csv', 'a', newline='') as mfile: 
        writer = csv.DictWriter(mfile, fieldnames = best_cutoff1, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        writer.writeheader() 
        writer.writerow(dict0)
    mfile.close()
#=======================================================================================================================

    f2 = open('./Results/M2_Best_Cutoff_'+dataset+'.csv', 'w') 
    f2.truncate() 
    f2.close()

    cutoff2 = pd.read_csv('./Results/M2_Performance_'+dataset+'.csv')
    cutoff2=pd.DataFrame(cutoff2)
    cutoff3 = cutoff2[~cutoff2['Model'].str.contains('Model')]
    cutoff3=pd.DataFrame(cutoff3)
   
    Best_Cutoff_M2= cutoff3['F1-score'].max()
    j = cutoff3['F1-score'].astype(float).idxmax()
    Model= cutoff3['Model'][j]

    best_cutoff2=['Model','Best_Cutoff'] 
    dict1= {'Model':Model,'Best_Cutoff':Best_Cutoff_M2} 
    
    with open('./Results/M2_Best_Cutoff_'+dataset+'.csv', 'a', newline='') as nfile: 
        writer = csv.DictWriter(nfile, fieldnames = best_cutoff2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        writer.writeheader() 
        writer.writerow(dict1)
    nfile.close()    
#=============================================[Dataset]============================================== 
#Enter the name of dataset ('NCT02514447', 'NCT03041311', 'NCT02499770')

dataset = 'NCT02514447'   
select_best_cut(dataset)
dataset = 'NCT03041311'   
select_best_cut(dataset)
dataset = 'NCT02499770'   
select_best_cut(dataset)