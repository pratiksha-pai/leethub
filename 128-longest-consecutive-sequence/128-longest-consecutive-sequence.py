class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        a.sort()
        n=len(a)
        if n==0:
            return 0
        s=1
        l=1
        print(a)
        for i in range(1, n):
            if a[i]==a[i-1]:
                continue
            if a[i] != a[i-1]+1:
                if l<s:
                    l=s
                s=1
            else:
                s+=1
        if l<s:
            l=s
        return l