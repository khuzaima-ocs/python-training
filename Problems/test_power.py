from time import time
import power_function
import power_optimized

n_start = time()
n_res = power_function.power(98723213213214124, 991)
n_end = time()

lgn_start = time()
lgn_res = power_optimized.power(98723213213214124, 991)
lgn_end = time()

print(f"O(N) power function took {n_end - n_start} seconds to execute")
print(f"O(lgN) power function took {lgn_end - lgn_start} seconds to execute")