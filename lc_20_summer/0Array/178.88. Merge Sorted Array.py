"""
178.88. Merge Sorted Array
合并两个有序数组


Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold 
additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""


nums1[:] = sorted(nums1[:m] + nums2)

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[m:] = nums2
    nums1.sort()



def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = j = 0
    l = []
    #num1 = nums1[:m]
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            l.append(nums1[i])
            i += 1
        else:
            l.append(nums2[j])
            j += 1
    while i < m:
        l.append(nums1[i])
        i += 1
    while j < n:
        l.append(nums2[j])
        j += 1
    nums1[:] = l



def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = j = 0
    l = []
    num1 = nums1[:m]
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            l.append(nums1[i])
            i += 1
        else:
            l.append(nums2[j])
            j += 1
    if i < m:
        l += nums1[i:m]
    if j < n:
        l += nums2[j:]
    nums1[:] = l



def merge(self, nums1, m, nums2, n):
    # Make a copy of nums1.
    nums1_copy = nums1[:m] 
    nums1[:] = []

    # Two get pointers for nums1_copy and nums2.
    p1 = 0 
    p2 = 0
    
    # Compare elements from nums1_copy and nums2
    # and add the smallest one into nums1.
    while p1 < m and p2 < n: 
        if nums1_copy[p1] < nums2[p2]: 
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1

    # if there are still elements to add
    if p1 < m: 
        nums1[p1 + p2:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p1 + p2:] = nums2[p2:]



def merge(self, nums1, m, nums2, n):
    # two get pointers for nums1 and nums2
    p1 = m - 1
    p2 = n - 1
    # set pointer for nums1
    p = m + n - 1

    # while there are still elements to compare
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] =  nums1[p1]
            p1 -= 1
        p -= 1

    # add missing elements from nums2
    nums1[:p2 + 1] = nums2[:p2 + 1]



def merge(self, nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]



# caikehe
def merge(self, nums1, m, nums2, n):
    l1, l2, end = m-1, n-1, m+n-1
    while l1 >= 0 and l2 >= 0:
        if nums2[l2] > nums1[l1]:
            nums1[end] = nums2[l2]
            l2 -= 1
        else:
            nums1[end] = nums1[l1]
            l1 -= 1
        end -= 1
    if l1 < 0: # if nums2 left
        nums1[:l2+1] = nums2[:l2+1]


def merge1(self, nums1, m, nums2, n):
	m, n = m-1, n-1
	while m >= 0 and n >= 0:
	    if nums1[m] > nums2[n]:
	        nums1[m+n+1] = nums1[m]
	        m -= 1
	    else:
	        nums1[m+n+1] = nums2[n]
	        n -= 1
	if n != -1: # nums2 is still left
	    nums1[:n+1] = nums2[:n+1]