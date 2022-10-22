# Tumor_Survival_CV
---
## About The Project



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
all the **data** from Schelker are stored at the directory bellow, which are accessible to all group members
~~~
    [Tumor_Survival_CV]/Data 
~~~

<details><summary>scripts</summary>

    ├── scripts  
    │    ├── Datasets.py		    # Making dataframes for building the predcitive models
    │ 	 ├── Main.py 		# main code using to build the predictive models 
    │ 	 ├── HouldOut.py			        # import pkg_resources
    │ 	 ├── HouldOut_M2.py			# Build simulation using test and purified.h5ad 
    │ 	 ├── LOOCV.py			# Split data to train and test   
    │ 	 ├── LOOCV_M2.py			        # import pkg_resources
    │ 	 ├── LpOCV.py			# Build simulation using test and purified.h5ad 
    │ 	 ├── LpOCV_M2.py			# Split data to train and test 
    │ 	 ├── KFold.py			        # import pkg_resources
    │ 	 ├── KFold_M2.py			# Build simulation using test and purified.h5ad 
    │ 	 ├── StratifiedKFold.py			# Split data to train and test
    │ 	 ├── StratifiedKFold_M2.py			# Build simulation using test and purified.h5ad 
    │ 	 ├── RepeatedKFold.py			# Split data to train and test 
    │ 	 ├── RepeatedKFold_M2.py			        # import pkg_resources
    │ 	 ├── RepeatedStratifiedKFold.py			# Build simulation using test and purified.h5ad 
    │ 	 ├── RepeatedStratifiedKFold_M2.py			# Split data to train and test
    │ 	 ├── Outputs.py			# Build simulation using test and purified.h5ad 
    │ 	 ├── Select_Best_Cutoff.py			# Split data to train and test
    │ 	 ├── Mean.py			# Split data to train and test
    │ 	 └── OS.py			# Predict the estimated proportion				
</details>
<details><summary>sh</summary>

    ├── sh  
    │    ├── create_h5ad.sh		# sh.file to run create_h5ad.py
    │ 	 ├── simulation.sh		# sh.files to run simulation.py
    │    ├── training.sh		# sh.files to run training.py
    │ 	 └── prediction.sh		# sh.files to run prediction.py 		
</details>
<details><summary>rout</summary>

    ├── rout 
    │    ├── create_h5ad.rout		# log.file for create_h5ad.sh
    │ 	 ├── simulation.rout		# log.file for simulation.sh
    │    ├── training.rout		# log.file for training.sh
    │ 	 └── prediction.rout		# log.file for prediction.sh 
</details>
<details><summary>outputs (final & intermedia results)</summary>

    ├──  intermedia result
    │    ├── purified.h5ad		    # it is the purified dataset for data augmentation
    │ 	 ├── Generic_mixfra 	# from simulation
    │    ├── Generic_mixsam.txt			# from simulation
    │    ├── Generic_celltypes.txt			# from simulation
    │    ├── Generic_celltypes.txt			# from simulation
    │ 	 ├── DAISM_model.pkl 	# from training
    │ 	 ├── DAISM_model_celltypes			# from training
    │ 	 ├── output/DAISM_model_feature.txt 	# from training
    ├──  final result     
    │ 	 └── *.txt			# The final prediction results in txt but Schelker datasets could not get the final results 
</details>
<details><summary>data</summary>
    
    ├── data
    │        ├── Schelker_scRNA_updated.tsv
    │        ├── trainp1p2.tsv		
    │        ├── trainp1p3.tsv			
    │        ├── trainp2p3.tsv	 	
    │        ├── bulk-schelker.tsv
    │        ├── bulkp1.tsv		
    │        ├── bulkp2.tsv		
    │	     └── bulkp3.tsv 
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
source $HOME/jupyter_py3/bin/activate
~~~
4. before we run the .sh files, we use in the following commands in to install some packages needed for the task
~~~
apt-get update (recommended)
apt-get install less (recommended)
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda  (recommended)
conda install argh  (recommended)
conda install anndata  (recommended)
conda install scikit-learn  (recommended)
pip install scanpy  (essential)
pip install tqdm   (essential)
pip install daism   (essential)
~~~

---

## Running files (estimated time per job)


<details><summary>1. create_h5ad.py	 (10 min)</summary>

- read annotation and Sc_RNAseq;

    - match the celltypes bewteen annotation and Sc_RNAseq;

    - build purified.h5ad;


 </details>
 
 ~~~
    sbatch ./sh/create_h5ad.sh
~~~


<details><summary>2.daism.py Generic_simulation (50 min)</summary>

- read the purified.h5ad;


</details>

~~~
    sbatch ./sh/simulation.sh
~~~


<details><summary>2.daism.py Generic_training (40 min)</summary>

- read the outputs of simulation module;

- split data to train, test and DAISM model;


</details>

~~~
    sbatch ./sh/training.sh
~~~

<details><summary>2.daism.py Generic_prediction </summary>

- read in the outputs of training moduel and test.txt;

- predict the estimated proportion;


</details>

~~~
    sbatch ./sh/prediction.sh
~~~




