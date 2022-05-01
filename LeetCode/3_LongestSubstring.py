class Solution:
    def lengthOfLongestSubstring(s) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            print("r",r)
            print("s",s[r])
            if s[r] not in seen:
                output = max(output,r-l+1)
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output
    #s = "abcabcbb" #3
    #s = "bwf"      #3
    #s = "au"       #2
    #s = "pwwkew"    #3
    #s = " "
    s = "aabaab!bb"
    print(lengthOfLongestSubstring(s))