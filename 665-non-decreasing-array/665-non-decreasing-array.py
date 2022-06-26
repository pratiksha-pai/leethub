class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<=2:
            return True
        
        c=0
        # nums.insert(0, -100001)
        # nums[0]=-1000001, nums[1]=nums[0] hence nums[1]>nums[0] 
        # test for i>2
        for i in range(1, n):
            # print('for num '+str(nums[i]))
            if nums[i]<nums[i-1]:
                if i==1:
                    nums[i-1]=nums[i]
                    c+=1
                    continue
                # check if nums[i] > nums[i-2] to decide whether i should be replaced or i-1
                if nums[i]<nums[i-2]:
                    nums[i]=nums[i-1]
                else:
                    nums[i-1]=nums[i]
                
                c+=1
                # print('c is '+str(c))
                if c>1:
                    return False
            
        
        
        if c>1:
            return False
        return True