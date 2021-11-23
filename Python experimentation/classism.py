class testClass:
    #define a default class attribute
    brain = False

    #init is called whenver a class is instantiated
    def __init__(self, name, color):
        # I guess classes don't need to have predefined attributes
        self.name = name #can create and assign an attribute just like this
        self.color = color # do it again!

    #this is an instance method that returns the class as  string
    def __str__(self):
        return f"name: {self.name}, color: {self.color}, brain: {self.brain}"
        
    #no need to call printself when you can just print(object)
    def printSelf(self):
        return f"name: {self.name}, color: {self.color}, brain: {self.brain}"


class subOfTest(testClass):
    x = "this is so poggers"
    
    #introduced default argument of name, let's see how this pans out
    def __init__(self, color, yellow,name = "god"):
        # I guess classes don't need to have predefined attributes
        self.name = name #can create and assign an attribute just like this
        self.color = color # do it again!
        self.yellow = yellow


    def __str__(self):
        try:
            return f"name: {self.name}, color: {self.color}, brain: {self.brain}, pog check: {self.x}, yellow: {self.yellow}"
        except:
            return "I dunno"
            
if __name__ == "__main__":
    instOfTestClass = testClass("gilbert godfried", 3)

    #print(f"what am I doing with my life: {instOfTestClass.name} and in a shade of {instOfTestClass.color} with a humongous {instOfTestClass.brain}")
    #instOfTestClass.brain = 7
    #print(f"actually my humongous is {instOfTestClass.brain}")
    #print(instOfTestClass.printSelf())
    #print(instOfTestClass)

    instSub = subOfTest("Greg", "seven")
    print(instSub)