# Sorting
Sorting is one of the most commonly seen problems in both daily coding practise and interview problems.
In the post, we will walk through some different sorting methods to have a better understanding of the algorithms.

In further applications, it is important to understand the features of the data given before deciding which sorting method to use.

## Useful resources:
- [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)
> Animations of different sorting methods can be found here to help us better understand the sorting processes.

## Introduction
### Term Explanation
- Stability
    For `a = b` and `a` is originally in front of `b`:
        stable: if `a` is still in front of `b` after sorting
        unstable: `a` may be appear after `b` after sorting

### Complexity Summarise
| Algorithm      | Average    | Worst      | Best       | Space Complexity | Stability|
|:--------------:|:----------:|:----------:|:----------:| :-------:| --------|
| Bubble Sort    | O(N^2)     | O(N^2)     | O(N)       | O(1)     | stable  |
| Selection Sort | O(N^2)     | O(N^2)     | O(N^2)     | O(1)     | unstable|
| Insertion Sort | O(N^2)     | O(N^2)     | O(N)       | O(1)     | stable  |
| Merge Sort     | O(Nlog(N)) | O(Nlog(N)) | O(Nlog(N)) | O(N)     | stable  |
| Quick Sort     | O(Nlog(N)) | O(Nlog(N)) | O(N^2)     | O(log(N) | unstable|
| Heap Sort      | O(Nlog(N)) | O(Nlog(N)) | O(Nlog(N)) | O(1)     | unstable|


## Bubble Sort
Traverse though the array repeatedly and compare two elements a time. Swap them if they are in the wrong order until all the elements are sorted.
It is named as bubble sort because the smallest element will gradually raise up to the top of the array like a bubble

### Code implementation
```python
def bubble_sort(nums: [int]) -> [int]:
    n = len(nums)
    for i in range(n):
        for j in range(n - 1):
            # compare two neighbour elements
            if nums[j+1] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[i]
    return nums
```
Time Complexity: O(N^2)

Space Complexity O(1)

## Selection Sort
Select the smallest element in the unsorted part and move it the the end of the sorted part.

### Code implementation
```python
def selection_sort(nums: [int]) -> [int]:
    n = len(nums)
    for i in range(n):
        min_index = i # record the position of the smallest element
        for j in range(i,n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
```
Time Complexity: O(N^2)

Space Complexity O(1)

## Insertion Sort
Insert element from unsorted part into the sorted array from tail.

### Code implementation

```python
def insertion_sort(nums: [int]) -> [int]:
    n = len(nums)
    for i in range(1,n):
        num = nums[i] # temporarily store the element
        j = i
        while j > 0 and nums[j-1] > num:
            nums[j] = nums[j-1] # move backward the sorted part
            j -= 1
        nums[j] = num # insertion
        
    return nums
```
> We can optimise the method for inserting the element into the sorted part.
> Here we temporarily store the value and find the correct position to insert, instead of swapping step by step.

Time Complexity: O(N^2) (Best reach O(N) when original array is close to sorted.)

Space Complexity O(1)

### Insertion sort linked list
Example: [LeetCode 0147: Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)
> Sort a linked list using insertion sort.
#### Code implementation
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertion_sort_list(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        cur, nxt = head, head.next 
        # create a dummy head
        dummy = ListNode(float('-inf'))
        dummy.next = head # point to head for later return

        while nxt:
            # both pointer move forward if in order
            if nxt.val >= cur.val: 
                cur = nxt
                nxt = nxt.next
            else: # insert to the right position
                cur.next = nxt.next # break the link
                # find the insert position
                pre1, pre2 = dummy, dummy.next
                while nxt.val > pre2.val:
                    pre1 = pre2
                    pre2 = pre2.next
                # insert
                pre1.next = nxt
                nxt.next = pre2
                # move pointer back to the start of next loop
                nxt = cur.next

        return dummy.next
```
> Note:
> 1. Create dummy head for making head node no longer special.
> 2. Traverse through the linked list with pointers
> 3. When insertion required, traverse from the head to find the right position to insert.

## Merge Sort
Merge sort is a classic implementation of the divide and Conquer method as well as recursion.
It merges sorted subsets to obtain the overall sorted array.

Compare with selection sort, merge sort has better time complexity performance in return for a O(N) spacce complexity.

### Code implementation
```python
def merge(left: [int], right: [int]) -> [int]:
    """Given two sorted sub-arrays, merge them into one sorted array."""
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


def merge_sort(nums: [int]) -> [int]:
    n = len(nums)
    if n <= 1:
        return nums

    # divide into two sub-arrays
    mid = n // 2
    left = merge_sort[:mid]
    right = merge_sort[mid:]

    return merge(left, right)
```
Time Complexity: O(Nlog(N))

Space Complexity O(N)

## Quick Sort
Choose a `pivot` and put everything smaller than it to its left, larger to its right to set the final position for this `pivot`.
> 1. Choose a pivot element
> 2. Partition: divide the array into two sections based on the pivot value.
> 3. Recursion for each section.

### Code implementation
```python
def quick_sort(nums: [int]) -> [int]:
    n = len(nums)
    
    def quick(left, right):
        if left >= right:
            return nums

        pivot = left
        i, j = left, right

        while i < j:
            # partition
            while i < j and nums[j] > nums[pivot]:
                j -= 1

            while i < j and nums[i] <= nums[pivot]:
                i += 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[pivot], nums[j] = nums[j], nums[pivot]

        quick(left, j-1)
        quick(j+1, right)

        return nums

    return quick(0, n-1)
```
Time Complexity: O(Nlog(N))

Space Complexity O(logN)

> Avoiding worst scenario 
> For special test case (e.g. ordered list or reversed ordered list), randomly choose the pivot, otherwise the time complexity is nearly the same as a selection sort.

### Further implementation of Partition
[LeetCode0215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
> Find the kth largest element in an unsorted array. 
> 
> Note that it is the kth largest element in the sorted order, not the kth distinct element

#### Code implementation
```python
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        target = n - k # target position
        left, right = 0, n - 1

        while True:
            index = self.partition(nums, left, right)

            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1 # next search area [index + 1, right]
            else:
                right = index - 1 # [left, index - 1]

    def partition(self, nums, left, right):
        """
            [left + 1, j] < pivot
            [j+1, i] >= pivot
        """
        pivot = nums[left]
        j = left

        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                # elements smaller than pivot goes to the front
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
        # satisfied [left, j - 1] < pivot, nums[j] = pivot, [j + 1, right] >= pivot
        nums[left], nums[j] = nums[j], nums[left]

        return j
```

> Reference:
> 1. https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
> 2. https://blog.csdn.net/MobiusStrip/article/details/83785159?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task%E4%BD%9C%E8%80%85%EF%BC%9Apowcai%E9%93%BE%E6%8E%A5%EF%BC%9Ahttps://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/%E6%9D%A5%E6%BA%90%EF%BC%9A%E5%8A%9B%E6%89%A3%EF%BC%88LeetCode%EF%BC%89%E8%91%97%E4%BD%9C%E6%9D%83%E5%BD%92%E4%BD%9C%E8%80%85%E6%89%80%E6%9C%89%E3%80%82%E5%95%86%E4%B8%9A%E8%BD%AC%E8%BD%BD%E8%AF%B7%E8%81%94%E7%B3%BB%E4%BD%9C%E8%80%85%E8%8E%B7%E5%BE%97%E6%8E%88%E6%9D%83%EF%BC%8C%E9%9D%9E%E5%95%86%E4%B8%9A%E8%BD%AC%E8%BD%BD%E8%AF%B7%E6%B3%A8%E6%98%8E%E5%87%BA%E5%A4%84%E3%80%82
> 














