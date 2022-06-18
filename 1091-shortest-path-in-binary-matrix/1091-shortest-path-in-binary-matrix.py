class Solution:
    c=0
    def it(self):
        a=[-1,0,1]
        res=[]
        for i in range(3):
            for j in range(3):
                res.append((a[i], a[j]))
        del res[4]
        return res
                
    def issafe(self, i:int, j:int, n:int)-> bool:
        if i>=n or j>=n or i<0 or j<0:
            return False
        return True
    
    def getmin(self, a:int ,b:int)->int:
        if a<b:
            return a
        return b

    def shortestPathBinaryMatrix(self, a: List[List[int]]) -> int:
        n=len(a)
        if n==0:
            return 0 
        
        if n==1 and a[0][0]==0:
            return 1
        
        if a[0][0]!=0 or a[n-1][n-1]!=0:
            return -1
        
        
        adj=[]
        adj.append((0, 0))
        d=[[sys.maxsize for i in range(n)] for j in range(n)] 
        a[0][0]=1
        d[0][0]=1
        
        it=self.it()
        while len(adj)!=0:
            temp=adj
            adj=[]
            if (n-1, n-1) in temp:
                return d[n-1][n-1] if d[n-1][n-1]!=sys.maxsize else -1
            for i in range(len(temp)):
                crow=temp[i][0]
                ccol=temp[i][1]
                tempd=d[crow][ccol]
                for j in range(8):
                    row=temp[i][0]+it[j][0]
                    col=temp[i][1]+it[j][1]
                    if self.issafe(row,col,n) and a[row][col]==0:
                        a[row][col]=1
                        adj.append((row, col))
                        if tempd+1<d[row][col]:
                            d[row][col]=tempd+1
        
        return d[n-1][n-1] if d[n-1][n-1]!=sys.maxsize else -1

    
    
    

    
#     def bfs(self, g: List[List[int]], v: List[List[bool]], a: List[int], d:int, n:int)->int:
        
#         self.c+=1
#         print(self.c)
#         print(a)

#         if len(a)==0:
#             return d
        
#         adj=[]
#         for i in range(len(a)):
#             # check adj nodes
#             k=self.it()
            
#             v[a[i][0]][a[i][1]]=True
#             print(v)
            
#             for j in range(8):
#                 row=a[i][0]+k[j][0]
#                 col=a[i][1]+k[j][1]
#                 if self.issafe(row, col, n) and g[row][col]==0 and v[row][col]==False:
#                     adj.append((row, col))
#             dmin=self.bfs(g,v,adj,d+1,n)
        
#         if (n-1, n-1) in a and d<dmin:
#             dmin=d
#         # print('dmin is '+str(dmin))
#         # print('d is '+str(d))
#         # if (n-1, n-1) in a:
#         #     dmin=self.getmin(dmin, d)
#         # print('dmin is '+str(dmin))
#         return dmin
        

    
#     takes care of right, down, right-down, and not for left, up, left-up
#     def gmin(self, a:int, b:int, c:int)->int:            
#         m=a
#         if b<m:
#             m=b
#         if c<m:
#             m=c
        
#         return m
        
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         import sys
#         n=len(grid)
#         if n==0:
#             return -1
#         if n==1 and grid[0][0]==0:
#             return 1
#         if grid[0][0]==1:
#             return -1
        
#         sp=[[10000 for i in range(n+1)] for j in range(n+1)]
        
#         for i in range(n):
#             for j in range(n):
#                 if i==0 and j==0:
#                     if grid[i][j]==0:
#                         sp[i+1][j+1]=1
#                     continue

#                 if grid[i][j]==0:
#                     sp[i+1][j+1]=1+self.gmin(sp[i][j+1], sp[i+1][j], sp[i][j])
        
#         print(sp)
                    
#         return sp[n][n] if sp[n][n]!=10000 else -1
        
        