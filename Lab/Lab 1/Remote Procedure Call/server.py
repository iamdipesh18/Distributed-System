import Pyro4

@Pyro4.expose

class Calculator(object):
    def add(self,x,y):
        return(x+y)
    def subtract(self,x,y):
        return(x-y)

#create a Pyro4 daemon
daemon = Pyro4.Daemon()
uri = daemon.register(Calculator)

#print the uri
print("Server URI : ", uri)

#start the server
print("Calculator Server Started. Press Ctrl + C to exit.")

try:
    daemon.requestLoop()
except KeyboardInterrupt:
    print("\n Exiting Calculator Server.")
    daemon.shutdown()
