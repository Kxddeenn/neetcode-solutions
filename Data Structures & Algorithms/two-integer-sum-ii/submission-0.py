class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = defaultdict(int)
        for i in range(len(numbers)):
            goal = target - numbers[i]
            
            if goal in res: 
                return [res[goal], i+1]
            
            res[numbers[i]] = i+1

        return False