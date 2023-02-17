#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --partition=preempt
#SBATCH --time=0-00:02:00
#SBATCH --mem=10mb
#SBATCH --cpus-per-task=1
#SBATCH --array=10
#SBATCH --requeue

spack load python@3.10.8
python3 ./rand_pi.py
