class C:
    def __init__(self, students_grades):
        self.students_grades = students_grades

    def m(self, n):
        result = []
        for student, grades in self.students_grades.items():
            if sum(grades) / len(grades) >= n:
                result.append(student)
        result.sort()
        return ",".join(result)