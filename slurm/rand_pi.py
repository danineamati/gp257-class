#!/usr/bin/env python3

import numpy as np
import os

def partial_rand_pi(num_samples: int, seed) -> float:
    """
    Second way of computing Pi:
    1. Sample 2 numbers
    2. Sum numbers in 1.
    3. Check if Sum in 2. is <=1
    4. Total that pass 3. * 4 = Pi
    """
    # Set the seed for the run
    assert isinstance(seed, int)
    np.random.seed(seed)
    
    # Use numpy to get all the random numbers 
    # (i.e., 2D arrays with 2 x num_samples)
    # Square all the numbers
    # Then, sum across the pairs axis
    sums_arr = np.sum(np.random.random((2, num_samples)) ** 2, axis = 0)
    assert sums_arr.shape == (num_samples,)
    
    # Check the ones that pass
    num_passed = np.sum(sums_arr <= 1)
    
    # Calculate the ratio
    ratio = num_passed / num_samples
    
    # Return the approximation to Pi
    return 4 * ratio
    

if __name__ == "__main__":
    verbose = False 
    
    if verbose:
        print("Using Numpy Version: " + str(np.version.version))
    
    # Get SLURM Array Task ID
    try:
        slurm_array_task_id = int(os.environ['SLURM_ARRAY_TASK_ID'])
        seed_val = slurm_array_task_id 
    except KeyError:
        print("Could not acquire SLURM_ARRAY_TASK_ID, using default seed")
        slurm_array_task_id = None
        seed_val = 0
    except TypeError as e:
        print(f"SLURM_ARRAY_TASK_ID could not be converted to an int: {slurm_array_task_id}")
        raise(e)
        
    
    if verbose:
        print(f"Using seed_val: {seed_val}")
    
    num_samps = 1000
    
    pi_approx = partial_rand_pi(num_samps, seed_val)
    if verbose:
        print(f"Approximation to Pi with {num_samps} samples is {pi_approx}.")
    
    # Determine Filename
    if slurm_array_task_id is None:
        fname = 'rand_results/result_rand_pi_test.txt'
    else:
        fname = f'rand_results/result_{slurm_array_task_id}.txt'
    
    # Write Result to File
    f = open(fname, 'w')
    f.write(str(pi_approx))
    f.close()
