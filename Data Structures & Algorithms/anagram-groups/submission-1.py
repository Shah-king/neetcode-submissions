class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Hashmap = defaultdict(list) # mapping char to list of anagrams
        for s in strs:
            count = [0] * 26 # a.....z

            for c in s:
                count[ord(c) - ord("a")] += 1 #subtracting 'a' ascii val from 'z' ascii val
            Hashmap[tuple(count)].append(s) # list can't be keys so we use tuple
        return Hashmap.values() # we return the keys in the hashmap

        
        
        