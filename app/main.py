import socket  # noqa: F401

def create_msg(id):
    id_bytes = id.to_bytes(4,byteorder="big")
    return len(id_bytes).to_bytes(4,byteorder="big") + id_bytes

def handle_client(client):
    client.recv(1024)
    client.sendall(create_msg(7))
    client.close()


def main():
    server = socket.create_server(("localhost", 9092), reuse_port=True)

    while True:
        client , addr = server.accept()
        handle_client(client)



if __name__ == "__main__":
    main()
