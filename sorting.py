# All sorting algorithms

# time: average O(n^2), best O(n), worst O(n^2) 
# space O(1), in-place, stable
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Optimization: stopping the algorithm if no swap in one inner loop
        if swapped == False:
            break


# time: average O(n^2), best O(n^2), worst O(n^2) 
# space O(1), in-place, unstable
def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# time: average O(n^2), best O(n), worst O(n^2) 
# space O(1), in-place, stable
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# time: average O(nlogn), best O(nlogn), worst O(nlogn)
# space: O(n), not in-place, stable
def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m+1]
    R = arr[m+1:r+1]
    i, j, k = 0, 0, l
    while (i < n1 and j < n2):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while (i < n1):
        arr[k] = L[i]
        i += 1
        k += 1
    while (j < n2):
        arr[k] = R[j]
        j += 1
        k += 1


# time: average O(nlogn), best O(nlogn), worst O(n^2)
# space: O(logn) stack frames, in-place, unstable
def quickSort(arr, l, r):
    if l < r:
        pivot = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        quickSort(arr, l, i - 1)
        quickSort(arr, i + 1, r)


# time: average O(nlogn), best O(n), worst O(nlogn)
# space: O(1), in-place, unstable
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapify(arr, i, 0)  # pay attention to the heap size

def maxHeapify(arr, size, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < size and arr[l] > arr[largest]:
        largest = l
    if r < size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, size, largest)


# assume that the input consists of integers in a small range
# time: O(n+k); O(n) if k = O(n)
# space: O(n+k), not in-place, stable
def countSort(arr):
    mi = min(arr)
    ma = max(arr)
    k = ma - mi + 1
    n = len(arr)
    count = [0] * k
    output = [0] * n
    for i in range(n):
        count[arr[i] - mi] += 1
    for i in range(1, k):
        count[i] = count[i - 1] + count[i]
    for i in range(n-1, -1, -1):
        output[count[arr[i] - mi] - 1] = arr[i]
        count[arr[i] - mi] -= 1
    for i in range(n):
        arr[i] = output[i]


# assume that the input consists of d-digit integers
# time: O(d(n+k)); O(n) if d is fixed and k = O(n)
# space: O(n+k), not in-place, stable 
def radixSort(arr):    
    ma = max(arr) # Find the maximum number to know number of digits 
    exp = 1
    while ma // exp > 0: 
        countSort2(arr, exp) 
        exp *= 10

def countSort2(arr, exp):
    n = len(arr)
    count = [0] * 10
    output = [0] * n
    for i in range(n):
        digit = arr[i] // exp % 10
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n-1, -1, -1):
        digit = arr[i] // exp % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    for i in range(n):
        arr[i] = output[i]


# assume that the input is drawn from a uniform distribution over [0, 1)
# time: average O(n), best O(n), worst O(n^2)
# space: O(n), not in-place, stable 
def bucketSort(arr):
    n = len(arr)
    buckets = []
    for i in range(n):
        buckets.append([])
    for i in range(n):
        buckets[int(n*arr[i])].append(arr[i])
    for i in range(n):
        insertionSort(buckets[i])
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1


array = [2, 5, 1, 8, 4, 3, 7, 8, 6, -1, 5]
bubbleSort(array)
print("bubble sort:", array)

array = [2, 5, 1, 8, 4, 3, 7, 8, 6, -1, 5]
selectionSort(array)
print("selection sort:", array)

array = [2, 5, 1, 8, 4, 3, 7, 8, 6, -1, 5]
insertionSort(array)
print("insertion sort:", array)

array = [2, 5, 1, 8, 4, 3, 7, 8, 6, -1, 5]
mergeSort(array, 0, len(array) - 1)
print("merge sort:", array)

array = [2, 5, 1, 8, 4, 3, 7, 8, 6, -1, 5]
quickSort(array, 0, len(array) - 1)
print("quick sort:", array)

array = [2, 5, 1, 8, 4, 3, 7, 8, 6, -1, 5]
heapSort(array)
print("heap sort:", array)

array = [2, 5, 1, 8, 4, 3, 7, 8, 6, -1, 5]
countSort(array)
print("count sort:", array)

array = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(array)
print("radix sort:", array)

array = [0.897, 0.665, 0.656, 0.1234, 0.565, 0.3434]
bucketSort(array)
print("bucket sort:", array)