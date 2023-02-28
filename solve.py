import numpy as np
from sort import *
import math
calc_step = 0

# Solve by brute force
def brute_force(arr):
    # Set global variables for euclidean distance counter
    global calc_step

    # Points count
    n = np.shape(arr)[0]
    
    # Initialize minimum value and min_pair
    min = math.inf
    min_pair = None
    
    # Search for minimum distance by checking every pair
    for i in range(n - 1):
        for j in range(i + 1, n):
            calc_step += 1
            distance = np.linalg.norm(arr[i]-arr[j])
            if (min > distance):
                min = distance
                min_pair = np.array([arr[i], arr[j]])
    
    return min, min_pair

def presorted_nearest_strip(strip_left, strip_right, min_distance, min_pair):
    # Set global variables for euclidean distance counter    
    global calc_step

    # Points dimension
    strip_dim = strip_left.shape[1]
    
    # Initialize minimum distance
    the_dist = min_distance

    # Check pair of points in the strip
    for p_left in strip_left:
        for p_right in strip_right:
            
            # Initialize dim and point_valid
            dim = 0
            point_valid = True
            
            # If a pair of points have at least one component with a difference larger than min_distance, skip check
            while dim < strip_dim - 1:
                if abs(p_left[dim] - p_right[dim]) > min_distance:
                    point_valid = False
                    break
                else:
                    dim += 1
            
            # Point valid only if all components of a pair of points have difference less than min_distance
            if (point_valid):
                distance = np.linalg.norm(p_left - p_right)
                calc_step += 1
                if distance < the_dist:
                    the_dist = distance
                    min_pair = np.array([p_left, p_right])

    return the_dist, min_pair             

def presorted_divide_and_conquer(presortedX):
    # Set global variables for euclidean distance counter    
    global calc_step

    if(presortedX.shape[0] <= 3): # Base case
        return brute_force(presortedX)
    
    else: # Recurrence
        # Divide 
        # Split intu two region with the same number of points (at most 1 difference in number when the total is odd)
        arr_left = presortedX[:presortedX.shape[0] // 2]
        arr_right = presortedX[presortedX.shape[0] // 2:]

        # Get mid strip
        mid = (presortedX[presortedX.shape[0] // 2 - 1][0] + presortedX[presortedX.shape[0] // 2][0]) / 2
        
        # Conquer
        # Solve for each left and right region
        delta_left, min_pair_left = presorted_divide_and_conquer(arr_left)
        delta_right, min_pair_right = presorted_divide_and_conquer(arr_right)

        # Combine
        # Calculate minimum distance and pair from left and right section
        delta = min(delta_left, delta_right)
        min_pair_LR = min_pair_left.copy() if delta == delta_left else min_pair_right.copy()
        
        # Threshold for strip region
        threshold_left = mid - delta
        threshold_right = mid + delta
        
        # Get points in the strip region
        arr_strip_left = presortedX[(presortedX[:, 0] >= threshold_left) & (presortedX[:, 0] <= mid)]
        arr_strip_right = presortedX[(presortedX[:, 0] <= threshold_right) & (presortedX[:, 0] > mid)]

        # Calculate minimum distance and pair in the strip, and combine it with the previous minimum distance and pair
        delta_strip, min_pair_strip = presorted_nearest_strip(arr_strip_left, arr_strip_right, delta, min_pair_LR)
        return min(delta, delta_strip), min_pair_strip