"""
This program broadcasts an object to all processes
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'Dartmouth': 1769}
else:
    data = None

print(f'I am process {rank} and my data is {data=} before the broadcast!')

# Broadcast the object from the process with rank 'root' to all other processes in the communicator
data = comm.bcast(data, root=0)

print(f'I am process {rank} and my data is {data=} after the broadcast!')