#!/bin/bash

#SBATCH --job-name="gather"
#SBATCH --time=00:05:00
#SBATCH --output=../out/04-gather-%j.out
#SBATCH --nodes=20
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=100M

module load openmpi/4.1.2

source /optnfs/common/miniconda3/etc/profile.d/conda.sh
conda activate mpi-env

mpiexec -np 20 python ../src/04-gather.py --mca mpi_cuda_support 0

