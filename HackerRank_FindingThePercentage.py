class mark:
    def __init__(self, markList):
        self.markList = list()
        self.markList = markList
        self.sum = 0
        self.num = len(self.markList)
        self.average = 0
    
    def calcAverage(self):
        for marks in self.markList:
            self.sum += marks
        try:
            self.average = self.sum / self.num
        except:
            print("Exception")
            return -1
        else:
            return self.average

    def __del__(self):
        pass

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    #print(student_marks[query_name])
    studentMark = mark(student_marks[query_name])
    print("%.2f" % studentMark.calcAverage())
    del studentMark
