import socket
import json


def parse_header(header: str) -> dict[str, str]:
    header_dict = {}
    for hline in header.split("\r\n")[1:]:
        k, v = hline.split(": ")
        header_dict[k] = v
    return header_dict


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 5555))
    s.listen()
    print("Listening on port 5555...")

    while True:
        conn, addr = s.accept()
        print("Connected by", addr)

        req = ""
        while True:
            data = conn.recv(1024)
            data_str = data.decode("utf-8")
            req += data_str
            # Check if '\r\n\r\n' is in the data
            if "\r\n\r\n" in data_str:
                break

        header, _ = req.split("\r\n\r\n")
        response_dict = parse_header(header)

        response = "HTTP/1.1 200 OK\r\n\r\n"
        response += json.dumps(response_dict)

        conn.sendall(response.encode("utf-8"))
        conn.close()


if __name__ == "__main__":
    main()
