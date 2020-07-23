"""
048.249. Group Shifted Strings
移位字符串分组

给定一个字符串，对该字符串可以进行 “移位” 的操作，也就是将字符串中每个字母都变为其
在字母表中后续的字母，比如："abc" -> "bcd"。这样，我们可以持续进行 “移位” 操作，从而生成如下移位序列：

"abc" -> "bcd" -> ... -> "xyz"
给定一个包含仅小写字母字符串的列表，将该列表中所有满足 “移位” 操作规律的组合进行分组并返回。

 

示例：

输入：["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
输出：
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
解释：可以认为字母表首尾相接，所以 'z' 的后续为 'a'，所以 ["az","ba"] 也满足 “移位” 操作规律。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-shifted-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




"""

def groupStrings(self, strings: List[str]) -> List[List[str]]:
    dic = {}
    ret = []

    for w in strings:
        if str(len(w)) not in dic:
            dic[str(len(w))] = []
        dic[str(len(w))].append(w)

    for _, v in dic.values():
        if len(v) == 1:
            ret.append(v)
        else:
            v.

    return ret



































