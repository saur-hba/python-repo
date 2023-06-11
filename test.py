def frequency(arr):
    n = len(arr)
    freq_count = {}
    for i in range(n):
        if arr[i] in freq_count:
         freq_count[arr[i]] += 1
        else:
            freq_count[arr[i]] = 1

    for count in freq_count:
       if freq_count[count] == n//4:
        return count