# Import the mpi4py module (internally calls MPI_Init())
from mpi4py import MPI

# Get a handle of the `World` communicator
comm = MPI.COMM_WORLD

# Obtain the rank of this process in the `World` communicator
rank = comm.Get_rank()

print(f'Hello, world! I am rank {rank}!')
