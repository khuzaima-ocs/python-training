import main
import time

start_v = time.time()
main.prime_finder_vanilla(30000)
end_v = time.time()

print(f"Vanilla version took {end_v - start_v} seconds")

start_c = time.time()
main.prime_finder_optimized(30000)
end_c = time.time()

print(f"Optimized version took {end_c - start_c} seconds")



