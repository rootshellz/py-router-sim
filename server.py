import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8000))
server.listen(2)

server_ip = "4.4.4.4"
server_mac = "44:44:44:44:44:44"

router_mac = "00:00:00:00:00:00"

while True:
    router_connection, address = server.accept()
    if router_connection:
        print(router_connection)
        break

while True:
    ethernet_header = ""
    IP_header = ""

    message = input("\nEnter the text message to send: ")
    destination_ip = input("Enter the IP of the clients to send the message to:\n1: 1.1.1.1\n2: 2.2.2.2\n3: 3.3.3.3\n")

    if destination_ip in ["1.1.1.1", "2.2.2.2", "3.3.3.3"]:
        source_ip = server_ip
        IP_header = IP_header + source_ip + destination_ip

        source_mac = server_mac
        destination_mac = router_mac
        ethernet_header = ethernet_header + source_mac + destination_mac

        packet = ethernet_header + IP_header + message

        router_connection.send(bytes(packet, "utf-8"))
    else:
        print("Unknown client")
