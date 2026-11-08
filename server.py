import socket
import time
from des import decrypt_ecb_message

HOST = "127.0.0.1"
PORT = 5000
KEY = b"BANKKEY!"
CLIENT_TIMEOUT_SECONDS = 5


def receive_exactly(connection, count, deadline):
    data = bytearray()
    while len(data) < count:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("Transaction reception timed out.")
        connection.settimeout(remaining)
        chunk = connection.recv(count - len(data))
        if not chunk:
            raise ConnectionError("The client disconnected before sending all data.")
        data.extend(chunk)
    return bytes(data)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Legacy Bank server listening on {HOST}:{PORT}")
        print("Press Ctrl+C to stop.\n")

        while True:
            connection, address = server.accept()
            with connection:
                print("Client connected:", address)
                try:
                    deadline = time.monotonic() + CLIENT_TIMEOUT_SECONDS
                    header = receive_exactly(connection, 8, deadline)
                    ciphertext_length = int.from_bytes(header[:4], "big")
                    plaintext_length = int.from_bytes(header[4:], "big")
                    expected_length = ((plaintext_length + 7) // 8) * 8
                    if not 1 <= plaintext_length <= 4096 or ciphertext_length != expected_length:
                        raise ValueError("Invalid transaction length.")

                    ciphertext = receive_exactly(connection, ciphertext_length, deadline)
                    print("Received ciphertext (hex):", ciphertext.hex().upper())
                    plaintext = decrypt_ecb_message(ciphertext, KEY, plaintext_length)
                    print("Decrypted transaction:", plaintext.decode("ascii"))
                except TimeoutError:
                    print(f"Could not process this transaction: client timed out after {CLIENT_TIMEOUT_SECONDS} seconds.")
                except (ValueError, ConnectionError, UnicodeDecodeError, OSError) as error:
                    print("Could not process this transaction:", error)
                print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nServer stopped.")
