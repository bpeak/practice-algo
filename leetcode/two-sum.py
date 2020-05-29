class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

"""
best ( 차이 엄청크네... )
해쉬로 모든수를 다 비교하는것이 아닌
내가 필요로하는 타겟값의 유무만 우선적으로 찾음 ( 없으면 넘어감 )
"""
class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i in range(len(nums)):
            if target - nums[i] in num_map:
                return [i, num_map[target - nums[i]]]
            num_map[nums[i]] = i
            
                
            
                            