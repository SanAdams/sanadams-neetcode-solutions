class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        # A 2D array that stores the values that occur at the frequency of that index 
        # For example, if 5, 3, and 2 occur 2 times frequency_array[2] = [5,3,2]
        # Initialized to empty arrays len(nums) + 1 times
        frequency_array = [[] for i in range (len(nums) + 1)]
        for num in nums:

            # Look into the frequency map and increment the value associated with the key num, if no such key exists, 
            # return 0, add 1, then map that key to a value equaling 1
            frequency_map[num] = 1 + frequency_map.get(num, 0)

        for num, freq in frequency_map.items():

            # For every number-frequency pair in the map, add the number to the list corresponding to its frequency
            frequency_array[freq].append(num)

        res = []
        
        for i in range(len(frequency_array) - 1, 0, -1):
                for num in frequency_array[i]:
                    res.append(num)

                    if len(res) == k:
                        return res


        