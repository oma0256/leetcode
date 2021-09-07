class Solution:
    def numIslands(self, grid):
        count = 0
        for row_positon, row in enumerate(grid):
            for element_position, element in enumerate(row):
                if element == '1':
                    count += 1
                    self.check_vertex_values(
                        element_position, grid, row_positon, row
                    )
        return count
    
    def check_vertex_values(self, element_position, grid, row_positon, row):
        """
        If the current value is 0, search is out of grid or row boundary stop.
        Check values top, bottom, left and right convert to 0 when visited to
        avoid infinite loop
        """
        if grid[row_positon][element_position] == '0':
            return None
        
        grid[row_positon][element_position] = '0'
        # Check up
        if row_positon - 1 >= 0:
            self.check_vertex_values(
                element_position, grid, row_positon - 1, row
            )
        # Check down
        if row_positon + 1 < len(grid):
            self.check_vertex_values(
                element_position, grid, row_positon + 1, row
            )
        # Check left
        if element_position - 1 >= 0:
            self.check_vertex_values(
                element_position - 1, grid, row_positon, row
            )
        # Check right
        if element_position + 1 < len(row):
            self.check_vertex_values(
                element_position + 1, grid, row_positon, row
            )

        return None


grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]
count = Solution().numIslands(grid)
print(count)
