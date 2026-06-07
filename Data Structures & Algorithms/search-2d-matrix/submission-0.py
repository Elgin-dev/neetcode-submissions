class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        l=0
        r=row *col -1
        while l<=r:
            mid=(l+r)//2
            row_in=mid//col
            col_in=mid%col
            val=matrix[row_in][col_in]
            if (val==target):
                return True
            elif val< target:
                l+=1
            else:
                r-=1
        return False                