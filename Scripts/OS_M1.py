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
#pip install lifelines
# %matplotlib inline
from lifelines import KaplanMeierFitter 
from lifelines import CoxPHFitter 
from lifelines import WeibullFitter
from lifelines import WeibullAFTFitter
from lifelines import ExponentialFitter
from lifelines import LogNormalFitter
from lifelines import LogLogisticFitter
from lifelines.statistics import proportional_hazard_test, logrank_test
from sklearn import preprocessing
from sklearn.tree import plot_tree
from sklearn.linear_model import LogisticRegression, ElasticNet
from sklearn.pipeline import Pipeline
from lifelines.utils import median_survival_times
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import csv as csv
import pandas as pd
import numpy as np
import statistics as st
#=================================================[Dataset]=========================================
def OS(dataset1, dataset2, dataset3):

    f1 = open('./Results/M1_OS_Bestcut'+dataset1+'.jpg', 'w')
    f1.truncate()
    f1.close()

    f2 = open('./Results/M1_WeibullAFT_'+dataset1+'.jpg', 'w')
    f2.truncate()
    f2.close()

    path = './Results/alldata_'+dataset1+'.csv' 
    with open(path ,"r") as f:
        reader =pd.read_csv(f, delimiter=',')
        data=pd.DataFrame(reader)
        data=data.fillna(0)
          
    coef= pd.read_csv('./Results/M1_Means_'+dataset2+'.csv', header =None)
    coef.columns= ['dataset','PC2','SEX','AGE', 'SMOKE', 'WEIGHT', 'RACE', 'intercept']
    coef1= pd.read_csv('./Results/M1_Means_'+dataset3+'.csv', header =None)
    coef1.columns= ['dataset','PC2','SEX','AGE', 'SMOKE', 'WEIGHT', 'RACE', 'intercept']


    data['PC2']= ((coef.loc[0,'PC2']+coef1.loc[0,'PC2'])/2)*data[['PC2']]
    data['SEX']= ((coef.loc[0,'SEX']+coef1.loc[0,'SEX'])/2)*data[['SEX']]
    data['AGE']= ((coef.loc[0,'AGE']+coef1.loc[0,'AGE'])/2)*data[['AGE']]
    data['SMOKE']= ((coef.loc[0,'SMOKE']+coef1.loc[0,'SMOKE'])/2)*data[['SMOKE']]
    data['WEIGHT']= ((coef.loc[0,'WEIGHT']+coef1.loc[0,'WEIGHT'])/2)*data[['WEIGHT']]
    data['RACE']= ((coef.loc[0,'RACE']+coef1.loc[0,'RACE'])/2)*data[['RACE']]
    data['intercept']= (coef.loc[0, 'intercept']+coef1.loc[0, 'intercept'])/2
    data_score= data[['PC2', 'SEX', 'AGE', 'SMOKE', 'WEIGHT', 'RACE', 'intercept']]

    X=data_score
    X=X.to_numpy() 

    y = data[['BORval']] 
    y=y.to_numpy() 
    y=y.ravel()
    model =  Pipeline([('Scaler', StandardScaler()),('estimator', LogisticRegression( 
             penalty='elasticnet',
             solver='saga', 
             multi_class='ovr',
             l1_ratio=int(1e-6),
             tol=1e-6, 
             max_iter=int(1e6), 
             warm_start=True, 
             random_state= 42, 
             intercept_scaling=10000.0))])          
    model.fit(X, y)

    y_pred = model.predict(X)
    prob= model.predict_proba(X)

    #score= data_score.sum(axis=1)
    #Score= np.array(score).reshape(-1,1)
    #sc= StandardScaler().fit_transform(Score)
    #scaler = preprocessing.MinMaxScaler()
    #normalizedScore=scaler.fit_transform(Score)

    D1= pd.read_csv('./Results/M1_Best_Cutoff_'+dataset2+'.csv')
    D1.columns= ['dataset', 'Best_Cutoff']
    D2= pd.read_csv('./Results/M1_Best_Cutoff_'+dataset3+'.csv')
    D2.columns= ['dataset', 'Best_Cutoff']
    BestCut_D1_D2= ((D1['Best_Cutoff'].values)+(D2['Best_Cutoff'].values))/2
    group= prob[:,1]> BestCut_D1_D2/2
    data['group']=group
    data.group = data.group.replace({True: 1, False: 0})

    data['group'] = data['group'].astype('category')
    #==============================================[Kaplan Meier Curve]=======================================
    print('Kaplan Meier Curve', dataset1)
    plt. clf()
    kmf = KaplanMeierFitter()
    plt.rcParams.update({'font.size': 12})
    plt.figure(figsize=(9,6))
    ax = plt.subplot(111)
    data.isnull().sum()
    m = (data['group'] == 0)
    Time, Status = data['time'].astype(int), data['event'].astype(int)
    kmf.fit(durations = Time[m], event_observed = Status[m], label = 'Non-responder')
    kmf.plot_survival_function(ax = ax, ci_show=False)

    kmf.fit(durations = Time[~m], event_observed = Status[~m], label = 'Responder')
    kmf.plot_survival_function(ax = ax, ci_show=False, at_risk_counts = True)
    plt.title("Survival of different group")
    plt.savefig('./Results/M1_OS_Bestcut'+dataset1+'.jpg', bbox_inches='tight')

    median_ = kmf.median_survival_time_
    median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
    print('median',median_)
    print(median_confidence_interval_)
    #===========================================[Accelerated Failure Time Model]=============================
    print('Accelerated Failure', dataset1)
    wb= WeibullFitter()
    ex= ExponentialFitter()
    log= LogNormalFitter()
    loglogis= LogLogisticFitter()

    data.loc[data['time']==0, 'time']=1
    #Fit to data
    for model in [wb, ex, log, loglogis]:
        model.fit(durations = data['time'].astype(int), event_observed = data['event'].astype(int))
        print('The AIC value for', model.__class__.__name__, 'is', model.AIC_)

    wb_aft= WeibullAFTFitter()
    data2= data[['PC2', 'SEX', 'AGE', 'SMOKE', 'WEIGHT', 'RACE', 'event', 'time', 'group']]
    wb_aft.fit(data2, duration_col = 'time', event_col = 'event')
    wb_aft.print_summary(decimals = 3, model = 'untransformed variables')
    ax = plt.subplots(figsize=(9,6))
    wb_aft.plot()
    plt.savefig('./Results/M1_WeibullAFT_'+dataset1+'.jpg', bbox_inches='tight')
    #===========================================[Cox Regression]=============================================
    print('Cox Regression', dataset1)
    data3= data[['PC2', 'SEX', 'AGE', 'SMOKE', 'WEIGHT', 'RACE', 'event', 'time', 'group']]
    cph = CoxPHFitter(alpha=0.05)
    cph.fit(data3, duration_col = 'time', event_col = 'event')
    cph.print_summary(decimals=3)
    #==================================================[Log_Rank_Test]=======================================
    result = logrank_test(data['time'], data['group'], data['event'])
    result.test_statistic
    result.p_value
    log_summary=result.print_summary()
    def p_val(result , decimals=6):
        print('p_value', result.p_value)
    p_val(result , decimals=6)
    
OS('NCT02499770', 'NCT02514447', 'NCT03041311')
 



