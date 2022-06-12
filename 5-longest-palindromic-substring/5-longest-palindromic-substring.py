class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0:
            return ''
        if n==1:
            return s
        if n==2 and s[0]==s[1]:
            return s
        
        lps=[]
        lpsl=[]
        lpsr=[]
        
        for i in range(n):
            lps.append(1)
            lpsl.append(i)
            lpsr.append(i)
        

        # odd palindrome        
        for i in range(0, n):
            templ=i-1
            tempr=i+1
            l=i
            r=i
            c=1
            
            while templ>=0 and tempr<n and s[templ]==s[tempr] :
                l=templ
                r=tempr
                c+=2
                
                templ-=1
                tempr+=1
                
            
            if c>lps[i]:
                lps[i]=c
                lpsl[i]=l
                lpsr[i]=r
        

        # even palindrome        
        for i in range(0, n-1):
            if s[i]!=s[i+1]:
                continue
            
            templ=i-1
            tempr=i+2
            l=i
            r=i+1
            c=2
            
            while templ>=0 and tempr<n and s[templ]==s[tempr] :
                l=templ
                r=tempr
                c+=2
                
                templ-=1
                tempr+=1
            
            if c>lps[i]:
                lps[i]=c
                lpsl[i]=l
                lpsr[i]=r
        
        maxlps=-1
        maxlpsi=-1
        
        for i in range(n):
            if maxlps<lps[i]:
                maxlps=lps[i]
                maxlpsi=i
        
        if maxlps==-1:
            return []
        
        final_l=lpsl[maxlpsi]
        final_r=lpsr[maxlpsi]
        return s[final_l:final_r+1:1]
        
        
#      gives TLE
#         n=len(s)
#         if n==0:
#             return ''
#         if n==1:
#             return s
#         if n==2 and s[0]==s[1]:
#             return s
        
#         lps=[[0 for i in range(n)] for j in range(n)]
#         k=0
#         for i in range(n):
#             lps[i][i]=1
        
#         for k in range(1,n):
#             for i in range(n-k):
#                 j=i+k
#                 if s[i]==s[j]:
#                     if i+1==j or lps[i+1][j-1]!=0:
#                         lps[i][j]=lps[i+1][j-1]+2
#                     else:
#                         lps[i][j]=0
#                 else:
#                     lps[i][j]=0
        
#         l=0
#         r=0
#         maxlps=-1
#         for i in range(n):
#             for j in range(i,n):
#                 if lps[i][j]>maxlps:
#                     maxlps=lps[i][j]
#                     l=i
#                     r=j
        
#         # print(lps)
#         # print(l,r)
        
#         return s[l:r+1:1]