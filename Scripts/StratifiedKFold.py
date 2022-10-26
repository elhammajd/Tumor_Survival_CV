from sklearn.metrics import roc_curve, auc, accuracy_score,classification_report, confusion_matrix, mean_absolute_error, mean_squared_error   
from sklearn.model_selection import KFold, LeaveOneOut,LeavePOut, StratifiedKFold, RepeatedKFold, ShuffleSplit,RepeatedStratifiedKFold,ParameterGrid, GridSearchCV, train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression, ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import l1_min_c 
from numpy import mean, std, sqrt
import csv as csv 
import pandas as pd 
import time as time
import pylab as pl
import numpy as np
from Outputs import *
#=======================================[Stratified]========================================
SEED=42
def make_dataset(dataset):  

    path = './Results/alldata_'+dataset+'.csv' 

    with open(path ,'r') as f: 
        reader =pd.read_csv(f, delimiter=',') 
        alldata=pd.DataFrame(reader) 

    X = alldata[['PC2','SEX','AGE','SMOKE','WEIGHT','RACE']] 
    X=X.to_numpy() 

    y = alldata[['BORval']] 
    y=y.to_numpy() 
    y=y.ravel()
    return X, y

def CV_method(dataset, model_name1, model_name2):
#split data
    X, y= make_dataset(dataset)
    r=''
    
    start_time_pred = time.time() 

    n_splits = range(3,6)
    for k in n_splits: 
        skf = StratifiedKFold(n_splits=k, shuffle=True, random_state=1)
        for train_ix, test_ix in skf.split(X, y):
            X_train, X_test = X[train_ix, :], X[test_ix, :] 
            y_train, y_test = y[train_ix], y[test_ix]

        #build model 
        model =  Pipeline([('Scaler', StandardScaler()),('estimator', LogisticRegression( 
                penalty='elasticnet', 
                solver='saga', 
                multi_class='ovr',
                l1_ratio=int(1e-6),
                tol=1e-6, 
                max_iter=int(1e6), 
                warm_start=True, 
                random_state= SEED, 
                intercept_scaling=10000.0))])          
        model.fit(X_train, y_train)

        model.intercept_= np.array(model.named_steps['estimator'].intercept_, dtype=float) 
        for m_i in model.intercept_: 
            model_intercept=m_i 

        model.coef_ = np.array(model.named_steps['estimator'].coef_, dtype=float) 
        model_coefficients= model.coef_ 

        for m_f in model_coefficients: 
            model_coefficient=m_f 
        model_coefficient=np.append(model_coefficient, model_intercept)  

        feature_names=['PC2', 'SEX', 'AGE', 'SMOKE', 'WEIGHT', 'RACE', 'intercept'] 
        coefs = pd.DataFrame(data = model_coefficient,  
                                    index = feature_names,  
                                    columns = ['Coefficient value']) 

        y_pred = model.predict(X_test)

        #time 
        end_time_pred = time.time() 
        Time_pred = (end_time_pred- start_time_pred) 
        Time = str(Time_pred)

         # The optimal cut off would be where tpr is high and fpr is low
        fpr, tpr, thresholds =roc_curve(y_test, y_pred)
        roc_auc = auc(fpr, tpr)
        i = np.arange(len(tpr)) # index for df
        roc = pd.DataFrame({'fpr' : pd.Series(fpr, index=i),'tpr' : pd.Series(tpr, index = i), '1-fpr' : pd.Series(1-fpr, index = i), 'tf' : pd.Series(tpr - (1-fpr), index = i), 'thresholds' : pd.Series(thresholds, index = i)})
        cut_off=roc.iloc[(roc.tf-0).abs().argsort()[:1]]
        roc_au=str(roc_auc)

        cm=confusion_matrix(y_test, y_pred)
        print(cm)
        TP = cm[0][0]
        FP = cm[0][1]
        FN = cm[1][0]
        TN = cm[1][1]

        # Sensitivity, hit rate, recall, or true positive rate
        TPR = TP/(TP+FN)
        # Specificity or true negative rate
        TNR = TN/(TN+FP) 
        # Negative predictive value
        NPV = TN/(TN+FN)
        # False positive rate
        FPR = FP/(FP+TN)
        # False negative rate
        FNR = FN/(TP+FN)
        # False discovery rate
        FDR = FP/(TP+FP)

        #view MSE 
        mse = mean_squared_error(y_test, y_pred) 
        #view RMSE 
        rmse = np.sqrt(mse)  

        #summary of results
        report = classification_report(y_test, y_pred, output_dict=True) 

        save_output(r, k, model_name1, model_name2,report, coefs, y_test, y_pred, dataset, TPR, TNR, NPV, FPR, FNR, FDR, roc_au, cm, Time, mse)
#=============================================[Dataset]============================================== 
#Enter the name of dataset ('NCT02514447', 'NCT03041311', 'NCT02499770')
dataset = 'NCT02514447'
CV_method(dataset,'Stratified', 'Fold')
dataset = 'NCT03041311'
CV_method(dataset,'Stratified', 'Fold')
dataset = 'NCT02499770'
CV_method(dataset,'Stratified', 'Fold')

