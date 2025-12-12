"""
Intuition
In short you need to pair element in array g to elements in array s in such a way that g[i] <= s[j]. 
To get the biggest number of such pairs you need to put the best g[i] for s[j].

The best here is the closest value of s[j]. 
Why the closest? Lets look at those two values 4, 7 from g and and 8 from s. 
It is better to select 7 as this gives more options to pair with 4 (4, 5, 6, 7, 8) can be paired.

So you sort both lists and then you do the simulation (moving from biggest to smallest value). 
You can either pop values (like I have done in python), but you can also just move indices (like I did in rust).

Complexity
Let n = max(len(s), len(g)), then

Time complexity: O(nlog⁡n)O(n \log n)O(nlogn)
Space complexity: O(1)O(1)O(1)
"""

# Code
class Solution:
  def findContentChildren(self, g: List[int], s: List[int]) -> int:
    if len(g) == 0 or len(s) == 0:
      return 0
    
    res = 0
    g, s = sorted(g), sorted(s)
    while s and g:
      cookie = s.pop()
      while g:
        greed = g.pop()
        if greed <= cookie:
          res += 1
          break
    
    return res