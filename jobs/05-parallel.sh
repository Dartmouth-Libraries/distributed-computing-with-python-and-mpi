#!/bin/bash

#SBATCH --job-name="mpi+mp"
#SBATCH --time=00:05:00
#SBATCH --output=../out/05-parallel-%j.out
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=100M

module load openmpi/4.1.2

source /optnfs/common/miniconda3/etc/profile.d/conda.sh
conda activate mpi-env

mpiexec -np 8 python ../src/05-parallel.py --mca mpi_cuda_support 0
