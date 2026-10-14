class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]] 
        ans = self.generate(numRows-1)    
        newRow = []
        newRow.append(1)
        for i,x in enumerate(ans[-1]):
            if x==1 and i != 0:
                break
            newRow.append(ans[-1][i]+ans[-1][i+1])
        newRow.append(1)
        ans.append(newRow)
        return ans       

    


        