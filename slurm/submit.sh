#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --partition=preempt
#SBATCH --time=0-02:00:00
#SBATCH --mem=1000
#SBATCH --cpus-per-task=1

spack load python
python3 ./leib.py
