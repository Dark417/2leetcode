"""
1351. Count Negative Numbers in a Sorted Matrix
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.



Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100




pseudo-code
1. brute force

2. binary search


"""
input0 = [[1, -1], [-1, -1]]


# D binary search
def bs(matrix):
    num = 0








    return num



# D bf
def num_neg(matrix):
    num = 0
    for i in matrix:
        for j in i:
            if j < 0:
                num += 1


    return num


res = num_neg(input0)
print(res)















