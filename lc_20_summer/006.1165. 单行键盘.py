"""
006.1165. Single-Row Keyboard
单行键盘

我们定制了一款特殊的力扣键盘，所有的键都排列在一行上。

我们可以按从左到右的顺序，用一个长度为 26 的字符串 keyboard （索引从 0 开始，到 25 结束）来表示该键盘的键位布局。

现在需要测试这个键盘是否能够有效工作，那么我们就需要个机械手来测试这个键盘。

最初的时候，机械手位于左边起第一个键（也就是索引为 0 的键）的上方。当机械手移动到某一字符所在的键位时，就会在终端上输出该字符。

机械手从索引 i 移动到索引 j 所需要的时间是 |i - j|。

当前测试需要你使用机械手输出指定的单词 word，请你编写一个函数来计算机械手输出该单词所需的时间。


示例 1：

输入：keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
输出：4
解释：
机械手从 0 号键移动到 2 号键来输出 'c'，又移动到 1 号键来输出 'b'，接着移动到 0 号键来输出 'a'。
总用时 = 2 + 1 + 1 = 4. 
示例 2：

输入：keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
输出：73
 
提示：

keyboard.length == 26
keyboard 按某种特定顺序排列，并包含每个小写英文字母一次。
1 <= word.length <= 10^4
word[i] 是一个小写英文字母

"""

# range()   end - 1 !!!
#for i in range(1,len(word)-1):


def calculateTime(self, keyboard, word):
    count = keyboard.index(word[0]) + 1
    for i in range(1,len(word)):
        count += abs(keyboard.index(word[i]) - keyboard.index(word[i-1]))    
    return count


def calculateTime(self, keyboard, word):    
    index = 0
    count = 0
    for i in word:
        count += abs(index - keyboard.index(i))
        index = keyboard.index(i)
    return count
































