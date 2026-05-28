class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        
        counts = list(s)
        proof = list(t)
        counts.sort()
        proof.sort()
        flag = True
        for i in range(len(proof)):
            if(proof[i]==counts[i]):
                flag
            else:
                flag = False
        return flag



