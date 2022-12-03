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

import csv as csv 
import pandas as pd 
import time as time
import pylab as pl
import numpy as np 
import pandas as pd 

def save_output(r, k, model_name1, model_name2,report, coefs, y_test, y_pred, dataset, TPR, TNR, mse, prob, pearson_residuals):
    
    #save the results  
    header=[str(r)+ model_name1+ str(k)+ model_name2]
    with open('./Results/M1_Coefs_'+dataset+'.csv', 'a', newline='') as pfile:
         coefs.to_csv(pfile, header=False, mode='a')
    
    performance=['Model','Accuracy','MSE','Sensitivity','Specificity','Persicion','Recall', 'F1-score', 'Support'] 
    dict1= {'Model':str(r)+ model_name1+ str(k)+ model_name2,'Accuracy':report['accuracy'],'MSE':mse, 'Sensitivity':TPR, 'Specificity':TNR, 'Persicion':report['weighted avg']['precision'],'Recall':report['weighted avg']['recall'], 
           'F1-score':report['weighted avg']['f1-score'], 'Support':report['weighted avg']['support']} 

    with open('./Results/M1_Performance_'+dataset+'.csv', 'a', newline='') as mfile: 
        writer = csv.DictWriter(mfile, fieldnames = performance, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        writer.writeheader() 
        writer.writerow(dict1)
    mfile.close()

    probability=['Model','0','1'] 
    dict2= {'Model':str(r)+ model_name1+ str(k)+ model_name2,'0':prob[:,0],'1':prob[:,1]} 

    with open('./Results/M1_Probability_'+dataset+'.csv', 'a', newline='') as rfile: 
        writer = csv.DictWriter(rfile, fieldnames = probability, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        writer.writeheader() 
        writer.writerow(dict2)
    rfile.close()

    pearson_residuals=['Model','0','1'] 
    dict3= {'Model':str(r)+ model_name1+ str(k)+ model_name2,'0':prob[:,0],'1':prob[:,1]} 

    with open('./Results/M1_Pearson_residuals_'+dataset+'.csv', 'a', newline='') as nfile: 
        writer = csv.DictWriter(nfile, fieldnames = pearson_residuals, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        writer.writeheader() 
        writer.writerow(dict3)
    nfile.close()


            
             