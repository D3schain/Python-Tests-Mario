'''
'                                                                    
' author: Mario Loock                                          
' date: 17:12:2017                                                   
' description: none  
' source: none
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums)<1:
            return False
        
        for i in range(0,len(nums)-1):
            for j in range(0,len(nums)-1):
                if (nums[i] + nums[j] == target) and i != j:
                    return [i,j]
        return False
    

def main():
    solution = Solution()
    result = solution.twoSum([8,99,2,7,11,15], 9)
    print(str(result))
    
if __name__ == "__main__":
    main()