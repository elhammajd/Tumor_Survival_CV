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
from sklearn.metrics import roc_curve, auc, accuracy_score,classification_report, confusion_matrix, mean_absolute_error, mean_squared_error   
from sklearn.model_selection import KFold, LeaveOneOut,LeavePOut, StratifiedKFold, RepeatedKFold, ShuffleSplit,RepeatedStratifiedKFold,ParameterGrid, GridSearchCV, train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression, ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import l1_min_c 
from numpy import mean, std, sqrt
import csv as csv 
import pandas as pd 
#import time as time
import pylab as pl
import numpy as np 
from Outputs_M1 import *
#===============================================[HoldOut]============================================
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
    k=''
    #start_time_pred = time.time() 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, shuffle=True)

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
    
    y_pred = model.predict(X_test)
    prob= model.predict_proba(X_test)
       
    #time 
    #end_time_pred = time.time() 
    #Time_pred = (end_time_pred- start_time_pred) 
    #Time = str(Time_pred)


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
                                index = range(7),  
                                columns = ['Coefficient']) 
    coefs['feature']=feature_names
    model = str(r)+ model_name1+ str(k)+ model_name2
    coefs['Model']=model


    cm=confusion_matrix(y_test, y_pred)
    TP = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]
    TN = cm[1][1]

    # Sensitivity, hit rate, recall, or true positive rate
    TPR = TP/(TP+FN)
    # Specificity or true negative rate
    TNR = TN/(TN+FP)

    #view MSE 
    mse = mean_squared_error(y_test, y_pred) 
    #view RMSE 
    rmse = np.sqrt(mse)  

    #obtain pearson residuals
    F = np.array([[y_test], [y_pred]])                                     
    table = sm.stats.Table(F)                                                                            
    pearson_residuals = table.resid_pearson  # Pearson's residuals

    #summary of results
    report = classification_report(y_test, y_pred, output_dict=True) 

    save_output(r, k, model_name1, model_name2,report, coefs, y_test, y_pred, dataset, TPR, TNR, mse, prob, pearson_residuals)
#=============================================[Dataset]============================================== 
#Enter the name of dataset ('NCT02514447', 'NCT03041311', 'NCT02499770')
dataset = 'NCT02514447'
CV_method(dataset,'HoldOut', '')
dataset = 'NCT03041311'
CV_method(dataset,'HoldOut', '')
dataset = 'NCT02499770'
CV_method(dataset,'HoldOut', '')
