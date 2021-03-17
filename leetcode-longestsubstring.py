class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_substrings = []
        substring = []
        for index, letter in enumerate(s[:-1]):
            if substring == "":
                substring.append(letter)
            elif letter in substring:
                unique_substrings.append(substring)
                substring = [] 
            elif letter == s[index+1]:
                substring.append(letter)
                substring = []
            else:
                substring.append(letter)
                
        if unique_substrings == "":
            return 0
        else:
            unique_substrings.sort(key=len, reverse=True)
            return len(unique_substrings[0])