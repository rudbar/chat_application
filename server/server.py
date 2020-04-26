from socket import AF_INET, socket, SOCK_STREAM 
from threading import Thread
import time
from person import Person

# ГЛОБАЛЬНЫЕ КОНСТАНТЫ
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZ = 512

# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ
persons = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR) # настройка сервера


def broadcast(msg, name):
    # отправляем новые сообщения всем пользователям
    for person in persons:
        client = person.client
        client.send(bytes(name, "utf8") + msg)


def client_communication(person):
    # Поток обрабатывает все сообщения от пользователя
 
    client = person.client

    # получаем имя пользователя
    name = client.recv(BUFSIZ).decode("utf8")
    person.set_name(name)
    msg = bytes(f"{name} присоединился к беседе!", "utf8")
    broadcast(msg, "") # вывод сообщения приветствия

    while True:
        try:
            msg = client.recv(BUFSIZ)

            if msg == bytes("{quit}", "utf8"):
                client.close()
                persons.remove(person)
                broadcast(bytes(f"{name} покинул(-а) чат...", "utf8"), "")
                print(f"[ОТКЛЮЧИЛСЯ] {name} отключился(-ась)")
                break
            else:
                broadcast(msg, name+": ")
                print(f"{name}: ", msg.decode("utf8"))

        except Exception as e:
            print("[ОШИБКА]", e)
            break


def wait_for_connection():
    # Ожидание подключения нового пользователя, когда новый пользователь подключился, 
    # запускается новый поток

    while True:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            persons.append(person)
            print(f"[ПОДКЛЮЧЕНИЕ] {addr} присоединился к беседе в {time.time().now}")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print("[ОШИБКА]", e)
            break

    print("СБОЙ НА СЕРВЕРЕ")


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS)
    print("Ожидание подключения...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
