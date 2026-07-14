class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" # empty string
        for s in strs: # iterate through the string
            res += str(len(s)) + "#" + s # add the len of the string to the string and the # symbol
        return res # return res


    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # res is empty list, i is a pointer
        while i < len(s): # we check as i doen't exceed the length of the orginal string
            j = i # we set another pointer starting at i
            while s[j] != "#": # as long as we don't reach the # char we increment j
                j += 1
            length = int(s[i: j]) # once we reach the # char we know the len of the string is from i to j
            res.append(s[j + 1 : j + 1 + length]) # this gives us our entire string
            i = j + 1 + length # update the pointer i 
        return res # return res

