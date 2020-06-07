class Solution:
    def imageSmoother(self , M):
        row = len(M)
        col = len(M(0))
        rlist = []
        clist = []
        for i in range(row):
            for j range(col):
                sum = M[i][j]
                count = 1
                if i-1>=0 and j-1 >=0:
                    sum += M[i-1][j-1]
                    count +=1
                if i-1>=0:
                    sum += M[i-1][j]
                if i-1>=0 and j+1 < col:
                    sum += M[i-1][j+1]
                    count +=1
                if j-1>=0:
                    sum += M[i][j-1]
                if i+1 < col and j-1 >=0:
                    sum += M[i-1][j-1]
                    count +=1
                if j+1 < col:
                    sum += M[i-1][j]
                if i+1 < row and j+1 < col:
                    sum += M[i-1][j+1]
                    count +=1
                if i+1 < row:
                    sum += M[i][j-1]
                rlist.append(sum // count)  #  //表示取整除 - 返回商的整数部分（向下取整）
            clist.append(rlist)
        return clist

