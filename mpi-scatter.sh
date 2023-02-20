#!/bin/bash

#SBATCH --job-name="mpi4py"
#SBATCH --time=00:05:00
#SBATCH --nodes=20
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=100M

module load openmpi
source /optnfs/common/miniconda3/etc/profile.d/conda.sh
conda activate genpurp

mpiexec -n 20 python scatter.py
