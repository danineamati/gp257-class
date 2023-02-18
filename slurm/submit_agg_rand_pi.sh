#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --partition=preempt
#SBATCH --time=0-00:20:00
#SBATCH --mem=1000
#SBATCH --cpus-per-task=1
#SBATCH --requeue
#SBATCH --job-name=rand_pi
#SBATCH --dependency=singleton

spack load python@3.10.8
python3 ./aggregate_rand_pi.py
