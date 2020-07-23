"""
042.3. Longest Substring Without Repeating Characters
无重复字符的最长子串

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""



while i < len(s):
            if s[j] not in cache:
                cache[s[j]] = 1
                j += 1
                continue
            else:
                longest = max(longest, len(cache))
                cache[s[i]] = 0
                cache[s[j]] = 1
                i += 1



def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0: return 0
    if len(s) == 1: return 1

    i = 0
    j = 2
    longest = 1
    char = {}
    while i < len(s) and j <= len(s):
        #print(s[i:j]
        if len(set(s[i:j])) > longest:
            longest += 1
            #j += 1
        else:
            i += 1
        j += 1
    return longest


def lengthOfLongestSubstring(self, s: str) -> int:
    start = maxLength = 0
    usedChar = {}
    
    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i

    return maxLength


def lengthOfLongestSubstring(self, s: str) -> int:
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)
            
        used[c] = i

    
    return max_length


def lengthOfLongestSubstring(self, s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dic:
            # update the res
            res = max(res, i-start)
            # here should be careful, like "abba"
            start = max(start, dic[ch]+1)
        dic[ch] = i
    # return should consider the last 
    # non-repeated substring
    return max(res, len(s)-start)



def lengthOfLongestSubstring(self, string):
    """
    Time:  O(n)
    Space: O(k)
    [k = length of the longest substring w/o repeating characters]
    """
    longest = 0
    left, right = 0, 0
    chars = set()
    while left < len(string) and right < len(string):
        if string[right] not in chars:
            chars.add(string[right])
            right += 1
            longest = max(longest, right - left)
        else:
            chars.remove(string[left])
            left += 1
    return longest


def lengthOfLongestSubstring(self, s):
    seen = ''
    mx = 0
	#1. for each character in s
    for c in s:
		#2. check if c is seen
        if c not in seen:
		#3. if not seen, add to seen list 
            seen+=c
        #4 if seen, slice seen list to previous c
        # for example, if c is 'a' and seen list is 'abc'
        # you will be slicing previous 'a'(seen.index(c)+1), thus seen list become 'bc'
        # then add the current 'a' bc + a, seenlist = 'bca'
        else:
            seen = seen[seen.index(c) + 1:] + c
        #5 check max length between current max with new length of seen
        mx = max(mx, len(seen))
    return mx


def lengthOfLongestSubstring(self, s: str) -> int:
    seen = {}
    l = 0
    output = 0
    for r in range(len(s)):
        """
        If s[r] not in seen, we can keep increasing the window size by moving right pointer
        """
        if s[r] not in seen:
            output = max(output,r-l+1)
        """
        There are two cases if s[r] in seen:
        case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
        case2: s[r] is not inside the current window, we can keep increase the window
        """
        else:
            if seen[s[r]] < l:
                output = max(output,r-l+1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r
    return output


def lengthOfLongestSubstring(s: str):
    max_len = 0
    sub = ''
    
    for l in s:
        if l in sub:
            sub = sub[sub.find(l)+1:]        
        sub += l
        if len(sub) > max_len:
            max_len = len(sub)
            
    return max_len











