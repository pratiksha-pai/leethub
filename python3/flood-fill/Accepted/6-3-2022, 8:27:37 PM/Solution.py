// https://leetcode.com/problems/flood-fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        arr = []
        arr.append([sr, sc])
        row_count = len(image)
        col_count = len(image[0])
        
        visited = [ [ False for i in range(col_count)] for j in range(row_count) ]
        visited[sr][sc] = True
        count  = 0
        while len(arr) != 0:
            row = arr[0][0]
            col = arr[0][1]
            
            count +=1
            # print('for count = '+str(count) + ' for row = '+str(row) + ' for col = '+str(col))

            if row-1 >= 0 and visited[row-1][col] == False and image[row][col] == image[row-1][col]:
                arr.append([row-1, col])
                visited[row-1][col] = True
            if col-1 >= 0 and visited[row][col-1] == False and image[row][col] == image[row][col-1]:
                arr.append([row, col-1])
                visited[row][col-1] = True
            if row+1 < row_count and visited[row+1][col] == False and image[row][col] == image[row+1][col]:
                arr.append([row+1, col])
                visited[row+1][col] = True
            if col+1 < col_count and visited[row][col+1] == False and image[row][col] == image[row][col+1]:
                arr.append([row, col+1])
                visited[row][col+1] = True

            image[row][col] = newColor
            visited[row][col] = True                
                
            # print('before pop')
            # print('length of arr = '+str(len(arr)))
            # for i in range(len(arr)):
            #     print(arr[i][0], arr[i][1])
            
            del arr[0]
            
            # print('after pop')
            # print('length of arr = '+str(len(arr)))
            # for i in range(len(arr)):
            #     print(arr[i][0], arr[i][1])
            
                
        return image
        