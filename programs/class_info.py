class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    class_ = "student"

    def test_score(self, maths, chemistry, biology):
        avg = (maths + chemistry + biology)/3
        return avg

John = Student("John", 21)
Jane = Student("Jane", 22)
Jack = Student("Jack", 22)

print(John.class_)
print(John.test_score(63, 74, 82))
print(Jane.class_)
print(Jane.test_score(75, 82, 66))
print(Jack.class_)
print(Jack.test_score(84, 57, 77))



