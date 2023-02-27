#!/bin/bash

#SBATCH --job-name="bcast"
#SBATCH --time=00:05:00
#SBATCH --output=../out/02-broadcast-%j.out
#SBATCH --nodes=20
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=100M

module load openmpi/4.1.2

source /optnfs/common/miniconda3/etc/profile.d/conda.sh
conda activate mpi-env

mpiexec -np 20 python ../src/02-broadcast.py --mca mpi_cuda_support 0
