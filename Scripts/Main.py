from LOOCV import *
from LpOCV import * 
from HoldOut import * 
from KFold import * 
from StratifiedKFold import *
from RepeatedKFold import *
from RepeatedStratifiedKFold import *
from KFold_M2 import * 
from StratifiedKFold_M2 import * 
from RepeatedKFold_M2 import * 
from RepeatedStratifiedKFold_M2 import *
from LOOCV_M2 import *
from LpOCV_M2 import * 
from HoldOut_M2 import * 
#=============================================[Dataset]============================================== 
#Select the name of dataset ('NCT02514447', 'NCT03041311', 'NCT02499770')

dataset = 'NCT03041311'
    
f1 = open('./Results/Time_'+dataset+'.csv', 'w') 
f1.truncate() 
f1.close() 

f2 = open('./Results/Result_'+dataset+'.csv', 'w') 
f2.truncate() 
f2.close() 

f3 = open('./Results/Summary_'+dataset+'.csv', 'w') 
f3.truncate() 
f3.close() 

f4 = open('./Results/Coefs_'+dataset+'.csv', 'w') 
f4.truncate() 
f4.close() 

f5 = open('./Results/Predictions_'+dataset+'.csv', 'w') 
f5.truncate() 
f5.close()

f6 = open('./Results/Confusion_Matrix_'+dataset+'.csv', 'w')
f6.truncate()
f6.close()

f7 = open('./Results/Performance_'+dataset+'.csv', 'w')
f7.truncate()
f7.close()

f8 = open('./Results/Best_Cutoff_'+dataset+'.csv', 'w')
f8.truncate()
f8.close()

f9 = open('./Results/Confusion_Matrix_'+dataset+'.csv', 'w')
f9.truncate()
f9.close()

CV_method(dataset,'LOOCV', '')
CV_method(dataset,'LpOCV', '')
CV_method(dataset,'HoldOut', '')
CV_method(dataset,'Fold', '')
CV_method(dataset,'Stratified','Fold')
CV_method(dataset,'Repeated', 'Fold')
CV_method(dataset,'Repeated_Stratified', 'Fold')
CV_method(dataset,'Fold_M2', '')
CV_method(dataset,'Stratified','Fold_M2')
CV_method(dataset,'Repeated', 'Fold_M2')
CV_method(dataset,'Repeated_Stratified', 'Fold_M2')
CV_method(dataset,'LOOCV_M2', '')
CV_method(dataset,'LpOCV_M2', '')
CV_method(dataset,'HoldOut_M2', '')
#=============================================[Dataset]============================================== 

dataset = 'NCT02514447'

f1 = open('./Results/Time_'+dataset+'.csv', 'w') 
f1.truncate() 
f1.close() 

f2 = open('./Results/Result_'+dataset+'.csv', 'w') 
f2.truncate() 
f2.close() 

f3 = open('./Results/Summary_'+dataset+'.csv', 'w') 
f3.truncate() 
f3.close() 

f4 = open('./Results/Coefs_'+dataset+'.csv', 'w') 
f4.truncate() 
f4.close() 

f5 = open('./Results/Predictions_'+dataset+'.csv', 'w') 
f5.truncate() 
f5.close()

f6 = open('./Results/Confusion_Matrix_'+dataset+'.csv', 'w')
f6.truncate()
f6.close()

f7 = open('./Results/Performance_'+dataset+'.csv', 'w')
f7.truncate()
f7.close()

f8 = open('./Results/Best_Cutoff_'+dataset+'.csv', 'w')
f8.truncate()
f8.close()

f9 = open('./Results/Confusion_Matrix_'+dataset+'.csv', 'w')
f9.truncate()
f9.close()

CV_method(dataset,'LOOCV', '')
CV_method(dataset,'LpOCV', '')
CV_method(dataset,'HoldOut', '')
CV_method(dataset,'Fold', '')
CV_method(dataset,'Stratified','Fold')
CV_method(dataset,'Repeated', 'Fold')
CV_method(dataset,'Repeated_Stratified', 'Fold')
CV_method(dataset,'Fold_M2', '')
CV_method(dataset,'Stratified','Fold_M2')
CV_method(dataset,'Repeated', 'Fold_M2')
CV_method(dataset,'Repeated_Stratified', 'Fold_M2')
CV_method(dataset,'LOOCV_M2', '')
CV_method(dataset,'LpOCV_M2', '')
CV_method(dataset,'HoldOut_M2', '')
#=============================================[Dataset]============================================== 

dataset = 'NCT03041311'

f1 = open('./Results/Time_'+dataset+'.csv', 'w') 
f1.truncate() 
f1.close() 

f2 = open('./Results/Result_'+dataset+'.csv', 'w') 
f2.truncate() 
f2.close() 

f3 = open('./Results/Summary_'+dataset+'.csv', 'w') 
f3.truncate() 
f3.close() 

f4 = open('./Results/Coefs_'+dataset+'.csv', 'w') 
f4.truncate() 
f4.close() 

f5 = open('./Results/Predictions_'+dataset+'.csv', 'w') 
f5.truncate() 
f5.close()

f6 = open('./Results/Confusion_Matrix_'+dataset+'.csv', 'w')
f6.truncate()
f6.close()

f7 = open('./Results/Performance_'+dataset+'.csv', 'w')
f7.truncate()
f7.close()

f8 = open('./Results/Best_Cutoff_'+dataset+'.csv', 'w')
f8.truncate()
f8.close()

f9 = open('./Results/Confusion_Matrix_'+dataset+'.csv', 'w')
f9.truncate()
f9.close()

CV_method(dataset,'LOOCV', '')
CV_method(dataset,'LpOCV', '')
CV_method(dataset,'HoldOut', '')
CV_method(dataset,'Fold', '')
CV_method(dataset,'Stratified','Fold')
CV_method(dataset,'Repeated', 'Fold')
CV_method(dataset,'Repeated_Stratified', 'Fold')
CV_method(dataset,'Fold_M2', '')
CV_method(dataset,'Stratified','Fold_M2')
CV_method(dataset,'Repeated', 'Fold_M2')
CV_method(dataset,'Repeated_Stratified', 'Fold_M2')
CV_method(dataset,'LOOCV_M2', '')
CV_method(dataset,'LpOCV_M2', '')
CV_method(dataset,'HoldOut_M2', '')



