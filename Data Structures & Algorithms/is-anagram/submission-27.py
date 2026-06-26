class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1 = Counter(s)
        table2 = Counter(t)
        if table1 == table2:
            return True
        return False


        

        