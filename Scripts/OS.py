#pip install lifelines
# %matplotlib inline
from lifelines import KaplanMeierFitter 
from lifelines import CoxPHFitter 
from lifelines import WeibullFitter
from lifelines import WeibullAFTFitter
from lifelines import ExponentialFitter
from lifelines import LogNormalFitter
from lifelines import LogLogisticFitter
from lifelines.statistics import proportional_hazard_test
from sklearn import preprocessing
from sklearn.tree import plot_tree
from lifelines.utils import median_survival_times
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import csv as csv
import pandas as pd
import numpy as np
import statistics as st
#======================================================[Dataset]=========================================
def OS(dataset1, dataset2, dataset3, doc, method):

    f1 = open('./Results/'+method+'OS_Bestcut'+dataset1+'.jpg', 'w')
    f1.truncate()
    f1.close()

    f2 = open('./Results/'+method+'WeibullAFT_'+dataset1+'.jpg', 'w')
    f2.truncate()
    f2.close()

    path = './Results/alldata_'+dataset1+'.csv' 
    with open(path ,"r") as f:
        reader =pd.read_csv(f, delimiter=',')
        data=pd.DataFrame(reader)
        data=data.fillna(0)
  
    if (method== 'Method1'):
        mean= pd.read_csv('./Results/Select_Best_Cutoff_Means.csv')
        data['PC2']= mean.loc[0,'PC2']*data[['PC2']]
        data['SEX']= mean.loc[0,'SEX']*data[['SEX']]
        data['AGE']= mean.loc[0,'AGE']*data[['AGE']]
        data['SMOKE']= mean.loc[0,'SMOKE']*data[['SMOKE']]
        data['WEIGHT']= mean.loc[0,'WEIGHT']*data[['WEIGHT']]
        data['RACE']= mean.loc[0,'RACE']*data[['RACE']]
        data['intercept']= mean.loc[0,'intercept']
        data_score= data[['PC2', 'SEX', 'AGE', 'SMOKE', 'WEIGHT', 'RACE','intercept']]

        score= data_score.sum(axis=1)
        Score= np.array(score).reshape(-1,1)
        sc= StandardScaler().fit_transform(Score)
        scaler = preprocessing.MinMaxScaler()
        normalizedScore=scaler.fit_transform(Score)
        print(normalizedScore)
        
        if (dataset1== 'NCT02499770'):
            D1= pd.read_csv('./Results/Select_Best_Cutoff_'+dataset2+'.csv')
            D2= pd.read_csv('./Results/Select_Best_Cutoff_'+dataset3+'.csv')

            BestCut_D1_D2= (max(D1.iloc[:,2])+ max(D2.iloc[:,2]))/2
            group= sc< BestCut_D1_D2/2
            data['Group']=group
            data.Group = data.Group.replace({True: 1, False: 0})

            data['Group'] = data['Group'].astype('category')

        elif (dataset1=='NCT02514447'):
            D1= pd.read_csv('./Results/Select_Best_Cutoff_'+dataset2+'.csv')
            D2= pd.read_csv('./Results/Select_Best_Cutoff_'+dataset3+'.csv')

            BestCut_D1_D2= (max(D1.iloc[:,2])+ max(D2.iloc[:,2]))/2
            group= sc< BestCut_D1_D2
            data['Group']=group
            data.Group = data.Group.replace({True: 1, False: 0})

        elif (dataset1=='NCT03041311'):
            D1= pd.read_csv('./Results/Select_Best_Cutoff_'+dataset2+'.csv')
            D2= pd.read_csv('./Results/Select_Best_Cutoff_'+dataset3+'.csv')

            BestCut_D1_D2= (max(D1.iloc[:,2])+ max(D2.iloc[:,2]))/2
            group= sc> BestCut_D1_D2/2
            data['Group']=group
            data.Group = data.Group.replace({True: 1, False: 0})
 
       
    elif (method== 'Method2'):   
        mean= pd.read_csv('./Results/Select_Best_Cutoff_M2_Means.csv')
        data['PC2']= mean.loc[0,'PC2']*data[['PC2']]
        data['SEX']= mean.loc[0,'SEX']*data[['SEX']]
        data['AGE']= mean.loc[0,'AGE']*data[['AGE']]
        data['SMOKE']= mean.loc[0,'SMOKE']*data[['SMOKE']]
        data['WEIGHT']= mean.loc[0,'WEIGHT']*data[['WEIGHT']]
        data['RACE']= mean.loc[0,'RACE']*data[['RACE']]
        data['intercept']= mean.loc[0,'intercept']
        data_score= data[['PC2','SEX','AGE', 'SMOKE', 'WEIGHT', 'RACE','intercept']]
    
        score= data_score.sum(axis = 1)
        Score= np.array(score).reshape(-1,1)
        sc= StandardScaler().fit_transform(Score)
        scaler = preprocessing.MinMaxScaler()
        normalizedScore=scaler.fit_transform(Score)

        if (dataset1== 'NCT02499770'):
            D1= pd.read_csv('./Results/Select_Best_Cutoff_'+dataset1+'.csv')

            group= sc> (max(D1.iloc[:,2]))
            data['Group']=group
            data.Group = data.Group.replace({True: 1, False: 0})

            data['Group'] = data['Group'].astype('category')

        elif (dataset1=='NCT02514447'):
            D1= pd.read_csv('./Results/Select_Best_Cutoff_'+dataset1+'.csv')

            group= sc< (max(D1.iloc[:,2]))
            data['Group']=group
            data.Group = data.Group.replace({True: 1, False: 0})

        elif (dataset1=='NCT03041311'):
            D1= pd.read_csv('./Results/Select_Best_Cutoff_'+dataset1+'.csv')

            group= sc> (max(D1.iloc[:,2]))            
            data['Group']=group
            data.Group = data.Group.replace({True: 1, False: 0})
        
    #==============================================[Kaplan Meier Curve]=======================================
    plt. clf()
    kmf = KaplanMeierFitter()
    ax = plt.subplot(111)
    m = (data['Group'] == 0)
    Time, Status = data['time'].astype(int), data['event'].astype(int)
    kmf.fit(durations = Time[m], event_observed = Status[m], label = 'FALSE')
    kmf.plot_survival_function(ax = ax)

    kmf.fit(durations = Time[~m], event_observed = Status[~m], label = 'TRUE')
    kmf.plot_survival_function(ax = ax, at_risk_counts = True)
    plt.title("Survival of different group")
    plt.savefig('./Results/'+method+'OS_Bestcut'+dataset1+'.jpg', bbox_inches='tight')

    median_ = kmf.median_survival_time_
    median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
    print('median',median_)
    print(median_confidence_interval_)

    #===========================================[Accelerated Failure Time Model]=============================
    wb= WeibullFitter()
    ex= ExponentialFitter()
    log= LogNormalFitter()
    loglogis= LogLogisticFitter()

    print(data['time'].astype(int))
    data.loc[data['time']==0, 'time']=1
    #Fit to data
    for model in [wb, ex, log, loglogis]:
        model.fit(durations = data['time'].astype(int), event_observed = data['event'].astype(int))
        print('The AIC value for', model.__class__.__name__, 'is', model.AIC_)

    wb_aft= WeibullAFTFitter()
    data2= data[['PC2', 'SEX', 'AGE', 'SMOKE', 'WEIGHT', 'RACE', 'event', 'time', 'Group']]
    wb_aft.fit(data2, duration_col = 'time', event_col = 'event')
    wb_aft.print_summary(decimals = 3, model = 'untransformed variables')
    ax = plt.subplots(figsize=(11,7))
    wb_aft.plot()
    plt.savefig('./Results/'+method+'WeibullAFT_'+dataset1+'.jpg', bbox_inches='tight')
    
OS('NCT02499770', 'NCT02514447', 'NCT03041311', 'Select_Best_Cutoff_', 'Method1')
OS('NCT02514447', 'NCT02499770', 'NCT03041311', 'Select_Best_Cutoff_', 'Method1') 
OS('NCT03041311', 'NCT02499770', 'NCT02514447', 'Select_Best_Cutoff_', 'Method1') 
OS('NCT02499770', 'NCT02514447', 'NCT03041311', 'Select_Best_Cutoff_M2_', 'Method2')
OS('NCT02514447', 'NCT02499770', 'NCT03041311', 'Select_Best_Cutoff_M2_', 'Method2') 
OS('NCT03041311', 'NCT02499770', 'NCT02514447', 'Select_Best_Cutoff_M2_', 'Method2') 
