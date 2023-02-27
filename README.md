# Distributed computing with Python and MPI

An introduction into using MPI in the Python programming language to run complex computations on a cluster.

## Session description
Most modern programming libraries for computational work make it easy to parallelize your code and thus leverage the power of all CPU cores on your machine. But what if even that is not enough? How can we truly unleash the power of a High Performance Cluster like Dartmouth’s Discovery and use hundreds of CPUs distributed across multiple nodes?

The answer: MPI. MPI is a standard for a Message-Passing Interface that is implemented in various libraries. It allows several nodes within a cluster to communicate. By sending status messages and data back and forth between nodes, the computational load can be distributed across any number of available nodes.

In this session, we will introduce MPI in Python covering basic concepts, one-to-one, one-to-many, many-to-one communications, and we will close out with a few notes on pitfalls and good practices.

## Getting started

### Requirements
You should have a good understanding of the fundamentals of programming in Python to get the most out of these materials.

If you want to run the examples on Dartmouth's Discovery cluster, you need a [Research Computing account](https://rc.dartmouth.edu/index.php/discovery-overview/accessing-the-cluster/https://rc.dartmouth.edu/index.php/discovery-overview/accessing-the-cluster/).

### Install
> The materials assume that you will run this on Discovery. You can certainly run them on your local computer, but setting up an MPI environment locally is not part of this tutorial.

See the slide deck in the folder `ppt` for instructions on how to get set up using MPI on Discovery.

### Usage
The repo has the following structure:
- `jobs`: SLURM job files for each example
- `out`: Output files will end up here
- `ppt`: The slide deck with instructions and explanations
- `src`: Python scripts for the examples

### Issues and feedback
If you run into any trouble working with these materials, have some questions about the content, or want to give general feedback, feel free to go through one of these channels to get in touch with us:
- [Open a new issue](https://git.dartmouth.edu/lib-digital-strategies/RDS/workshops/infrastructure/distributed-computing-with-python-and-mpi/-/issues)
- [Send an email](mailto:simon.stone@dartmouth.edu)
- [Book an appointment](https://dartgo.org/meetwithsimon) (Dartmouth-members only)

### Licensing
<table>
<tbody>
  <tr>
    <td style="padding:0px;border-width:0px;vertical-align:center">
    Instructional materials created by Simon Stone for Dartmouth College Library under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons CC BY-NC 4.0 License</a>.
    </td>
    <td style="padding:0 0 0 1em;border-width:0px;vertical-align:center"><img alt="Creative Commons License" src="https://i.creativecommons.org/l/by/4.0/88x31.png"/></td>
  </tr>
</tbody>
</table>

Except where otherwise noted, the example programs are made available under the OSI-approved MIT license.

