class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        item = intervals.pop(0)
        
        while intervals:
            
            s1,e1, s2,e2 = item[0], item[1], intervals[0][0], intervals[0][1]
            
            if e1>= s2:
                item = [s1, max(e1,e2)]
                intervals.pop(0)
            else:
                res.append(item)
                item = intervals.pop(0)
                
        res.append(item)
            
        return res