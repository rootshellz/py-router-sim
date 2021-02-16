import socket
import time

router = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router.bind(("localhost", 8100))

router_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router_send.bind(("localhost", 8200))

router_mac = "00:00:00:00:00:00"

server = ("localhost", 8000)

client1_ip = "1.1.1.1"
client1_mac = "11:11:11:11:11:11"

client2_ip = "2.2.2.2"
client2_mac = "22:22:22:22:22:22"

client3_ip = "3.3.3.3"
client3_mac = "33:33:33:33:33:33"

router_send.listen(4)

client1 = None
client2 = None
client3 = None
while not client1 or not client2 or not client3:
    client, address = router_send.accept()

    if not client1:
        client1 = client
        print("Client 1 is online")
    elif not client2:
        client2 = client
        print("Client 2 is online")
    else:
        client3 = client
        print("Client 3 is online")

arp_table_socket = {client1_ip: client1, client2_ip: client2, client3_ip: client3}

arp_table_mac = {client1_ip: client1_mac, client2_ip: client2_mac, client3_ip: client3_mac}

router.connect(server)
while True:
    received_message = router.recv(1024)
    received_message = received_message.decode("utf-8")

    source_mac = received_message[0:17]
    destination_mac = received_message[17:34]

    source_ip = received_message[34:41]
    destination_ip = received_message[41:48]

    message = received_message[48:]

    print(f"The packed received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}")
    print(f"\nSource IP address: {source_ip}, Destination IP address: {destination_ip}")
    print("\nMessage: " + message)

    ethernet_header = router_mac + arp_table_mac[destination_ip]
    IP_header = source_ip + destination_ip
    packet = ethernet_header + IP_header + message

    destination_socket = arp_table_socket[destination_ip]
    destination_socket.send(bytes(packet, "utf-8"))
