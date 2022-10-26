import csv as csv 
import pandas as pd 
import time as time
import pylab as pl
import numpy as np 

def save_output(r, k, model_name1, model_name2,report, coefs, y_test, y_pred, dataset, TPR, TNR, NPV, FPR, FNR, FDR, roc_au, cm, Time, mse):
    
    #save the results  
    header=[str(r)+ model_name1+ str(k)+ model_name2]   
    with open('./Results/Coefs_'+dataset+'.csv', 'a', newline='') as pfile:
         coefs.to_csv(pfile, header=True, mode='a') 
    
    header=[str(r)+ model_name1+ str(k)+ model_name2] 
    with open('./Results/Confusion_Matrix_'+dataset+'.csv', 'a', newline='') as file: 
        writer = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        writer.writerow(header) 
        writer.writerow(cm)
    file.close()
    
    header=[str(r)+ model_name1+ str(k)+ model_name2 +'-Time']
    with open('./Results/Time_'+dataset+'.csv', 'a', newline='') as kfile: 
        writer = csv.writer(kfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        writer.writerow(header) 
        writer.writerow(Time) 
    kfile.close()

    performance=['Model','Sensitivity','Specificity','Negative predictive value','False positive rate', 'False negative rate','False discovery rate'] 
    dict0= {'Model':str(r)+ model_name1+ str(k)+ model_name2,'Sensitivity':TPR, 'Specificity':TNR, 'Negative predictive value':NPV, 'False positive rate':FPR, 'False negative rate':FNR, 'False discovery rate':FDR} 

    with open('./Results/Performance_'+dataset+'.csv', 'a', newline='') as rfile: 
        writer = csv.DictWriter(rfile, fieldnames = performance, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        writer.writeheader() 
        writer.writerow(dict0)
    rfile.close()
    
    results=['Model','Accuracy','MSE'] 
    dict1= {'Model':str(r)+ model_name1+ str(k)+ model_name2 ,'Accuracy':report['accuracy'],'MSE':mse} 

    with open('./Results/Result_'+dataset+'.csv', 'a', newline='') as nfile: 
        writer = csv.DictWriter(nfile, fieldnames = results, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        writer.writeheader() 
        writer.writerow(dict1)
    nfile.close() 
        
    summary=['Model','Persicion','Recall', 'F1-score', 'Support', 'Accuracy','MSE', 'Roc_Auc'] 
    dict2={'Model':str(r)+ model_name1+ str(k)+ model_name2,'Persicion':report['weighted avg']['precision'],'Recall':report['weighted avg']['recall'], 
           'F1-score':report['weighted avg']['f1-score'], 'Support':report['weighted avg']['support'], 'Accuracy':report['accuracy'],'MSE':mse, 'Roc_Auc':roc_au } 

    with open('./Results/Summary_'+dataset+'.csv', 'a', newline='') as sfile: 
        writer = csv.DictWriter(sfile, fieldnames = summary, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        writer.writeheader() 
        writer.writerow(dict2)
    sfile.close()
        
    roc=['Model','Roc_Auc'] 
    dict3={'Model':str(r)+ model_name1+ str(k)+ model_name2,'Roc_Auc':roc_au} 

    with open('./Results/Best_Cutoff_'+dataset+'.csv', 'a', newline='') as mfile: 
        writer = csv.DictWriter(mfile, fieldnames = roc, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        writer.writeheader() 
        writer.writerow(dict3)
    mfile.close()
             