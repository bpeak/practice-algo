class Solution:
    def uniqueOccurrences(self, arr):
        num_map = {}
        num_set = set()
        for v in arr:
            if v in num_map:
                num_map[v] += 1
            else:
                num_map[v] = 1
        for v in num_map.values():
            if v in num_set:
                return False
            num_set.add(v)
        return True