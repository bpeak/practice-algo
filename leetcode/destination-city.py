# https://leetcode.com/problems/destination-city

class Solution:
    def destCity(self, paths):
        srcSet = set()
        for src, dest in paths:
            srcSet.add(src)
        for src, dest in paths:
            if dest not in srcSet:
                return dest
