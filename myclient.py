import sys
from ex2utils import Client

class myclient(Client):


    def onStart(self):
        print("client has started")
        self.reg_stat = False


    def onMessage(self, socket, message):

        print("message received: " + message)
        if message == "the user name is already used, please redo":
            self.reg_stat = False
        else:
            self.reg_stat = True
        return message




ip = sys.argv[1]
port = int(sys.argv[2])
client = myclient()
client.start(ip, port)
print("you need to register first, type the name you want to use")
# client.reg_stat
while client.reg_stat == False:

    reg = ("reg " +input("enter register name: "))
    client.send((reg).encode())


(command, sep, parameter) = reg.strip().partition(' ')

print("if you want to sending a message to all users, just type your message")
print("if you want to check  the list of registered/connected users, type 'check users'")
print("enter the message by following form: message|name of person you want to send message.")
print("if you want to quit, type 'quit'\n")
while client.isRunning():
    # client.send("hello world".encode())
    # client.onMessage

    mes = input()
    client.send((parameter + ":" + mes).encode())
    if mes == "quit":
        client.stop()
        break


