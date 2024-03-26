class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        for i in range(1, len(grid)):
            if (grid[i] != grid[0] and grid[i] != [1 - x for x in grid[0]]):
                return False
        return True