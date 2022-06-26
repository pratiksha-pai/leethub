class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        adj=set()
        m=len(mat)
        n=len(mat[0])
        
        def issafe(a,b):
            if 0<=a<m and 0<=b<n:
                return True
            return False
        
        it=[[-1,0], [0,-1], [1,0],[0,1]]
        
        visited=[[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(4):
                    row=i+it[k][0]
                    col=j+it[k][1]
                    if issafe(row, col) and mat[i][j]==0:
                        visited[i][j]=True
                        if mat[row][col]!=0:
                            adj.add((row,col))

        c=0
        # print(visited)
        res=[[sys.maxsize for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    res[i][j]=0 
        
        # print(res)
        while len(adj)!=0:
            # print(adj)
            temp=set()
            c+=1
            temp_adj=list(adj)
            # print(c)
            # print(visited)
            for p in range(len(temp_adj)):
                i=temp_adj[p][0]
                j=temp_adj[p][1]
                visited[i][j]=True
                if c<res[i][j]:
                    res[i][j]=c
                
                # print('for i and j '+str(i)+' '+str(j))
                for k in range(4):
                    row=i+it[k][0]
                    col=j+it[k][1]
                    # print(row,col)
                    if issafe(row,col) and mat[row][col]>=1 and visited[row][col]==False:
                        temp.add((row,col))
                        
            # print(visited)

            adj=temp
                        
            
        
        return res