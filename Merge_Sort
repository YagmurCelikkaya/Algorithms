# Heap Sort algorithm with given python list
def heapify(array, l, i):
    largest = i         # Initialize largest as root
    left = 2 * i + 1     # Left child
    right = 2 * i + 2    # Right child

    # If left child is larger than root
    if left < l and array[left] > array[largest]:
        largest = left

    # If right child is larger than current largest
    if right < l and array[right] > array[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # Swap
        heapify(array, l, largest)  # Recursively heapify the affected subtree

def heap_sort(array):
    l = len(array)

    # Build a max heap
    for i in range(l // 2 - 1, -1, -1):
        heapify(array, l, i)

    # Extract elements from heap one by one
    for i in range(l - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # Swap
        heapify(array, i, 0)

mylist = [12, 11, 13, 5, 6, 7]
heap_sort(mylist)
print("Sorted array is:", mylist)
