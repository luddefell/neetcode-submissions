class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t = 0
        b = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1
        result = []
        while l <= r and t <= b:

            for col in range(l, r + 1):
                result.append(matrix[t][col])
            t += 1

            for row in range(t, b + 1):
                result.append(matrix[row][r])
            r -= 1

            if t <= b:
                for col in range(r, l - 1, -1):
                    result.append(matrix[b][col])
                b -= 1

            if l <= r:
                for row in range(b, t - 1, -1):
                    result.append(matrix[row][l])
                l += 1

        return result