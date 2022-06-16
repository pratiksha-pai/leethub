class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        # print(l1, l2)
        
        s1=''.join(sorted(s1))
        for i in range(0, l2-l1+1):
            t=s2[i:i+l1]
            t=''.join(sorted(t))
            if s1==t:
                return True
            # print(t)
            
        return False
        
        
        
        
        
#         gives tle
#         return False
#         for i in range(l2):
#             j=i
#             t=s1
            
#             while j<l2 and s2[j] in t:
#                 # print(s2[j])
#                 k=t.index(s2[j])
#                 t=t[0:k]+t[k+1:]
#                 j+=1
#             if len(t)==0:
#                 return True
#             # print()
#         return False
        
        
#         some tests 
#         e="abbbcd"
#         if "b" in e:
#             # print(del e[e.index("b")])
#             i=e.index("b")
#             e=e[0:i]+e[i+1:]
#             i=e.index("a")
#             e=e[0:i]+e[i+1:]
#             print(e)
            
#         t=s1
#         index=0
#         l=None
#         r=None
        
#         while t[index] not in s2:
#             index+=1
        
#         if t[index] not in s2:
#             return False
#         else:
#             i=s2.index(t[index])
#             if i
#             l=i-1
#             r=i+1
        
        
#         while len(t)!=0 or s2[i] in t or s2[l] in t or s2[r] in t:
#             t=t[0:i]+t[i+1:]