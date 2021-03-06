#!/usr/bin/env python
# coding: utf-8

# In[ ]:


61. Rotate List
Medium

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL


# In[1]:


5%3


# In[5]:


input1 = [1,2,3,4,5]


# In[8]:


def rotateRight(head, k):
    k = k%len(head)
    output = []
    output[:] = head[k+1:] + head[:k+1]
    return output


# In[9]:


output = rotateRight(input1, 2)
output


# In[ ]:




