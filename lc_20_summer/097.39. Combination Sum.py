"""
097.39. Combination Sum
组合总和


Given a set of candidate numbers (candidates) (without duplicates) and a target number 
(target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""




# liweiwei
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    size = len(candidates)
    if size == 0:
        return []

    # 剪枝是为了提速，在本题非必需
    candidates.sort()
    # 在遍历的过程中记录路径，它是一个栈
    path = []
    res = []
    # 注意要传入 size ，在 range 中， size 取不到
    self.__dfs(candidates, 0, size, path, res, target)
    return res

def __dfs(self, candidates, begin, size, path, res, target):
    # 先写递归终止的情况
    if target == 0:
        # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
        # 或者使用 path.copy()
        res.append(path[:])
        return

    for index in range(begin, size):
        residue = target - candidates[index]
        # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
        if residue < 0:
            break
        path.append(candidates[index])
        # 因为下一层不能比上一层还小，起始索引还从 index 开始
        self.__dfs(candidates, index, size, path, res, residue)
        path.pop()






def combinationSum(self, candidates, target):
    dp = [[[]] if j == 0 else [] for j in range(target + 1)]
    for candidate in candidates:
        for j in range(candidate, target + 1):
            dp[j] += [res + [candidate] for res in dp[j - candidate]]
    return dp[-1]


























