import socket
import time

client1_ip = "1.1.1.1"
client1_mac = "11:11:11:11:11:11"
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

router = ("localhost", 8200)

time.sleep(1)
client1.connect(router)

while True:
    received_message = client1.recv(1024)
    received_message = received_message.decode("utf-8")

    source_mac = received_message[0:17]
    destination_mac = received_message[17:34]

    source_ip = received_message[34:41]
    destination_ip = received_message[41:48]

    message = received_message[48:]

    print(f"\nPacket integrity:\ndestination MAC address matches client 1 MAC address: {client1_mac == destination_mac}")
    print(f"\ndestination IP address matches client 1 IP address: {client1_ip == destination_ip}")
    print("\nThe packed received:")
    print(f"\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}")
    print(f"\nSource IP address: {source_ip}, Destination IP address: {destination_ip}")
    print("\nMessage: " + message)
