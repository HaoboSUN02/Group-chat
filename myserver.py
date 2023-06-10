import sys

from ex2utils import Server


# from ex2utils import Client

class myserver(Server):

    def onStart(self):
        self.count = 0
        self.dict = {}
        print("server has started")

    def onStop(self):
        print("server has stopped")

    def onMessage(self, socket, message):
        # message = message.upper()
        (command, sep, parameter) = message.strip().partition(' ')
        (speci_name, sepa, para) = message.strip().partition('|')
        (name, sep, text) = message.strip().partition(':')
        if text == "check users":
            key = self.dict.keys()
            for i in key:
                self.dict[name].send(("the list of connected users is: " + i).encode())
            return True

        if text == "quit":
            # self.dict[name].close()
            del self.dict[name]
            print(name + " has quit")
            return True

        if command == 'reg':

            if parameter in self.dict:
                socket.send("the user name is already used, please redo".encode())

            else:
                socket.send("you have registered successfully".encode())
                self.dict[parameter] = socket
                # return False

        if para == "":
            pass

        elif para in self.dict:
            self.dict[para].send((speci_name + "(private)").encode())
            return True
        else:
            self.dict[name].send("the user you want to send message is not connected".encode())
            return True

        #     self.dict[name] = parameter
        print("message received: " + name + ":" + text)

        # print("message received: " + message.decode())
        print(self.dict)
        print(para)

        for i in self.dict:
            if i != name:

                self.dict[i].send((name + ":" + text).encode())

        return True

    def onDisconnect(self, socket):
        self.count -= 1
        print("a client has disconnected")
        print("number of clients: " + str(self.count))
        # return True

    def onConnect(self, socket):
        self.count += 1
        print("a client has connected")
        print("number of clients: " + str(self.count))
        # return True


ip = sys.argv[1]
port = int(sys.argv[2])
server = myserver()
server.start(ip, port)
