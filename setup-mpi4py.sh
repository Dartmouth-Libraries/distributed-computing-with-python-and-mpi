#!/bin/bash

module load openmpi/4.1.2

source /optnfs/common/miniconda3/etc/profile.d/conda.sh

conda create --name mpi-env python=3.8 -y
conda activate mpi-env

pip install mpi4py --no-cache-dir