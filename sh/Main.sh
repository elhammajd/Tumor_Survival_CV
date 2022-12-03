#!/bin/bash
#SBATCH --account=def-ubcxzh
#SBATCH --output=./rout/%x-%j.out
#SBATCH --cpus-per-task=5
#SBATCH --mail-user=elhmajd@gmail.com
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --mail-type=REQUEUE
#SBATCH --mail-type=ALL
#SBATCH --ntasks=6  
#SBATCH --mem-per-cpu=32G # 2GiB of memery 
#SBATCH -t 03-10:00
python -u ./Scripts/Main_M1.py;
python -u ./Scripts/Main_M2.py




