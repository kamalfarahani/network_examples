import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 5555))
    print("Listening on port 5555...")
    while True:
        data, addr = sock.recvfrom(1024)
        msg_str = data.decode("utf-8")
        reply_str = "Echo: " + msg_str
        sock.sendto(reply_str.encode("utf-8"), addr)


if __name__ == "__main__":
    main()
