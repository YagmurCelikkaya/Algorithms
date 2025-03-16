#  Sorting Algorithms

Thre are two types of sorting algorithms 

1. **Comparison-based Sorting** : Bubble Sort, Merge Sort
2. **Non-comparison-based Sorting** : Counting Sort

---

##  Comparison-Based Sorting

### 1️ Bubble Sort
- **Time Complexity:** \( O(n^2) \) (Worst and Average), 
                        \( O(n) \) (Best case if already sorted)
- **Space Complexity:** \( O(1) \) (in-place sorting)

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

##  Non-Comparison Sorting

###  Counting Sort
- **Time Complexity:** \( O(n + k) \), where \( k \) is the range of input values.
- **Space Complexity:** \( O(n + k) \) (uses extra space for frequency count).

####  How It Works:
1. Find the **maximum value** in the array.
2. Create a **count array** to store occurrences.
3. Compute **cumulative sums** to determine positions.
4. Build the **sorted array** using the count array.

####  Example Table:

| Index | Before | Cumulative Count |
|--------|---------|----------------|
| 1      | 1       | 1              |
| 2      | 2       | 3              |
| 3      | 2       | 5              |
| 4      | 1       | 6              |
| 5      | 0       | 6              |
| 6      | 0       | 6              |
| 7      | 0       | 6              |
| 8      | 1       | 7              |

---
