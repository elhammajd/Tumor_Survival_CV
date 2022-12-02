# Tumor_Survival_CV
---
## About The Project

Since clinical trials are costly and time-consuming, selecting an experimental treatment in the early stages is essential. Many machine learning methods can use early stages clinical outcomes to segment patients into two groups, responders and non-responders. Such classification models predict the probability of a patient being a responder. In this study, we propose a novel data-driven approach to select a better cutoff value based on the optimal cross-validation technique.
To illustrate our novel method, we applied it to three clinical trial datasets of small-cell lung cancer patients. We used two different datasets to build a scoring system to segment patients. Then the models were applied to segment patients into the test data. 

For more details please read the paper entiteled "Segmentation of patients with small cell lung cancer into responders and non-responders using the optimal cross-validation technique" and the original code in "https://github.com/elhammajd/Tumor_Survival_CV".

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
    │ 	 ├── Main_M1.py 		         # Main code calling the functions of predictive models outputs for the novel method
    │ 	 ├── Main_M2.py 		         # Main code calling the functions of predictive models outputs for the standard method
    │ 	 ├── HouldOut.py	                 # Building predictive method by using HoldOut CV 
    │ 	 ├── LOOCV.py			         # Building predictive method by using LOOCV CV   
    │ 	 ├── LpOCV.py			         # Building predictive method by using LpOCV CV   
    │ 	 ├── KFold.py			         # Building predictive method by KFold CV 
    │ 	 ├── StratifiedKFold.py		         # Building predictive method by using StratifiedKFold CV 
    │ 	 ├── RepeatedKFold.py		         # Building predictive method by using RepeatedKFold CV  
    │ 	 ├── RepeatedStratifiedKFold.py		 # Building predictive method by using RepeatedStratifiedKFold CV 
    │ 	 ├── BestCutoff_M1.py		         # Selecting the best predictive models along with their best cut offs
    │ 	 ├── Mean.py		                 # Calculating the mean of coefficient of features from selected predictive models
    │ 	 ├── Outputs_M1.py	         	 # Saving the results of predictive models in csv files for the novel method
    │ 	 ├── Outputs_M2.py		         #  Saving the results of predictive models in csv files for the standard method
    │ 	 ├── OS_M1.py		                 # Computing Kaplan-Meier, CPH, and AFT according to the novel method	
    │ 	 └── OS_M2.py			         # Computing Kaplan-Meier, CPH, and AFT according to the standard method					
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
    │ 	 ├── Dataset.out		# log.file from Dataset.sh
    │ 	 ├── Main.out		# log.file from Main.sh
    │ 	 ├── BestCutOff.out	# log.file from BestCutOff.sh
    │ 	 ├── Mean.out		# log.file from Mean.sh
    │ 	 └── OS.out		# log.file from OS.sh; **Summary of CPH and AFT model for the novel and the standar model can be found in OS.out**	
	
</details>
<details><summary>outputs (final & intermedia results)</summary>

    ├──  intermedia result
    │ 	 ├── M1_Coefs_NCT02499770.csv	        # Coefficient of each feature for each predictive model on NCT02499770 in the novel model
    │ 	 ├── M1_Coefs_NCT02514447.csv	        # Coefficient of each feature for each predictive model on NCT02514447 in the novel model
    │ 	 ├── M1_Coefs_NCT03041311.csv	        # Coefficient of each feature for each predictive model on NCT03041311 in the novel model
    │ 	 ├── M2_Coefs_NCT02499770.csv	        # Coefficient of each feature for each predictive model on NCT02499770 in the standard model
    │ 	 ├── M2_Coefs_NCT02514447.csv	        # Coefficient of each feature for each predictive model on NCT02514447 in the standard model
    │ 	 ├── M2_Coefs_NCT03041311.csv	        # Coefficient of each feature for each predictive model on NCT03041311 in the standard model
    │ 	 ├── Best_Cutoff_NCT02499770.csv	# Best cut offs of predictive models for NCT02499770 in the novel model
    │ 	 ├── Best_Cutoff_NCT02514447.csv	# Best cut offs of predictive models for NCT02514447 in the novel model
    │ 	 ├── Best_Cutoff_NCT03041311.csv	# Best cut offs of predictive models for NCT03041311 in the novel model
    ├──  final result     
    │ 	 ├── M1_Performance_NCT02499770.csv	# Performance of predictive models for NCT02499770 in the novel model
    │ 	 ├── M1_Performance_NCT02514447.csv	# Performance of predictive models for NCT02514447 in the novel model
    │ 	 ├── M1_Performance_NCT03041311.csv	# Performance of predictive models for NCT03041311 in the novel model
    │ 	 ├── M2_Performance_NCT02499770.csv	# Performance of predictive models for NCT02499770 in the standard model
    │ 	 ├── M2_Performance_NCT02514447.csv	# Performance of predictive models for NCT02514447 in the standard model
    │ 	 ├── M2_Performance_NCT03041311.csv	# Performance of predictive models for NCT03041311 in the standard model
    │ 	 ├── M1_Probability_NCT02499770.csv	# Probability of predictive models for NCT02499770 in the novel model
    │ 	 ├── M1_Probability_NCT02514447.csv     # Probability of predictive models for NCT02514447 in the novel model
    │ 	 ├── M1_Probability_NCT03041311.csv	# Probability of predictive models for NCT03041311 in the novel model
    │ 	 ├── M2_Probability_NCT02499770.csv	# Probability of predictive models for NCT02499770 in the standard model
    │ 	 ├── M2_Probability_NCT02514447.csv	# Probability of predictive models for NCT02514447 in the standard model
    │ 	 ├── M2_Probability_NCT03041311.csv	# Probability of predictive models for NCT03041311 in the standard model
    │ 	 ├── M1_Pearson_residuals_NCT02499770.csv	# Pearson residuals of predictive models for NCT02499770 in the novel model
    │ 	 ├── M1_Pearson_residuals_NCT02514447.csv	# Pearson residuals of predictive models for NCT02514447 in the novel model
    │ 	 ├── M1_Pearson_residuals_NCT03041311.csv	# Pearson residuals of predictive models for NCT03041311 in the novel model
    │ 	 ├── M2_Pearson_residuals_NCT02499770.csv	# Pearson residuals of running predictive models for NCT02499770 in the standard model
    │ 	 ├── M2_Pearson_residuals_NCT02514447.csv	# Pearson residuals of running predictive models for NCT02514447 in the standard model
    │ 	 ├── M2_Pearson_residuals_NCT03041311.csv	# Pearson residuals of running predictive models for NCT03041311 in the standard model
    │ 	 ├── M1_OS_Bestcut_NCT03041311.csv	# Kaplan Meier for NCT03041311 in the novel model
    │ 	 ├── M1_OS_Bestcut_NCT02499770.csv	# Kaplan Meier for NCT02499770 in the novel model
    │ 	 ├── M1_OS_Bestcut_NCT02514447.csv	# Kaplan Meier for NCT02514447 in the novel model
    │ 	 ├── M2_OS_Bestcut_NCT03041311.csv	# Kaplan Meier for NCT03041311 in the standard model
    │ 	 ├── M2_OS_Bestcut_NCT02499770.csv	# Kaplan Meier for NCT02499770 in the standard model
    │ 	 ├── M2_OS_Bestcut_NCT02514447.csv	# Kaplan Meier for NCT02514447 in the standard model
    │ 	 ├── M1_WeibullAFT_NCT02499770.csv	# AFT model for NCT02499770 in the novel model
    │ 	 ├── M1_WeibullAFT_NCT02514447.csv	# AFT model for NCT02514447 in the novel model
    │ 	 ├── M1_WeibullAFT_NCT03041311.csv	# AFT model for NCT03041311 in the novel model
    │ 	 ├── M2_WeibullAFT_NCT02499770.csv	# AFT model for NCT02499770 in the standard model
    │ 	 ├── M2_WeibullAFT_NCT02514447.csv	# AFT model for NCT02514447 in the standard model
    │ 	 └── M2_WeibullAFT_NCT03041311.csv	# AFT model for NCT03041311 in the standard model
    
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
2. create the subdirectories **scripts**, **sh**, **rout**, and **outputs** at [Tumor_Survival_CV]；
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

## Running files

Please run the following jobs in order.


<details><summary>1. Datasets.py</summary>

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


<details><summary>2. Main.py</summary>

- running the seven CV techniques and Nested CV techniques using the merged dataframe reached from Dataset.sh;
	
- saving all results in csv files by running Output.py;

</details>

~~~
    sbatch ./sh/Main.sh
~~~


<details><summary>3. BestCutOff</summary>

- reading the predcition outputs of models reached by running Main.sh;

- detecting the best predcitive models and their best cut offs;


</details>

~~~
    sbatch ./sh/BestCutOff.sh
~~~

<details><summary>4. Mean.py</summary>

- reading the Main.sh and BestCutOff.sh outputs;

- calculating the mean of coefficients of each feature reached from selected predictive models;


</details>

~~~
    sbatch ./sh/Mean.sh
~~~

<details><summary>5. OS.py (30 min)</summary>

- reading the outputs from running Mean.sh and Main.sh;

- computing Kaplan-Meier Curve for each dataset;


</details>

~~~
    sbatch ./sh/OS.sh
~~~






