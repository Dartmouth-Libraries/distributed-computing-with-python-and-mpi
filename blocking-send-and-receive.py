"""
This program showcases a blocking send and receive
"""
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'Dartmouth': 1769}
    sleep_s = 5
    print(f'I am {rank=} and about to send {data=} in {sleep_s} seconds.')
    time.sleep(5)
    comm.send(data, dest=1, tag=11)

if rank == 1:
    start = time.time()
    data = comm.recv(source=0, tag=11)
    end = time.time()
    print(f'I am {rank=} and have received {data=}')
    print(f'I waited {end-start} seconds for the data.')

print(f"I am {rank=} and I am done.")
