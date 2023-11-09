# class : provides basic structure for an object
class student:
    def _init_(self, name, course):
        self.name = name,
        self.course = course
    def displayDetails(self):
        print("name : ",self.name),
        print("course : ",self.course)
    pihu = _init_("PIHU", "BTECH")
    return pihu

print(pihu)