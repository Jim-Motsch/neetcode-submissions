class Solution:
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        # for i in range(len(nums)):
        #     found = nums[i]
        #     for j in range(len(nums)):
        #         if (found == nums[j] and found != nums[i]):
        #             flag = True
        nums.sort()
        for i in range(len(nums)):
            if(i >= 1):
                prev = nums[i-1]
                if (prev == nums[i]):
                    flag = True
        return flag
            

        