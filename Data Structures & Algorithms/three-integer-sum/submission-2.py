class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        results = []
        
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]: 
                continue

            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    
                elif total > 0:
                    right -= 1

                else:
                    left += 1   


        return results