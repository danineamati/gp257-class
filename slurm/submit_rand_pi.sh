#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --partition=preempt
#SBATCH --time=0-00:20:00
#SBATCH --mem=1000
#SBATCH --cpus-per-task=1
#SBATCH --array=0-1000
#SBATCH --requeue
#SBATCH --job-name=rand_pi

spack load python@3.10.8
python3 ./rand_pi.py
