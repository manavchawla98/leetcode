# Max sum of k consecutive elements in arr
def max_sum(arr, k):
    max_sum = 0
    for i in range(k):
        max_sum += arr[i]

    for i in range(k, len(arr)-1):
        max_sum = max(max_sum, max_sum - arr[i-k] + arr[i])

    return max_sum


s = max_sum([100,200,300,300,400,100], 2)
print(s)

