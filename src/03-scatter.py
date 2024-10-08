"""
This program scatters an array across nodes
"""
from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    print(f'I am process {rank} and I am preparing to scatter an array '
          f'of size={size * 3 + 1} across {size} processes.')
    data = [i for i in range(size * 3 + 1)]
    # The number of elements in 'data' has to match the number of receiving processes
    # We therefore slice the list into 'size' (not necessarily equally long) slices
    data = np.array_split(data, size)
else:
    data = None

print(f'I am process {rank} and before the scatter I have {data=}.')
data = comm.scatter(data, root=0)
print(f'I am process {rank} and after the scatter I have {data=}.')
