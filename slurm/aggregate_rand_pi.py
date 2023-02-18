#!/usr/bin/env python3

import os

print('Starting Aggregation Process')

# Start the estimate at zero
pi_estimate = 0

# Start the counter at zero
num_results = 0

with os.scandir('rand_results/') as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file() and entry.name.startswith('result'):
            # We have found a valid file. Increment the counter
            num_results += 1
            
            # Open file, read the contents as a float, and then close
            results_file = open(entry, 'r')
            estimate = float(results_file.read())
            results_file.close()
            
            # print(f'Added {estimate} from {entry}')
            
            # Add it to the pi estimate
            pi_estimate += estimate

if num_results > 0:
    # Divide the pi estimate to average it out
    pi_estimate /= num_results

# print(f'Final result is {pi_estimate}')
    
# Print the results to file
fname = 'final_rand_results.txt'
f_rand_results = open(fname, 'w')
f_rand_results.write(str(pi_estimate))
f_rand_results.close()
