class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        merged = [intervals[0]]
        for cur in intervals[1:]:
            last_merge = merged[-1]
            if last_merge[1] >= cur[0]:
                last_merge[1] = max(last_merge[1], cur[1])
            else:
                merged.append(cur)
        return merged