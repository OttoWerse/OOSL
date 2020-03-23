class Student:
    """Class student"""
    no_of_students = 0

    def __init__(self, first_name, last_name, mat_nr):
        """Constructor for class "Student\""""
        Student.no_of_students += 1
        self.first_name = first_name
        self.last_name = last_name
        self.mat_nr = mat_nr

    def __str__(self):
        """String conversion for class "Student\""""
        return f'{self.last_name}, {self.first_name}: {self.mat_nr}'

    @property
    def get_details(self):
        """Returns details for a student"""
        return self.__dict__

    def enroll(self, course):
        """Enrolls a student in a given course"""
        course.enroll(self)

    def get_no_of_students(self):
        """returns the amount of students"""
        return Student.no_of_students

    def get_course_participants(self, course):
        """generates a list of all students in a given course"""
        return course.participants


class Course:
    def __init__(self, course_id, name, participants=[]):
        """Constructor for class "Course\""""
        self.course_id = course_id
        self.name = name
        self.participants = participants

    def __str__(self):
        """String conversion for class "Student\""""
        return f'{self.course_id}, {self.name}: {self.participants}'

    def enroll(self, student):
        """Enrolls a student"""
        self.participants.append(student)


if __name__ == '__main__':
    s = Student('Tim', 'Garbe', 13374269)
    print(s)
    c = Course(420, 'Angewandte Rattenhörnchenologie')
    s.enroll(c)
    print(c)

    print(s.get_course_participants(c))
    print(s.get_no_of_students())