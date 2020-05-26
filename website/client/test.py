from client import Client
import time
from threading import Thread

c1 = Client("Ian")
c2 = Client("Ivan")

def update_messages():
    msgs = []
    run = True
    while run:
        time.sleep(0.1)
        new_messages = c1.get_messages()
        msgs.extend(new_messages)
        for msg in new_messages:
            print(msg)
            if msg == "{вышел}":
                run = False
                break

Thread(target=update_messages).start()

c1.send_message("privet")
time.sleep(1)
c2.send_message("bla bla bla")
time.sleep(2)
c1.send_message("kak dela")
time.sleep(3)
c2.send_message("best")
time.sleep(41)
c1.send_message("dlskfjsdlf")
time.sleep(5)
c2.send_message("good bye")
time.sleep(6)

c1.disconnect()
time.sleep(2)
c2.disconnect()