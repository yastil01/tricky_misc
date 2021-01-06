class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        left, up = 0, 0
        right, down = cols-1, rows-1
        
        res = []
        dir = 'R'
        while len(res) < rows*cols:

            for i in range(left, right+1):
                res.append(matrix[up][i])
            up += 1

            if  len(res) < rows*cols:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
     

            if  len(res) < rows*cols:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1


            if  len(res) < rows*cols:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
 
        return res
