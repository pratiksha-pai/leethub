class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if n<=2:
            return []
        nums.sort()
        i=0
        res=[]
        while i<=n-1:
            l=i+1
            r=n-1
            while l<r:
                tsum=nums[i]+nums[l]+nums[r]
                if tsum==0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<n-2 and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                    while r>0 and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                elif tsum>0:
                    r-=1
                else:
                    l+=1 
            while i<n-2 and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return res

#     def swap(self, a:bool)-> bool:
#         if a ==True:
#             return False
#         return True
    
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n=len(nums)
#         if n<=2:
#             return []
        
#         # nmap={}
#         # for i in range(n):
#         #     nmap[i]=nums[i]
            
#         # use nmap for indexes
#         # print(nmap)
#         # nmap=dict(sorted(nmap.items(), key=lambda item: item[1]))
#         # print(nmap)
        
#         nums.sort()
#         res=[]
#         l=0
#         r=n-1
#         flag=False
        
#         print(nums)
#         while l<r:
#             psum=nums[l]+nums[r]
#             # if psum<nums[l]:
#             #     l+=1
#             # elif psum>nums[r]:
#             #     r-=1
#             # else:
#             templ=l+1
#             tempr=r-1
#             count=0
#             print('for l '+str(nums[l])+' r '+str(nums[r]))
#             while templ<=tempr:  
#                 mid=int((templ+tempr+1)/2)
#                 # count=count+1 
#                 # print('count and mid '+str(count)+' '+str(nums[mid]))
#                 print(nums[mid])
#                 if nums[mid]+psum==0:
#                     print('equal')
#                     res.append([nums[l], nums[mid], nums[r]])
#                     templ=mid+1
#                     tempr=mid-1
#                 elif nums[mid]+psum>0:
#                     print('greater than')
#                     tempr=mid-1
#                 else:
#                     print('lesser than')
#                     templ=mid+1
#             print('done with one iter')
#             if flag==False:
#                 while nums[l]==nums[l+1]:
#                     l+=1
#                 l+=1
#                 flag=True
#             else:
#                 while nums[r]==nums[r-1]:
#                     r-=1
#                 r-=1
#                 flag=False
        
#         # temp_res=list(set(res))
#         # temp_res = list(dict.fromkeys(res))
        
#         return res
                    