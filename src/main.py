from solve import *
from plot import *
import time as t
import solve


n = int(input("Input the number of points ( > 1) = "))
while (n <= 1):
    print("Number of points must be greater than 1")
    n = int(input("Input the number of points ( > 1) = "))

dim = int(input("Input dimension ( > 0) = "))
while (dim <= 0):
    print("Dimension must be greater than 0")
    dim = int(input("Input dimension ( > 0) = "))

x = np.random.uniform(-1000.0, 1000.0, (n, dim))

tic = t.perf_counter()
minima, min_pair_bf = brute_force(x)
toc = t.perf_counter()
print("\n==================BRUTE FORCE===================")
print(f"Point 1                     : {min_pair_bf[0]}")
print(f"Point 2                     : {min_pair_bf[1]}")
print(f"Minimum distance            : {minima}")
print(f"Euclidean distance counter  : {solve.calc_step}")
print(f"Computation time            : {toc-tic}s")

# Reset euclidean distance counter
solve.calc_step = 0
tic = t.perf_counter()
quick_sort(x, 0, x.shape[0] - 1, 0)
minima, min_pair_dnc = presorted_divide_and_conquer(x)
toc = t.perf_counter()
print("\n===============DIVIDE AND CONQUER================")
print(f"Point 1                    : {min_pair_dnc[0]}")
print(f"Point 2                    : {min_pair_dnc[1]}")
print(f"Minimum distance           : {minima}")
print(f"Euclidean distance counter : {solve.calc_step}")
print(f"Computation time           : {toc-tic}s")

if(x.shape[1] == 3):
    vis_valid = input("Visualize the result? (y/n)")
    while vis_valid != "y" and vis_valid != "n":
        print("Input not valid, please choose between y/n")
        vis_valid = input("Visualize the result? (y/n)")
    
    if vis_valid == "y":
        visualize3D(x, min_pair_dnc)