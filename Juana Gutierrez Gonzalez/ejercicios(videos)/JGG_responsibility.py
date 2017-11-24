"""JUANA GUTIERREZ GONZALEZ
 GITI9072  juanizg7@gmail.com
 1215100194"""
class Handler: #abtrsct handler
    """abstract handler"""
    def __init__(self, successor):
        self._successor = successor #define who is the next handler

    def handle(self, request):
        handled = self._handle(request) #If handler , stop hare

        #Otherwise , keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler): #Inherits form the abstract handler
    """Concrete handler 1"""
    def _handle(self, request):
        if 0 < request <= 10: #provide  a condition sor handling
            print("request {} handled in handler 1".format(request))
            return True #indicate that the request has been handler

class DefaultHandler(Handler): #Inherits from the abstract  handler
    """Default Handler"""

    def _handle(self, request):
        """If there is not  handler avaliable """
        #No condition checking since this a deafault handler
        print("End of chain, no handler for {}".format(request))
        return True #Indicates that the reques has been handler

class Client: #using handlers
    def __init__(self):
      self.handler = ConcreteHandler1(DefaultHandler(None)) #Create handlers and use them is a sequense you want
                                                            #Note that the default handler has no successor
    def delegate(self, requests): #send yours requests one at a time for handlers  to handler
        for request in requests:
            self.handler.handle(request)

# Create  a client
c = Client()
#Create requests
requests = [2, 5, 30]
#send the requests
c.delegate(requests)