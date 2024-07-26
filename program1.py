def getTotalIsles(grid):
    def dfs(row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W':
            return
        grid[row][col] = 'W'  
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(row + dr, col + dc)

    num_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L':
                num_islands += 1
                dfs(row, col)

    return num_islands

map1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]

map2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]

print("Number of distinct islands in map 1:", getTotalIsles(map1))
print("Number of distinct islands in map 2:", getTotalIsles(map2))  
