class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap
        freq = [[] for i in range(len(nums)+ 1)] # iterate over the frequecy list
        for n in nums: # for ecah number in the input array
            count[n] = 1 + count.get(n , 0) # we want to get the count/ freq of ecah number
        for n, c in count.items(): # append the count to the freq list
            freq[c].append(n)
        res = [] # empty array to store result
        for i in range(len(freq) - 1, 0, -1): # we go backwards start from end of the list and go until the beginning of the list 
            for n in freq[i]: # for ecah index value append it the result array 
                res.append(n)
                if len(res) == k: # once we know the numbe of k elements we are looking for then return it 
                    return res
            

        

        