class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        else:
            freq_map_t = {}
            freq_map_s = {}

            for letter in t:
                freq_map_t[letter] = 1 + freq_map_t.get(letter, 0)
            
            for letter in s:
                freq_map_s[letter] = 1 + freq_map_s.get(letter, 0)
            
            for letter in t:
                if freq_map_t.get(letter) != freq_map_s.get(letter):
                    return False
            
            return True

