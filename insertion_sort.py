def insertionSort1(n, arr):
    value = arr[n - 1]      # Store last element
    i = n - 2               # Start from element before last

    # Shift elements greater than value to the right
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1

    # Insert the value at correct position
    arr[i + 1] = value
    print(*arr)