#!/bin/bash
#SBATCH --job-name=SingleCoreTest
#SBATCH --account=<project>
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --partition=test

module load geoconda
srun python single_core_example.py /appl/data/geo/sentinel/s2_example_data/L2A