class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        index = 0
        index1 = 0
        stoploop = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i !=j:
                    index = i
                    index1 = j
                    stoploop = True
                    break
            if stoploop:
                break
        arr.append(index)
        arr.append(index1)
        return arr
        