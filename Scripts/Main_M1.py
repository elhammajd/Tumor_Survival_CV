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
#from LOOCV import *
#from LpOCV import * 
#from HoldOut import * 
#from KFold import * 
#from StratifiedKFold import *
from RepeatedKFold import *
#from RepeatedStratifiedKFold import *
#=============================================[Dataset]============================================== 
#Select the name of dataset ('NCT02514447', 'NCT03041311', 'NCT02499770')

f1 = open('./Results/M1_Coefs_'+dataset+'.csv', 'a') 
f1.truncate() 
f1.close() 

f2 = open('./Results/M1_Performance_'+dataset+'.csv', 'a') 
f2.truncate() 
f2.close()

f3 = open('./Results/M1_Probability_'+dataset+'.csv', 'a')
f3.truncate()
f3.close()

f4 = open('./Results/M1_Pearson_residuals_'+dataset+'.csv', 'a')
f4.truncate()
f4.close()

dataset = 'NCT03041311'
CV_method(dataset,'LOOCV', '')
CV_method(dataset,'LpOCV', '')
CV_method(dataset,'HoldOut', '')
CV_method(dataset,'Fold', '')
CV_method(dataset,'Stratified','Fold')
CV_method(dataset,'Repeated', 'Fold')
CV_method(dataset,'Repeated_Stratified', 'Fold')
#=============================================[Dataset]============================================== 
f1 = open('./Results/M1_Coefs_'+dataset+'.csv', 'a') 
f1.truncate() 
f1.close() 

f2 = open('./Results/M1_Performance_'+dataset+'.csv', 'a') 
f2.truncate() 
f2.close()

f3 = open('./Results/M1_Probability_'+dataset+'.csv', 'a')
f3.truncate()
f3.close()

f4 = open('./Results/M1_Pearson_residuals_'+dataset+'.csv', 'a')
f4.truncate()
f4.close()


dataset = 'NCT02514447'
CV_method(dataset,'LOOCV', '')
CV_method(dataset,'LpOCV', '')
CV_method(dataset,'HoldOut', '')
CV_method(dataset,'Fold', '')
CV_method(dataset,'Stratified','Fold')
CV_method(dataset,'Repeated', 'Fold')
CV_method(dataset,'Repeated_Stratified', 'Fold')
#=============================================[Dataset]============================================== 
f1 = open('./Results/M1_Coefs_'+dataset+'.csv', 'a') 
f1.truncate() 
f1.close() 

f2 = open('./Results/M1_Performance_'+dataset+'.csv', 'a') 
f2.truncate() 
f2.close()

f3 = open('./Results/M1_Probability_'+dataset+'.csv', 'a')
f3.truncate()
f3.close()

f4 = open('./Results/M1_Pearson_residuals_'+dataset+'.csv', 'a')
f4.truncate()
f4.close()

dataset = 'NCT03041311'
CV_method(dataset,'LOOCV', '')
CV_method(dataset,'LpOCV', '')
CV_method(dataset,'HoldOut', '')
CV_method(dataset,'Fold', '')
CV_method(dataset,'Stratified','Fold')
CV_method(dataset,'Repeated', 'Fold')
CV_method(dataset,'Repeated_Stratified', 'Fold')



