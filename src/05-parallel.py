"""
This program showcases the use of MPI (node-level parallelism) and  (cpu-level parallelism)
"""
from mpi4py import MPI
import numpy as np

from multiprocessing import Pool
import os
import time


comm = MPI.COMM_WORLD
rank = comm.Get_rank()


def cpu_count():
    return int(os.environ['SLURM_CPUS_PER_TASK'])


def node_count():
    return comm.size


def something_taking_1ms(value):
    """ A dummy function that takes about 1 millisecond to run"""
    start = time.perf_counter()
    while (time.perf_counter() - start) < 0.001:
        continue
    return value


def something_that_takes_a_long_time(arr, n_workers):
    """
    This does something that individually takes 1 millisecond
    in parallel using CPU-level parallelism
    """
    with Pool(n_workers) as p:
        result = p.map(something_taking_1ms, arr)
    return result


def run(data, use_nodes, n_cpus):
    n_nodes = node_count() if use_nodes else 1

    if use_nodes:
        if rank == 0:
            data = np.array_split(data, n_nodes)

        data = comm.scatter(data, root=0)

    if use_nodes or rank == 0:
        data = something_that_takes_a_long_time(data, n_cpus)

    if use_nodes:
        data = comm.gather(data, root=0)


if __name__ == "__main__":
    array_size = 40_000

    data = None
    if rank == 0:
        data = [x for x in range(array_size)]

    """ Single CPU """
    if rank == 0:
        start = time.perf_counter()

    run(data=data, use_nodes=False, n_cpus=1)

    if rank == 0:
        end = time.perf_counter()

        single_cpu_runtime = end - start
        print(f'The program ran in {single_cpu_runtime} seconds using 1 node'
              f' with 1 CPU.')

    comm.barrier()

    """ Single node, multiple CPUs"""
    if rank == 0:
        start = time.perf_counter()
    run(data=data, use_nodes=False, n_cpus=cpu_count())

    if rank == 0:
        end = time.perf_counter()

        multi_cpu_runtime = end - start
        print(f'The program ran in {multi_cpu_runtime} seconds using 1 node'
              f' with {cpu_count()} CPUs.')

        print(f"The speedup of multi CPU over single CPU is "
              f"{single_cpu_runtime / multi_cpu_runtime:.2f}. "
              f"Ideal speedup is {cpu_count()}")

    comm.barrier()

    """ Multiple nodes, multiple CPUs """
    if rank == 0:
        start = time.perf_counter()

    run(data=data, use_nodes=True, n_cpus=cpu_count())

    if rank == 0:
        end = time.perf_counter()

        multi_node_runtime = end - start

        print(f'The program ran in {multi_node_runtime} seconds '
              f'using {node_count()} nodes '
              f'with {cpu_count()} CPUs each.')
        print(f"The speedup of multi node over single node, multi CPU is "
              f"{multi_cpu_runtime / multi_node_runtime:.2f}. "
              f"Ideal speedup is {node_count()}.")
        print(f"The speedup of multi node over single node, single CPU is "
              f"{single_cpu_runtime / multi_node_runtime:.2f}. "
              f"Ideal speedup is {node_count() * cpu_count()}.")

    comm.barrier()
