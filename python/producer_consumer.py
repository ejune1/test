import time
import random
from threading import Thread
from threading import Lock
from threading import Event

class Messages:
    def __init__(self):
        #use a list as a queue, pretend it isn't thread safe
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

class Producer:
    def __init__(self, messages, limit):
        self.messages = messages
        self.limit  = limit
    
    def produce(self):
        for x in range(limit):
            message = random.randint(0, 99)
            self.messages.send(message)
            print(f"Producer sent {message}")
            
            #pretend some processing is going on
            sleeptime = random.randint(0,1000)
            time.sleep(sleeptime / 1000)

        message = -1
        self.messages.send(message)

        print(f"Producer sent {limit} messages")

class Consumer:
    def __init__(self, messages):
        self.messages = messages

    def consume(self):
        message = 0
        while message != -1:
            #blocks
            message = messages.receive()
            print(f"Consumer got {message}")

            #pretend some processing is going on
            sleeptime = random.randint(0,1000)
            time.sleep(sleeptime / 1000)

if __name__ == "__main__":
    limit = 100
    messages = Messages()

    producer = Producer(messages, limit)
    consumer = Consumer(messages)

    producer_thread = Thread(target = producer.produce)
    consumer_thread = Thread(target = consumer.consume)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
