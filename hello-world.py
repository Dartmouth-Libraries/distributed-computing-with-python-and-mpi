from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(f'I am rank {rank}!')
if rank == 0:    
    data = {'a': 7, 'b': 3.14}
    print(f'I am sending {data=}')
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print(f'I have received {data=}')
