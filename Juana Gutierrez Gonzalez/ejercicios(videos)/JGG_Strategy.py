"""JUANA GUTIERREZ GONZALEZ
 GITI9072  juanizg7@gmail.com
 1215100194"""
import types #Import the types module

class Strategy:
    """tThe Strategy pattern class """

    def __init__(self, function=None):
        self.name = "default Strategy"

        #If  a reference  to a funtion is a provided, replace the execute ()method the given function

    def execute(self): #This gets replaced by another verion if another strategy is provided
        """The defaul method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))

#Replacemet method 1
def strategy_one(self):
    print("{}is used to execute method 1".format(self.name))

#Replacemet method 2
def strategy_two(self):
    print("{} used to execute method 2".format(self.name))



#Let's create our default strategy
s0 = Strategy()
#Let's create our default strategy
s0.execute()

#Let's create the first varition of our default by providing a new behabior
s1 = Strategy(strategy_one)
#let's set its name
s1.name  = "strategy one"
#let's execute  the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy two"
s2.execute()