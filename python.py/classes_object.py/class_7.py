#Create Student with name + scores list. Add average() and add_score(score)
class Student :
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores

    def average(self) :
        total = 0
        for num in self.scores :
            total += num
        avg = total / len(self.scores)
        return avg

    def add_score(self,score) :
        self.scores = score
        return self.scores

std = Student("Jia",[1,2,3,4])
print(std.average())
print(std.add_score([11,22,33]))
print(std.average())