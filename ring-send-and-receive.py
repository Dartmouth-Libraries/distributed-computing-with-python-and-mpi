"""
This program passes an object around in a ring using blocking sending and receiving
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
max_rank = comm.size - 1

data = 0

for i in range(5):
    if rank == 0:
        if data == 0:
            sender = None
        else:
            sender = max_rank
        receiver = rank+1
    elif rank == max_rank:
        sender = rank-1
        receiver = 0
    else:
        sender = rank-1
        receiver = rank+1

    if sender is not None:
        data = comm.recv(source=sender)
    data += 1
    print(f'I am {rank=} and I am sending {data=} to rank {receiver}!')
    comm.send(data, dest=receiver)
