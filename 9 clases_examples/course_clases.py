class Course:
    def __init__(self, courseName, credit, courseBook):
        self.courseName = courseName
        self.credit = credit
        self.courseBook = courseBook
        self.score = 0

    # this method suppose to print the course info
    def info(self):
        return print(f"This course is {self.courseName} {self.credit} {self.courseBook} {self.score}")

    # this method suppose to update the score
    def updateScore(self, grade):
        self.score = grade

    def updateCourseBook(self, book):
        self.courseBook = book

# create three objects for your courses.
mathematics = Course ("Math", 5, "Math without stress")
english = Course ("Professional English language B2", 3, "English. Professional language B2.")
mathematics.info()
mathematics.updateScore(5)
mathematics.updateCourseBook("New book")
mathematics.info()