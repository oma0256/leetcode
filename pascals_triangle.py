class Solution:
    def generate(self, numRows):
        triangle = [[1]]
        if numRows >= 2:
            triangle = [[1], [1, 1]]
            for _ in range(numRows - 2):
                sub_triangle = []
                last_sub_triangle = triangle[-1]
                for index in range(len(last_sub_triangle) - 1):
                    sub_triangle.append(
                        last_sub_triangle[index] + last_sub_triangle[index + 1]
                    )
                sub_triangle.insert(0, 1)
                sub_triangle.append(1)
                triangle.append(sub_triangle)
        return triangle


print(Solution().generate(5))
print(Solution().generate(1))
        