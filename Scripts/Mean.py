from csv import writer
import pandas as pd
import statistics as st
import csv as csv
import numpy as np 

def mean(doc):
    f1 = open('./Results/'+doc+'Means.csv', 'w')
    f1.truncate()
    f1.close()

    coeff1 = pd.read_csv('./Results/Coefs_NCT02499770.csv')
    coeff1.columns= ['feature', 'Coefficients', 'Model']
    coeff2 = pd.read_csv('./Results/Coefs_NCT02514447.csv')
    coeff2.columns= ['feature', 'Coefficients', 'Model']
    coeff3 = pd.read_csv('./Results/Coefs_NCT03041311.csv')
    coeff3.columns= ['feature', 'Coefficients', 'Model']

    Model1= pd.read_csv('./Results/'+doc+'NCT02499770.csv')
    Model2= pd.read_csv('./Results/'+doc+'NCT02514447.csv')
    Model3= pd.read_csv('./Results/'+doc+'NCT03041311.csv')

    header_list = ['Model', 'PC2', 'SEX', 'AGE', 'SMOKE', 'WEIGHT', 'RACE', 'intercept']
    with open('./Results/'+doc+'Means.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(header_list)  
        f_object.close()

    X1=(coeff1.loc[:,'Model'].isin(Model1.loc[:,'Model']))
    coefs1=(coeff1.loc[X1])
    coefs1=pd.DataFrame(coefs1)
    coefs1.columns= ['feature', 'Coefficients', 'Model']
    X2=(coeff2.loc[:,'Model'].isin(Model2.loc[:,'Model']))
    coefs2=(coeff1.loc[X2])
    X3=(coeff3.loc[:,'Model'].isin(Model3.loc[:,'Model']))
    coefs3=(coeff1.loc[X3])

    PC2_D2=coefs2.loc[coefs2.loc[:,'feature']=='PC2']
    PC2_D3=coefs3.loc[coefs3.loc[:,'feature']=='PC2']
    PC2_sum=[PC2_D2['Coefficients'].sum(), PC2_D3['Coefficients'].sum()]
    PC2_mean_D1=st.mean(PC2_sum)

    PC2_D1=coefs1.loc[coefs1.loc[:,'feature']=='PC2']
    PC2_D3=coefs3.loc[coefs3.loc[:,'feature']=='PC2']
    PC2_sum=[PC2_D1['Coefficients'].sum(), PC2_D3['Coefficients'].sum()]
    PC2_mean_D2=st.mean(PC2_sum)

    PC2_D1=coefs1.loc[coefs1.loc[:,'feature']=='PC2']
    PC2_D2=coefs2.loc[coefs2.loc[:,'feature']=='PC2']
    PC2_sum=[PC2_D1['Coefficients'].sum(), PC2_D2['Coefficients'].sum()]
    PC2_mean_D3=st.mean(PC2_sum) 

    SEX_D2=coefs2.loc[coefs2.loc[:,'feature']=='SEX']
    SEX_D3=coefs3.loc[coefs3.loc[:,'feature']=='SEX']
    SEX_sum=[SEX_D2['Coefficients'].sum(), SEX_D3['Coefficients'].sum()]
    SEX_mean_D1=st.mean(SEX_sum)

    SEX_D1=coefs1.loc[coefs1.loc[:,'feature']=='SEX']
    SEX_D3=coefs3.loc[coefs3.loc[:,'feature']=='SEX']
    SEX_sum=[SEX_D1['Coefficients'].sum(), SEX_D3['Coefficients'].sum()]
    SEX_mean_D2=st.mean(SEX_sum)

    SEX_D1=coefs1.loc[coefs1.loc[:,'feature']=='SEX']
    SEX_D2=coefs2.loc[coefs2.loc[:,'feature']=='SEX']
    SEX_sum=[SEX_D1['Coefficients'].sum(), SEX_D2['Coefficients'].sum()]
    SEX_mean_D3=st.mean(SEX_sum)

    AGE_D2=coefs2.loc[coefs2.loc[:,'feature']=='AGE']
    AGE_D3=coefs3.loc[coefs3.loc[:,'feature']=='AGE']
    AGE_sum=[AGE_D2['Coefficients'].sum(), AGE_D3['Coefficients'].sum()]
    AGE_mean_D1=st.mean(AGE_sum)

    AGE_D1=coefs1.loc[coefs1.loc[:,'feature']=='AGE']
    AGE_D3=coefs3.loc[coefs3.loc[:,'feature']=='AGE']
    AGE_sum=[AGE_D1['Coefficients'].sum(), AGE_D3['Coefficients'].sum()]
    AGE_mean_D2=st.mean(AGE_sum)

    AGE_D1=coefs1.loc[coefs1.loc[:,'feature']=='AGE']
    AGE_D2=coefs2.loc[coefs2.loc[:,'feature']=='AGE']
    AGE_sum=[AGE_D1['Coefficients'].sum(), AGE_D2['Coefficients'].sum()]
    AGE_mean_D3=st.mean(AGE_sum)

    SMOKE_D2=coefs2.loc[coefs2.loc[:,'feature']=='SMOKE']
    SMOKE_D3=coefs3.loc[coefs3.loc[:,'feature']=='SMOKE']
    SMOKE_sum=[SMOKE_D2['Coefficients'].sum(), SMOKE_D3['Coefficients'].sum()]
    SMOKE_mean_D1=st.mean(SMOKE_sum)

    SMOKE_D1=coefs1.loc[coefs1.loc[:,'feature']=='SMOKE']
    SMOKE_D3=coefs3.loc[coefs3.loc[:,'feature']=='SMOKE']
    SMOKE_sum=[SMOKE_D1['Coefficients'].sum(), SMOKE_D3['Coefficients'].sum()]
    SMOKE_mean_D2=st.mean(SMOKE_sum)

    SMOKE_D1=coefs1.loc[coefs1.loc[:,'feature']=='SMOKE']
    SMOKE_D2=coefs2.loc[coefs2.loc[:,'feature']=='SMOKE']
    SMOKE_sum=[SMOKE_D1['Coefficients'].sum(), SMOKE_D2['Coefficients'].sum()]
    SMOKE_mean_D3=st.mean(SMOKE_sum)


    WEIGHT_D2=coefs2.loc[coefs2.loc[:,'feature']=='WEIGHT']
    WEIGHT_D3=coefs3.loc[coefs3.loc[:,'feature']=='WEIGHT']
    WEIGHT_sum=[WEIGHT_D2['Coefficients'].sum(), WEIGHT_D3['Coefficients'].sum()]
    WEIGHT_mean_D1=st.mean(WEIGHT_sum)

    WEIGHT_D1=coefs1.loc[coefs1.loc[:,'feature']=='WEIGHT']
    WEIGHT_D3=coefs3.loc[coefs3.loc[:,'feature']=='WEIGHT']
    WEIGHT_sum=[WEIGHT_D1['Coefficients'].sum(), WEIGHT_D3['Coefficients'].sum()]
    WEIGHT_mean_D2=st.mean(WEIGHT_sum)

    WEIGHT_D1=coefs1.loc[coefs1.loc[:,'feature']=='WEIGHT']
    WEIGHT_D2=coefs2.loc[coefs2.loc[:,'feature']=='WEIGHT']
    WEIGHT_sum=[WEIGHT_D1['Coefficients'].sum(), WEIGHT_D2['Coefficients'].sum()]
    WEIGHT_mean_D3=st.mean(WEIGHT_sum)

    RACE_D2=coefs2.loc[coefs2.loc[:,'feature']=='RACE']
    RACE_D3=coefs3.loc[coefs3.loc[:,'feature']=='RACE']
    RACE_sum=[RACE_D2['Coefficients'].sum(), RACE_D3['Coefficients'].sum()]
    RACE_mean_D1=st.mean(RACE_sum)

    RACE_D1=coefs1.loc[coefs1.loc[:,'feature']=='RACE']
    RACE_D3=coefs3.loc[coefs3.loc[:,'feature']=='RACE']
    RACE_sum=[RACE_D1['Coefficients'].sum(), RACE_D3['Coefficients'].sum()]
    RACE_mean_D2=st.mean(RACE_sum)

    RACE_D1=coefs1.loc[coefs1.loc[:,'feature']=='RACE']
    RACE_D2=coefs2.loc[coefs2.loc[:,'feature']=='RACE']
    RACE_sum=[RACE_D1['Coefficients'].sum(), RACE_D2['Coefficients'].sum()]
    RACE_mean_D3=st.mean(RACE_sum)

    intercept_D2=coefs2.loc[coefs2.loc[:,'feature']=='intercept']
    intercept_D3=coefs3.loc[coefs3.loc[:,'feature']=='intercept']
    intercept_sum=[intercept_D2['Coefficients'].sum(), intercept_D3['Coefficients'].sum()]
    intercept_mean_D1=st.mean(intercept_sum)

    intercept_D1=coefs1.loc[coefs1.loc[:,'feature']=='intercept']
    intercept_D3=coefs3.loc[coefs3.loc[:,'feature']=='intercept']
    intercept_sum=[intercept_D1['Coefficients'].sum(), intercept_D3['Coefficients'].sum()]
    intercept_mean_D2=st.mean(intercept_sum)

    intercept_D1=coefs1.loc[coefs1.loc[:,'feature']=='intercept']
    intercept_D2=coefs2.loc[coefs2.loc[:,'feature']=='intercept']
    intercept_sum=[intercept_D1['Coefficients'].sum(), intercept_D2['Coefficients'].sum()]
    intercept_mean_D3=st.mean(intercept_sum)


    if (doc=='Select_Best_Cutoff_'):
        
        Mean_D1=['NCT02499770', PC2_mean_D1, SEX_mean_D1, AGE_mean_D1, SMOKE_mean_D1, WEIGHT_mean_D1, RACE_mean_D1, intercept_mean_D1]
        print(Mean_D1)
        with open('./Results/'+doc+'Means.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(Mean_D1)  
            f_object.close()   


        Mean_D2=['NCT02514447', PC2_mean_D2, SEX_mean_D2, AGE_mean_D2, SMOKE_mean_D2, WEIGHT_mean_D2, RACE_mean_D2,intercept_mean_D2]
        with open('./Results/'+doc+'Means.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(Mean_D2)  
            f_object.close()

        Mean_D3=['NCT03041311', PC2_mean_D3, SEX_mean_D3, AGE_mean_D3, SMOKE_mean_D3, WEIGHT_mean_D3, RACE_mean_D3, intercept_mean_D3]
        with open('./Results/'+doc+'Means.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(Mean_D3)  
            f_object.close()
            
    if (doc=='Select_Best_Cutoff_M2_'):
        
        Mean_D1=['NCT02499770', PC2_D1['Coefficients'].sum(), SEX_D1['Coefficients'].sum(), AGE_D1['Coefficients'].sum(), SMOKE_D1['Coefficients'].sum(), WEIGHT_D1['Coefficients'].sum(), RACE_D1['Coefficients'].sum(), intercept_D1['Coefficients'].sum()]
        with open('./Results/'+doc+'Means.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(Mean_D1)  
            f_object.close()   


        Mean_D2=['NCT02514447', PC2_D1['Coefficients'].sum(), SEX_D1['Coefficients'].sum(), AGE_D1['Coefficients'].sum(), SMOKE_D1['Coefficients'].sum(), WEIGHT_D1['Coefficients'].sum(), RACE_D1['Coefficients'].sum(), intercept_D1['Coefficients'].sum()]
        with open('./Results/'+doc+'Means.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(Mean_D2)  
            f_object.close()

        Mean_D3=['NCT03041311', PC2_D1['Coefficients'].sum(), SEX_D1['Coefficients'].sum(), AGE_D1['Coefficients'].sum(), SMOKE_D1['Coefficients'].sum(), WEIGHT_D1['Coefficients'].sum(), RACE_D1['Coefficients'].sum(), intercept_D1['Coefficients'].sum()]
        with open('./Results/'+doc+'Means.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(Mean_D3)  
            f_object.close()

doc='Select_Best_Cutoff_'
mean(doc)
doc='Select_Best_Cutoff_M2_'
mean(doc)