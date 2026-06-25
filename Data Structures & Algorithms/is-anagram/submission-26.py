class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        table1 = Counter(s)
        table2 = Counter(t)
        if table1 == table2:
            return True
        return False
        #for i, r in enumerate(sort1):
            #if r not in table2:
                #return False
        #return True

        

        