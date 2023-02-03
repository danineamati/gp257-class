# slurm



## Getting started


Open up Chrome Remote Desktop

Begin by logging into one of the development nodes and forward X11 graphics

srun --pty --x11 /bin/bash

Next load python 3.10

If you haven't setup spack yet run 

. ~/../spack/spack/share/spack/setup-env.sh

Next clone the repository

git clone http://zapad.stanford.edu/GP257/labs-2023/slurm.git

Finally open up a jupyter lab inside the respoitory

cd slurm

jupyter lab notebook.ipynb