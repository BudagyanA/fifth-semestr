class FibonachiList:

    def __iter__(self):
        self.lst = [0, 1]
        return self

    def __next__(self):
        self.lst.append(self.lst[-1] + self.lst[-2]) 
        return self.lst 
