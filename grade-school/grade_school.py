class School:
    def __init__(self):
        self.grades = {}

    def add_student(self, name, grade):
        try:
            self.grades[grade].append(name)
        except KeyError:
            self.grades[grade] = [name]

    def grade(self, gradeNo):
        return sorted(self.grades.get(gradeNo, []))

    def roster(self):
        return [
            student
            for k in sorted(self.grades.keys())
            for student in sorted(self.grades[k])
        ]
