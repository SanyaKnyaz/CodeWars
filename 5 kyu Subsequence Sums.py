'''
Subsequence Sums
https://www.codewars.com/kata/60df63c6ce1e7b0023d4af5c
'''
def subsequence_sums(arr, s):
    running_sum = 0
    prev_sums = {} 
    arr = [0]+arr
    count = 0
    for n in arr:
        running_sum += n
        if running_sum - s in prev_sums:
            count += prev_sums[running_sum - s]
        prev_sums[running_sum] = prev_sums.get(running_sum, 0) + 1
    return count