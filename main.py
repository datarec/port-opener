# Simple port listener.

import socket
import random
import time
import os


def advanced_mode():
    time.sleep(0.3)
    os.system("cls")
    print("## Simple port opener ## > Advanced mode")
    try:
        ip = input("\nEnter IP to listen on: ")
        port = int(input("Enter port to listen on: "))

        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind((ip, port))
        print("\nListening on socketpair: {}:{}".format(ip, port))
        listener.listen()
        send, conn_info = listener.accept()

        print("Connection received from: {}".format(conn_info[0]))
    except ValueError:
        print("\nERROR: enter a port to listen on.")
        time.sleep(2)
        main()
    except socket.gaierror:
        print("ERROR: IP Address format incorrect. ")


def simple_mode():
    time.sleep(0.3)
    os.system("cls")
    print("## Simple port opener ## > Advanced mode")

    ip = "127.0.0.1"
    rand_port = random.randrange(2000, 4000)
    print("\nListening on socketpair: {}:{}".format(ip, rand_port))

    listener_simple = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener_simple.bind((ip, rand_port))
    listener_simple.listen()
    send, conn_info= listener_simple.accept()
    print("Connection received from: {}".format(conn_info[0]))


def main():
    time.sleep(0.3)
    os.system("cls")
    print("## Simple port opener ## - datarec on github")

    simple_advanced = input("""
1) Simple Mode (Preset with random port and local host)
2) Advanced mode (Custom listener)
    
    
>> """)
    if simple_advanced == "1":
        simple_mode()
    elif simple_advanced == "2":
        advanced_mode()


if __name__ == "__main__":
    main()
