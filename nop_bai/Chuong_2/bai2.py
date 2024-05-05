def TamGiacTren(self):
        n = len(self)
        for i in range(1,n):
            for j in range(1, i):
                print(i ,"   " ,j," ", self[i][j])
                if self[i][j] != 0:
                    return False
        return True