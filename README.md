# Tumor_Survival_CV
---
## About The Project

This study confirms that the CV technique has significant impact on the accuracy of prediction probability of BOR. Thus, it is important to find and apply the optimal CV technique to build the predictive models. The results of this study shows, although, the datasets may have similar pre-processing, the same features, and data types but different size of data. The optimal CV technique to predict the probability of BOR is not the same. This study carried out to explore whether one specific CV technique can be get the most accurate predictions and segmentation of patients on clinical trials. In many previous studies, one specific CV technique was applied without explanations about the reasons of selection or testing other CV techniques. Using inappropriate CV technique can negative impact on the predictions and segmentations patients. It can be very vital in real clinical practice to predict the probability of clinical trials feature accurately. The results revealed that the best CV technique is uncertain in practice. Thus, it is important to try to consider the performance of different CV technique on clinical trials. In this study, a general model contains seven main CV techniques, in addition, the Nested CV technique were used to select the best prediction probability of BOR and segment the patients based on scores and best cut of that reached from the best performance of predictive models and then the CV technique were resulted in best performance were selected as the optimal CV technique. 

---
## Directory Layout
![image](image0.png)

We assume the user set the default directory at **beluga** at Compute Canada
~~~
    [Tumor_Survival_CV]  
~~~
all codes are in the subdirectory directory at **Tumor_Survival_CV**
~~~
    [Tumor_Survival_CV]/Scripts 
~~~
all the .sh files that run the python files are in the subdirectory directory at **sh** 
~~~
    [Tumor_Survival_CV]/sh  
~~~
all the log files are in the subdirectory directory at **rout** 
~~~
    [Tumor_Survival_CV]/rout  
~~~
all the final results/intermedia results are in the subdirectory directory at **outputs**
~~~
    [Tumor_Survival_CV]/Results  
~~~
all the **data**  are stored at the directory bellow, which are accessible to group members
~~~
    [Tumor_Survival_CV]/Data 
~~~

<details><summary>scripts</summary>

    ├── scripts  
    │ 	 ├── Datasets.py	                 # Making dataframes for building the predcitive models
    │ 	 ├── Main.py 		                 # Main code calling the functions of predictive models outputs
    │ 	 ├── HouldOut.py	                 # Building predictive method by using HoldOut CV 
    │ 	 ├── HouldOut_M2.py		         # Building predictive method by using Nested HoldOut CV  
    │ 	 ├── LOOCV.py			         # Building predictive method by using LOOCV CV   
    │ 	 ├── LOOCV_M2.py		         # Building predictive method by using Nested LOOCV CV 
    │ 	 ├── LpOCV.py			         # Building predictive method by using LpOCV CV  
    │ 	 ├── LpOCV_M2.py		         # Building predictive method by using Nested LpOCV CV  
    │ 	 ├── KFold.py			         # Building predictive method by KFold CV 
    │ 	 ├── KFold_M2.py		         # Building predictive method by using Nested KFold CV 
    │ 	 ├── StratifiedKFold.py		         # Building predictive method by using StratifiedKFold CV 
    │ 	 ├── StratifiedKFold_M2.py	         # Building predictive method by using Nested StratifiedKFold CV 
    │ 	 ├── RepeatedKFold.py		         # Building predictive method by using RepeatedKFold CV  
    │ 	 ├── RepeatedKFold_M2.py	         # Building predictive method by using Nested RepeatedKFold CV 
    │ 	 ├── RepeatedStratifiedKFold.py		 # Building predictive method by using RepeatedStratifiedKFold CV 
    │ 	 ├── RepeatedStratifiedKFold_M2.py	 # Building predictive method by using Nested RepeatedStratifiedKFold CV 
    │ 	 ├── Outputs.py			         # The functions for saving the results of predictive models in csv files 
    │ 	 ├── Select_Best_Cutoff.py		 # Selecting the best predictive models along with their best cut offs
    │ 	 ├── Mean.py		                 # Calculating the mean of coefficient of features from selected predictive models
    │ 	 └── OS.py			         # Computing Kaplan-Meier Curve according to selected predictive models				
</details>
<details><summary>sh</summary>
    
    ├── sh  
    │ 	 ├── Dataset.sh		# sh.file to run Datasets.py
    │ 	 ├── Main.sh		# sh.file to run Main.py, HoldOut.py, HoldOut_M2, and ...
    │ 	 ├── BestCutOff.sh	# sh.file to run Select_Best_Cutoff.py
    │ 	 ├── Mean.sh		# sh.file to run Mean.py
    │ 	 └── OS.sh		# sh.file to run OS.py		
		
</details>
<details><summary>rout</summary>
        
    ├── rout  
    │ 	 ├── Dataset.sh		# log.file from Dataset.sh
    │ 	 ├── Main.sh		# log.file from Main.sh
    │ 	 ├── BestCutOff.sh	# log.file from BestCutOff.sh
    │ 	 ├── Mean.sh		# log.file from Mean.sh
    │ 	 └── OS.sh		# log.file from OS.sh	
	
</details>
<details><summary>outputs (final & intermedia results)</summary>

    ├──  intermedia result
    │ 	 ├── Coefs_NCT02499770.csv	        # Coefficient of each feature for each predictive model on NCT02499770 
    │ 	 ├── Coefs_NCT02514447.csv	        # Coefficient of each feature for each predictive model on NCT02514447
    │ 	 ├── Coefs_NCT03041311.csv	        # Coefficient of each feature for each predictive model on NCT03041311
    │ 	 ├── Best_Cutoff_NCT02499770.csv	# Best cut offs of predictive models for NCT02499770
    │ 	 ├── Best_Cutoff_NCT02514447.csv	# Best cut offs of predictive models for NCT02514447
    │ 	 ├── Best_Cutoff_NCT03041311.csv	# Best cut offs of predictive models for NCT03041311
    ├──  final result     
    │ 	 ├── Performance_NCT02499770.csv	# Performance of predictive models for NCT02499770
    │ 	 ├── Performance_NCT02514447.csv	# Performance of predictive models for NCT02514447
    │ 	 ├── Performance_NCT03041311.csv	# Performance of predictive models for NCT03041311
    │ 	 ├── Result_NCT02499770.csv	        # Result of predictive models for NCT02499770
    │ 	 ├── Result_NCT02514447.csv             # Result of predictive models for NCT02514447
    │ 	 ├── Result_NCT03041311.csv	        # Result of predictive models for NCT03041311
    │ 	 ├── Summary_NCT02499770.csv	        # Summary of predictive models for NCT02499770
    │ 	 ├── Summary_NCT02514447.csv	        # Summary of predictive models for NCT02514447
    │ 	 ├── Summary_NCT03041311.csv	        # Summary of predictive models for NCT03041311
    │ 	 ├── Confusion_Matrix_NCT02499770.csv	# Confusion Matrix of predictive models for NCT02499770
    │ 	 ├── Confusion_Matrix_NCT02514447.csv	# Confusion Matrix of predictive models for NCT02514447
    │ 	 ├── Confusion_Matrix_NCT03041311.csv	# Confusion Matrix of predictive models for NCT03041311
    │ 	 ├── Time_NCT02499770.csv	        # Time of running predictive models for NCT02499770
    │ 	 ├── Time_NCT02514447.csv	        # Time of running predictive models for NCT02514447
    │ 	 └── Time_NCT03041311.csv	        # Time of running predictive models for NCT03041311
</details>
<details><summary>data</summary>
	    
    ├── data
    │ 	 ├── NCT02499770	# Small Cell Lung Cancer dataset, downloaded from https://data.projectdatasphere.org/projectdatasphere/html/access
    │ 	 ├── NCT02514447	# Small Cell Lung Cancer dataset, downloaded from https://data.projectdatasphere.org/projectdatasphere/html/access
    │ 	 └── NCT03041311	# Small Cell Lung Cancer dataset, downloaded from https://data.projectdatasphere.org/projectdatasphere/html/access
 
</details>

---
## Notice

As all the processes are conducted using the relative path, it's very important to set up [Tumor_Survival_CV] and use it correctly. 
[Tumor_Survival_CV] should be consisted of three parts: part 1 is ```/project/6003851/``` to ensure all the files can run on Compute Canada; part 2 is your ```user name``` at Compute Canada; part 3 is your ```folder's name```. For example, the writer's directory is as follows:

~~~
/project/6003851/elhma/Tumor_Survival_CV
~~~

If you are not sure about the path of your working folder, try to type in 'pwd' command in linux or 'getwd()' in R language for reference. 

---
## Before you start
1. decide the path of [Tumor_Survival_CV] to replicate our results;
2. create the subdirectories **scripts**, **sh**, **rout**, and **outputs** at [DAISM]；
3. allocate all relevant files into each subdirectory. The **rout**, and **outputs** folders will be empty at the beginning while the **scripts** and **sh** folders should look like the figure below:

![image](image1.png)

5. In the main directory [Tumor_Survival_CV], use the following commands to python/3.8  language in Compute Canada (The environment settings in CC change occasionally, make sure to check and use their latest settings):
~~~
module load python/3.8
~~~
4. before we run the .sh files, we use in the following commands in to install some packages needed for the task
~~~
pip install Cython
pip install pyreadstat
pip install sklearn
pip install numpy
pip install pandas
~~~

---

## Running files (estimated time per job)


<details><summary>1. Datasets.py (20 min)</summary>

- reading dataset downloaded from https://data.projectdatasphere.org/projectdatasphere/html/access;

- building a dataframe of baseline characteristics of patients;

- building a dataframe of PCA of the dynamic tumor size for the early four visits;
	
- building a dataframe of Overall Survival;

- building a dataframe of Best Overall Response;

- building a merged dataframe from all features;	

 </details>
 
 ~~~
    sbatch ./sh/Dataset.sh
~~~


<details><summary>2.Main.py (12 hours)</summary>

- running the seven CV techniques and Nested CV techniques using the merged dataframe comesd from Dataset.sh;
	
- saving all results in csv files by running Output.py;

</details>

~~~
    sbatch ./sh/Main.sh
~~~


<details><summary>3.BestCutOff (20 min)</summary>

- reading the predcition outputs of models reached by running Main.sh;

- detecting the best predcitive models and their best cut offs;


</details>

~~~
    sbatch ./sh/BestCutOff.sh
~~~

<details><summary>4.Mean.py (20 min)</summary>

- reading the Main.sh and BestCutOff.sh outputs;

- calculating the mean of coefficients of eact feature comes from selected predictive models;


</details>

~~~
    sbatch ./sh/Mean.sh
~~~

<details><summary>5.OS.py (30 min)</summary>

- reading the outputs of by running Mean.sh and Main.sh;

- computing Kaplan-Meier Curve for each dataset;


</details>

~~~
    sbatch ./sh/OS.sh
~~~






