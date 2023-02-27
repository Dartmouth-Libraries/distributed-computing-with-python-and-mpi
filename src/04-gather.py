"""
This program gathers data from all processes
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = rank
data = comm.gather(data, root=0)
print(f'I am process {rank} and my data is {data=}.')