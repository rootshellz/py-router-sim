import socket
import time

client3_ip = "3.3.3.3"
client3_mac = "33:33:33:33:33:33"
client3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

router = ("localhost", 8200)

time.sleep(1)
client3.connect(router)

while True:
    received_message = client3.recv(1024)
    received_message = received_message.decode("utf-8")

    source_mac = received_message[0:17]
    destination_mac = received_message[17:34]

    source_ip = received_message[34:41]
    destination_ip = received_message[41:48]

    message = received_message[48:]

    print(f"\nPacket integrity:\ndestination MAC address matches client 3 MAC address: {client3_mac == destination_mac}")
    print(f"\ndestination IP address matches client 3 IP address: {client3_ip == destination_ip}")
    print("\nThe packed received:")
    print(f"\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}")
    print(f"\nSource IP address: {source_ip}, Destination IP address: {destination_ip}")
    print("\nMessage: " + message)
