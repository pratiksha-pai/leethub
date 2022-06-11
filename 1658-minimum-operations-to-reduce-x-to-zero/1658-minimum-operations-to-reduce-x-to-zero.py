class Solution:
    # after learning the algorithm 
    def gmax(self, a:int, b:int)->int:
        if a>b:
            return a
        return b
    
    def minOperations(self, nums: List[int], x: int) -> int:
        n=len(nums)
        if n==0:
            return -1
        
        t=sum(nums)
        # to find the sum 
        t=t-x
        if t==0:
            return n
        c=0
        
        # find the max subarray to have the sum as t 
        l=0
        maxl=-1
        
        for r in range(n):
            c+=nums[r]
            while c>t and l<=r:
                c-=nums[l]
                l+=1
            if c==t:
                maxl=self.gmax(maxl, r-l+1)
        
        if maxl==-1:
            return -1
        return n-maxl
                
            
        
    
    
#     before learning the algorithm
#     def getMin(self, a:int, b:int)->int:
#         if a==-1 and b==-1:
#             return -1
#         if a==-1:
#             return b
#         if b==-1:
#             return a
#         if a<b:
#             return a 
#         return b

#     def check(self, nums: List[int], i:int, j:int, x:int, c:int)->int:
#         if x==0:
#             return c
#         if x<0:
#             return -1
        
#         n=len(nums)
#         if i>=n or j<0 or i>j:
#             return -1
        
#         l=-1
#         r=-1
        
#         if x-nums[i]>=0:
#             l=self.check(nums,i+1,j,x-nums[i],c+1)
#             # print('l '+str(l))
#         if x-nums[j]>=0:
#             r=self.check(nums,i, j-1, x-nums[j], c+1)
#             # print('r '+str(r))
        
#         return self.getMin(l,r)
        
    
#     def minOperations(self, nums: List[int], x: int) -> int:
#         n=len(nums)
#         if n==0:
#             return -1
#         c=0
#         return self.check(nums,0,n-1,x,c)