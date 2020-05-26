class Solution:
    def replaceElements(self, arr):
        for i in range(len(arr) - 1):
            right_max = max(arr[i + 1:])
            arr[i] = right_max
        arr[len(arr) - 1] = -1
        return arr