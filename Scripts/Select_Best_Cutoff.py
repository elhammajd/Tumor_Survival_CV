from csv import writer
import pandas as pd
import statistics as st
import csv as csv

def select_best_cut(dataset):
    f1 = open('./Results/Select_Best_Cutoff_'+dataset+'.csv', 'w') 
    f1.truncate() 
    f1.close() 

    f2 = open('./Results/Select_Best_Cutoff_M2_'+dataset+'.csv', 'w') 
    f2.truncate() 
    f2.close() 
    
    best_cutoff1 = pd.read_csv('./Results/Best_Cutoff_'+dataset+'.csv')
    best_cutoff1=pd.DataFrame(best_cutoff1)

    LOOCV= best_cutoff1[best_cutoff1.iloc[:,0].apply(lambda x: 'LOOCV' in x and '_M2' not in x)]
    Best_LOOCV= max(LOOCV.iloc[:,1])

    LpOCV= best_cutoff1[best_cutoff1.iloc[:,0].apply(lambda x: 'LpOCV' in x and '_M2' not in x)]
    Best_LpOCV= max(LpOCV.iloc[:,1])
        
    HoldOut= best_cutoff1[best_cutoff1.iloc[:,0].apply(lambda x: 'HoldOut' in x and '_M2' not in x)]
    Best_HoldOut= max(HoldOut.iloc[:,1])
    
    KFold=best_cutoff1[best_cutoff1.iloc[:,0].apply(lambda x: 'Fold' in x and 'Stratified' not in x and 'Repeated' not in x and '_M2' not in x)]
    Best_KFold= max(KFold.iloc[:,1])

    Stratified=best_cutoff1[best_cutoff1.iloc[:,0].apply(lambda x: 'Stratified' in x and 'Repeated' not in x and '_M2' not in x)]
    Best_Stratified= max(Stratified.iloc[:,1])
        
    RepeatedKFold=best_cutoff1[best_cutoff1.iloc[:,0].apply(lambda x: 'Repeated' in x and 'Stratified' not in x and '_M2' not in x)]
    Best_RepeatedKFold= max(RepeatedKFold.iloc[:,1])

    Repeated_Stratified= best_cutoff1[best_cutoff1.iloc[:,0].apply(lambda x: 'Repeated_Stratified' in x and '_M2' not in x)]
    Best_Repeated_Stratified= max(Repeated_Stratified.iloc[:,1])
    
    optimal=max(Best_LOOCV, Best_LpOCV, Best_HoldOut, Best_KFold, Best_Stratified, Best_RepeatedKFold, Best_Repeated_Stratified)
    Model= best_cutoff1[best_cutoff1.iloc[:,1]==optimal]
    Model.columns = ['Model', 'Roc']
    
    Model.to_csv('./Results/Select_Best_Cutoff_'+dataset+'.csv', header=True, mode='a')
    
    LOOCV_M2= best_cutoff1[best_cutoff1.iloc[:,0].str.contains('LOOCV_M2', case=False)]
    Best_LOOCV_M2= max(LOOCV_M2.iloc[:,1])

    LpOCV_M2= best_cutoff1[best_cutoff1.iloc[:,0].str.contains('LpOCV_M2', case=False)]
    Best_LpOCV_M2= max(LpOCV_M2.iloc[:,1])
        
    HoldOut_M2= best_cutoff1[best_cutoff1.iloc[:,0].str.contains('HoldOut_M2', case=False)]
    Best_HoldOut_M2= max(HoldOut_M2.iloc[:,1])
    
    KFold_M2=best_cutoff1[best_cutoff1.iloc[:,0].apply(lambda x: 'Fold_M2' in x and 'Stratified' not in x and 'Repeated' not in x)]
    Best_KFold_M2= max(KFold_M2.iloc[:,1])

    StratifiedKFold_M2=best_cutoff1[best_cutoff1.iloc[:,0].apply(lambda x: 'Stratified' in x and 'Fold_M2' in x and 'Repeated' not in x)]
    Best_StratifiedKFold_M2= max(StratifiedKFold_M2.iloc[:,1])
        
    RepeatedKFold_M2=best_cutoff1[best_cutoff1.iloc[:,0].apply(lambda x: 'Repeated' in x and 'Fold_M2' in x and 'Stratified' not in x)]
    Best_RepeatedKFold_M2= max(RepeatedKFold_M2.iloc[:,1])

    Repeated_Stratified_M2= best_cutoff1[best_cutoff1.iloc[:,0].apply(lambda x: 'Repeated_Stratified' in x and 'Fold_M2' in x)]
    Best_Repeated_Stratified_M2= max(Repeated_Stratified.iloc[:,1])
    
    optimal=max( Best_LOOCV_M2, Best_LpOCV_M2, Best_HoldOut_M2, Best_KFold_M2, Best_StratifiedKFold_M2, Best_RepeatedKFold_M2, Best_Repeated_Stratified_M2)
    Model_M2= best_cutoff1[best_cutoff1.iloc[:,1]==optimal]
    Model_M2.columns = ['Model', 'Roc']
    
    Model_M2.to_csv('./Results/Select_Best_Cutoff_M2_'+dataset+'.csv',header=True,mode='a')
    
#=============================================[Dataset]============================================== 
#Enter the name of dataset ('NCT02514447', 'NCT03041311', 'NCT02499770')

dataset = 'NCT02514447'   
select_best_cut(dataset)
dataset = 'NCT03041311'   
select_best_cut(dataset)
dataset = 'NCT02499770'   
select_best_cut(dataset)