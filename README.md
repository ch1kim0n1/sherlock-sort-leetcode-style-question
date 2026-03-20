# Sherlock Sort (Adaptive Segment-Based Sorting)

## Problem - Difficulty: HARD

Given an integer array `nums`, sort the array in ascending order.

Instead of using a single standard sorting algorithm, implement an adaptive sorting strategy that:

1. Detects monotonic increasing subarrays (runs).
2. Chooses an appropriate sorting method for each segment based on its characteristics.
3. Merges all sorted segments efficiently into a final sorted array.

---

## Definitions

A **run** is a contiguous subarray where:
```
nums[i] <= nums[i + 1]
```

A segment is considered **counting-sort-friendly** if:
- Its size is sufficiently large
- The range of values is relatively small compared to its size

---

## Requirements

You must:

1. Scan the array and split it into runs.
2. For each run:
   - If the segment is suitable for counting sort, use it.
   - Otherwise, use a comparison-based sort.
3. Merge all sorted segments using an efficient k-way merge strategy.

---

## Function Signature

```python
def sherlockSort(nums: List[int]) -> List[int]:
```

---

## Constraints

- `1 <= nums.length <= 100000`
- `-1000000000 <= nums[i] <= 1000000000`

---

## Examples

### Example 1
```
Input:  nums = [1,2,3,10,11,12,5,2,9,1,1,1,1,1]
Output: [1,1,1,1,1,1,2,2,3,5,9,10,11,12]
```

### Example 2
```
Input:  nums = [5,4,3,2,1]
Output: [1,2,3,4,5]
```

### Example 3
```
Input:  nums = [1,2,3,4,5]
Output: [1,2,3,4,5]
```

---

## Follow-Up

- Implement the solution without using built-in sorting functions.
- Optimize the solution for arrays that are already partially sorted.
- Analyze how the number of runs affects performance.

---

## Complexity Analysis

Let `n` be the length of the array and `k` be the number of runs.

### Time Complexity
- Run detection: `O(n)`
- Segment sorting: `O(n log n)` (worst case)
- Merge phase: `O(n log k)`

Overall: `O(n log n)`

### Space Complexity
- Auxiliary storage for segments and merging: `O(n)`

---

## Hints

1. Use a linear scan to detect increasing runs.
2. Use counting sort when the value range is small relative to the segment size.
3. Use a heap-based approach for efficient k-way merging.

---

## Key Insight

This problem focuses on designing an adaptive system that leverages existing structure in the data rather than relying on a single fixed sorting strategy.

---

## Tags

Array  
Sorting  
Heap  
Divide and Conquer  
Greedy  
Design  
Advanced Algorithms
