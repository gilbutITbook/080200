def permutation(arr, start):
    if len(arr)-1 == start:
        print(arr)
        return

    for idx in range(start, len(arr)):
        arr[start], arr[idx] = arr[idx], arr[start]
        permutation(arr, start+1)
        arr[start], arr[idx] = arr[idx], arr[start]

if __name__=="__main__":
    arr=[1, 2, 3]
    permutation(arr, 0)

