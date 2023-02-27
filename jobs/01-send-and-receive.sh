#!/bin/bash

#SBATCH --job-name="sndrcv"
#SBATCH --time=00:05:00
#SBATCH --output=../out/01-send-and-receive-%j.out
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=100M

module load openmpi/4.1.2

source /optnfs/common/miniconda3/etc/profile.d/conda.sh
conda activate mpi-env

mpiexec -np 2 python ../src/01-send-and-receive.py --mca mpi_cuda_support 0
