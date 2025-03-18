#  Sorting Algorithms

There are two types of sorting algorithms 

1. **Comparison-based Sorting** : Bubble Sort, Merge Sort, Heap Sort
2. **Non-comparison-based Sorting** : Counting Sort, Radix Sort, Bucket Sort

---

##  Comparison-Based Sorting

### 1️ Bubble Sort
- **Time Complexity:** \( O(n^2) \) (Worst and Average), 
                        \( O(n) \) (Best case if already sorted)
- **Space Complexity:** \( O(1) \) (in-place sorting)

*Bubble Sort* is the simplest sorting algorithm. This algorithm is not suitable for large data sets because its average and worst-case time complcity are quite high

####  How It Works:
1. Compare adjacent elements and swap them if they are in the wrong order.
2. Repeat the process for all elements until no swaps are needed.

####  Example Walkthrough:

Starting with the array **[8, 5, 10, 6, 4]**:

1. Compare **8 and 5**, swap → `[5, 8, 10, 6, 4]`
2. Compare **8 and 10**, no swap → `[5, 8, 10, 6, 4]`
3. Compare **10 and 6**, swap → `[5, 8, 6, 10, 4]`
4. Compare **10 and 4**, swap → `[5, 8, 6, 4, 10]`
5. Repeat the process until sorted → `[4, 5, 6, 8, 10]`


---

### 2️ Merge Sort
- **Time Complexity:** \( O(n \log n) \) (Best, Worst, and Average cases)
- **Space Complexity:** \( O(n) \) (uses extra space for merging)

####  How It Works:
1. Recursively **divide** the array into halves until each subarray has one element.
2. **Merge** the subarrays back together in sorted order.

####  Example Walkthrough:

Starting with **[8, 5, 10, 6, 4]**:

1. Split into parts → `[8, 5]`, `[10]`, `[6, 4]`
2. Sort each part → `[5, 8]`, `[10]`, `[4, 6]`
3. Merge sorted parts → `[5, 8, 10]`, `[4, 6]`
4. Merge everything → `[4, 5, 6, 8, 10]`


---

### 3 Heap Sort
- **Time Complexity:** \( O(n log n) \) (Best, Worst, and Average cases)
- **Space Complexity:** \( 0(log n) \) (in-place sorting)

*Heap Sort* is a sorting technique based on *Binary Heap Data Structure*

#### How It Works:
1. Convert the array into a **heapify tree**
2. Swap the root with the last element and re-heapify

#### Example Walkthrough:

Starting with **[9, 4, 3, 8, 10, 2, 5]**

1. Build a max heapify tree
    -  
    ```
            9
         /     \
        4       3
      /  \    /  \
     8   10  2    5
   

2. First compare the floor level **[8, 10]** and **[2, 5]**
3. Find the larger ones and compare it with the upper level and swap them too if it is larger than that ones too.
    -    
    ```
            9
         /     \
        10      5
       /  \    /  \
      8    4  2    3
    ```

4. Then compare with the top element and swap if it is needed.
    -    
    ```
            10
         /     \
         9       5
       /  \    /  \
      8    4  2    3
    ```

5. Rebuild the array with the same way we do the heapify tree, but the array will be sorted from largest to smallest.

---

##  Non-Comparison Sorting

### 1 Counting Sort
- **Time Complexity:** \( O(n + k) \), where \( k \) is the range of input values, and \(n\) is the number of elements in te input array. 
- **Space Complexity:** \( O(n + k) \) (uses extra space for frequency count).

*Counting Sort* is efficient when dealing with a small range of integers but it is not suitable for alrge-value ranges or floating-point numbers

####  How It Works:
1. Find the **maximum value** in the array.
2. Create a **count array** to store occurrences.
3. Compute **cumulative sums** to determine positions.
4. Build the **sorted array** using the count array.

####  Example Table:

Starting with **[4, 2, 2, 8, 3, 3, 1]**

index      = **[0, 1, 2, 3, 4, 5, 6, 7, 8]**

countArray = **[0, 1, 2, 2, 1, 0, 0, 0, 1]**

Cumulative Count calculate like that :
- countArray[i] = countArray[i-1] + i 

|      Index       | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  |
|     --------     |----|----|----|----|----|----|----|----|----|
|      Before      | 0  | 1  | 2  | 2  | 1  | 0  | 0  | 0  | 1  |
| Cumulative Count | 0  | 1  | 3  | 5  | 6  | 6  | 6  | 6  | 7  |

#### Placing
1. After calculating cumulative counts start placing the values based on there first indexis so the first element we are going to replace is 1.
    - Found its countArray representation and subtrack -1.
    - That number is its index number.
2. Keep subtrack -1 in every duplicated number.
    
---

### 2 Radix Sort
- **Time Complexity:** \( O(nk)\) (best, and worst cases)
- **Space Complexity:** \( O(n + k)\) 

*Radix Sort* sorts numbers digit by digit, from the least significant digit to the most significant digit.

#### How It Works:
1. Find the maximum number and its digits then, it repeats as many times as the number of digits.
2. Then compare every elements first digit and sort them in that way.
3. Repeat this proccess according to the maximum values digit and in every comparision don not forget to use the sorted array before that comparision not the original one

#### Example Walkthrough:

Starting with **[170, 45, 75, 90, 802, 24, 2, 66]**

1. (sorting by ones place)

| Original | 170 | 45 | 75 | 90 | 802| 24 | 2  | 66 |
| -------- |-----|----|----|---------|----|----|----|
|  Digits  |  0  |  5 |  5 |  0 |  2 |  4 |  2 |  6 | 
|  Sorted  | 170 | 90 | 802|  2 | 24 | 45 | 75 | 66 |

2. (sorting by tens place)

|  Current | 170 | 90 | 802| 2  | 24 | 45 | 75 | 66 |
| -------- |-----|----|----|----|----|----|----|----|
|  Digits  |  7  |  9 |  0 |  0 |  2 |  4 |  7 |  6 | 
|  Sorted  | 802 | 2  | 24 | 45 | 66 | 75 | 170| 90 |

3. (sorting by hundreds place)

|  Current | 802 | 2  | 24 | 45 | 66 | 75 | 170| 90 |
| -------- |-----|----|----|----|----|----|----|----|
|  Digits  |  8  |  0 |  0 |  0 |  0 |  0 |  1 |  0 | 
|  Sorted  |  2  | 24 | 45 | 66 | 75 | 90 | 170| 802|

Final Sorted Array:
`[2, 24, 45, 66, 75, 90, 170, 802]`
