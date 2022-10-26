#======================================[Dataset-Clean files]============================
def clean_files(dataset):
    
    f1 = open('./Results/base_'+dataset+'.csv', 'w')
    f1.truncate()
    f1.close()

    f2 = open('./Results/os_'+dataset+'csv', 'w')
    f2.truncate()
    f2.close()

    f3 = open('./Results/BestResp_'+dataset+'.csv', 'w')
    f3.truncate()
    f3.close()

    f4 = open('./Results/loadings_'+dataset+'.csv', 'w')
    f4.truncate()
    f4.close()

    f5 = open('./Results/alldata_'+dataset+'.csv', 'w')
    f5.truncate()
    f5.close()
    
#Enter the name of dataset ('NCT02514447', 'NCT03041311', 'NCT02499770')    
clean_files('NCT02514447')
clean_files('NCT02499770')
clean_files('NCT03041311')
