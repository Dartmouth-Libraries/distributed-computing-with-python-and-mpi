#!/bin/bash

#SBATCH --job-name="mpi4py"
#SBATCH --time=00:05:00
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=100M

module load openmpi
source /optnfs/common/miniconda3/etc/profile.d/conda.sh
conda activate genpurp

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

mpiexec -n 8 python parallel.py
