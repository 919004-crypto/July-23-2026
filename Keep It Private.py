class myClass:

    __priveVar=27;

    def __priveMeth(self):
        print("I am inside class myClass")
    
    def hello(self):
        print("This is the value of priveVar:",myClass.__priveVar)

foo = myClass()  
foo.hello()  

