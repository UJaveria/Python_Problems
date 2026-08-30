# Put several Student objects in a list. Write a plain function top_student(students) returning the
# highest-average student.
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



def top_student(students):
        avg = []
        for std in students :
            avg.append(Student.average(std))

        heighest = max(avg)
        for std in students :
            if Student.average(std) == heighest :
                return (f"Object : {std}, Name of Object : {std.name}")


std1 = Student("Mani",[80,79,90,69,100])
std2 = Student("Javeria",[77,81,68,66,70])
std3 = Student("Atiq",[90,70,65,71,66])
std4 = Student("Shafiq",[88,91,83,77,68])
students = [std1,std2,std3,std4]
print(top_student(students))
