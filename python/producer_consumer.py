from threading import Thread
from threading import Lock
from threading import Event

class Messages:
    def __init__(self):
        self.__messages = []
        self.__lock = Lock()
        self.__event = Event()

    def __str__(self):
        return str(self.messages)

    def send(self, message):
        self.__lock.acquire()
        self.__messages.append(message)
        self.__event.set()
        self.__lock.release()

    def receive(self):
        self.__event.wait()
        self.__lock.acquire()
        message = None
        if len(self.__messages) > 0:
            message = self.__messages.pop(0)

        if len(self.__messages) == 0:
            self.__event.clear()

        self.__lock.release()
        return message
