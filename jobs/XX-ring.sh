#!/bin/bash

#SBATCH --job-name="mpi-ring"
#SBATCH --output=../out/XX-ring-%j.out
#SBATCH --time=00:05:00
#SBATCH --nodes=20
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=100M
#SBATCH --exclude=k19


module load openmpi/4.2.1

source /optnfs/common/miniconda3/etc/profile.d/conda.sh
conda activate mpi-env

mpiexec -n 20 python ../src/XX-ring.py
