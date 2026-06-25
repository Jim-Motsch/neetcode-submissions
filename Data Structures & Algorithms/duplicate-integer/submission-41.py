class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = set()
        for r in nums:
            if r in table:  # If we've seen this number before, it's a duplicate!
                return True
            table.add(r)
        return False
        