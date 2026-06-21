class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        left, right = 0, len(numbers) -1
        sum, index1, index2 = [],0,0
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else: 
                index1 = left+1
                index2 = right+1
                break
        return [index1,index2]

        