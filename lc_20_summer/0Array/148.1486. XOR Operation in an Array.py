"""
148.1486. XOR Operation in an Array
数组异或操作


Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

 

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
Example 2:

Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
Example 3:

Input: n = 1, start = 7
Output: 7
Example 4:

Input: n = 10, start = 5
Output: 2
 

Constraints:

1 <= n <= 1000
0 <= start <= 1000
n == nums.length
"""


def xorOperation(self, n: int, start: int) -> int:
    nums = [start + 2 * i for i in range(n)]
    return functools.reduce(lambda x, y: x ^ y, nums, 0)

return functools.reduce(operator.xor, range(start, start + 2 * n, 2))




def xorOperation(self, n, start):
    res = start
    for i in range(1, n):
        res = res ^ (start + 2 * i)
    return res


def xorOperation(self, n: int, start: int) -> int:
    last = start + 2 * (n - 1)
    if start % 4 < 2:
        start = 0
    else:
        n -= 1
    if n % 2 == 0: return start ^ (n & 2)
    return start ^ last ^ (n & 2)


































