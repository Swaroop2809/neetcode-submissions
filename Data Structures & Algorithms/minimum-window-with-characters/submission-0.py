from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        have={}
        required=len(need)
        formed=0
        left=0
        min_len=float("inf")
        result=""
        for right in range(len(s)):
            ch=s[right]
            have[ch]=have.get(ch,0)+1
            if ch in need and have[ch]==need[ch]:
                formed+=1
            while formed==required:
                window=right-left+1
                if window<min_len:
                    min_len=window
                    result=s[left:right+1]
                
                have[s[left]]-=1
                if s[left] in need and have[s[left]]<need[s[left]]:
                    formed-=1
                left+=1
        return result        