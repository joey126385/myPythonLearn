class Person():
    pass

class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class Factory():
    def get_person(self,p_type):
        if p_type == "w":
            return Worker()
        elif p_type == "s":
            return Student()
        elif p_type == "t":
            return Teacher()
        else:
            raise ValueError("创建异常，请传入正确的人类型！")

factory = Factory()
worker = factory.get_person("w")
student =  factory.get_person("s")
teacher =  factory.get_person("t")