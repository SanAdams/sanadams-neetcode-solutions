class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency_arrays = {}
        res = []
       # Turn each word into a frequency array
        for string in strs:
            frequency = [0] * 26
            for i in range(len(string)):
                frequency[ord(string[i]) - 97] += 1
            frequency_arrays[string] = tuple(frequency)

        # Map the frequency arrays(words) to their sublists
        sublists = {}
        for i in range(len(strs)):
            current_string = strs[i]
            if frequency_arrays[current_string] in sublists:
                sublists[frequency_arrays[current_string]].append(current_string)
            else:
                sublists[frequency_arrays[current_string]] = []
                sublists[frequency_arrays[current_string]].append(current_string)
        
        # append each sublist to the result
        for sublist in sublists.values():
            res.append(sublist)

        return res