"""JUANA GUTIERREZ GONZALEZ
 GITI9072  juanizg7@gmail.com
 1215100194"""
class Borg:
    """Borg class making attributes  global """
    _shared_state =  {}
 #attribute dictionary

    def __init__(self):
        self.__dict__=self._shared_state #make it attribute dictionary

class Singleton(Borg): #inherits from the Borg class
    """this essenstially  make the singleton objects an objects-oriented global  variable"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        #update the attrubute dictionary by inserting  a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
    #returns  the attribute dictionay  for printing
     return str(self._shared_state)

#let's create  a singleton  object  and add our firts acronym
x = Singleton(HTTP = "Hyper Text Tranfer Protocol")
#print the object
print(x)

#let's  create another singleton  object  and if it refers to the some attribute  dictionary  by adding another acronym
y=Singleton(SNMP = "simple network Management protocol")
#print de object
print(y)