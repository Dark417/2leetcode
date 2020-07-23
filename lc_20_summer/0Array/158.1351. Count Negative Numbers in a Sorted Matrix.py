"""
158.1351. Count Negative Numbers in a Sorted Matrix
统计有序矩阵中的负数

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


"""



def countNegatives(self, grid: List[List[int]]) -> int:
    return sum(i < 0 for j in grid for i in j )


    return str(grid).count('-')

    
return sum(bisect_left(type('', (), {'__getitem__': lambda _, i: r[~i]})(), 0, 0, len(r)) for r in A)

return(j:=0)or sum((j:=next((j for j in range(j,len(r))if r[~j]>=0),len(r)))for r in A)
return sum(itertools.accumulate([0]+A,lambda j,r:next((j for j in range(j,len(r))if r[~j]>=0),len(r))))



def countNegatives(self, grid):
    def bin(row):
        start, end = 0, len(row)
        while start<end:
            mid = start +(end -start) // 2
            if row[mid]<0:
                end = mid
            else:
                start = mid+1
        return len(row)- start
    
    count = 0
    for row in grid:
        count += bin(row)
    return(count)



def countNegatives(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    r, c, cnt = m - 1, 0, 0
    while r >= 0 and c < n:
        if grid[r][c] < 0:
            cnt += n - c
            r -= 1
        else:
            c += 1
    return cnt


def countNegatives(self, grid):
    i = len(grid)-1
    j = 0
    count = 0
    while i>=0 and j< len(grid[0]):        if grid[i][j] < 0:
            count +=len(grid[0])-j
            i -= 1
        else:
            j +=1
    return(count)





































































































