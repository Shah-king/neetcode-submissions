class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} #create an empty dictionary
        for i, item in enumerate(nums): # iterate over the list of numbers
            complement = target - item # find the num needed to reach the target
            if complement in dict: 
                return [dict[complement], i] # if such num exists in the dictionary return it's index 
            dict[item] = i # If not, store the current item with its index i in the dictionary 
        return [] # return an empty dictionary