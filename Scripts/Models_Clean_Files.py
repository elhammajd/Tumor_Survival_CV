#===========================================[Models-Clean files]=========================
def clean_files(dataset):
    
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
   
#Enter the name of dataset ('NCT02514447', 'NCT03041311', 'NCT02499770')    
clean_files('NCT02514447')
clean_files('NCT02499770')
clean_files('NCT03041311')
