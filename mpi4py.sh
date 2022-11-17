#!/bin/bash

#SBATCH --job-name="mpi4py"
#SBATCH --time=00:05:00
#SBATCH --partition=haswell64
#SBATCH --nodes=10
#SBATCH --ntasks-per-node=5
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=100M
#SBATCH --mail-user=simon.stone@dartmouth.edu
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --output=out.put

# Setup computational environment, i.e, load desired modules
# module purge
# module load <module name>



# Execute parallel application 
module load openmp
conda activate genpurp
srun mpiexec -n 50 python hello-world.py