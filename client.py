import socket
from des import encrypt_ecb_message

HOST = "127.0.0.1"
PORT = 5000
KEY = b"BANKKEY!" #standard key for both files


def get_transaction():
    while True:
        message = input("Enter a transaction (ASCII letters, numbers, or symbols): ")
        try:
            plaintext = message.encode("ascii")
        except UnicodeEncodeError:
            print("Please enter ASCII characters only, like TRANSFER or PAY:2500.50.")
            continue

        if not plaintext:
            print("The transaction cannot be empty.")
        elif len(plaintext) > 4096:
            print("Please keep the test transaction at or below 4096 characters.")
        else:
            return plaintext


def main():
    plaintext = get_transaction()
    ciphertext = encrypt_ecb_message(plaintext, KEY)
    padding_length = len(ciphertext) - len(plaintext)

    print("\nPlaintext:", plaintext.decode("ascii"))
    print("Padding bytes added:", padding_length)
    print("Full ciphertext (hex):", ciphertext.hex().upper())
    print("\nDES-ECB ciphertext blocks:")
    blocks = []
    for index in range(0, len(ciphertext), 8):
        block = ciphertext[index:index + 8].hex().upper()
        blocks.append(block)
        print(f"  Block {index // 8 + 1}: {block}")

    if len(blocks) >= 2 and blocks[0] == blocks[1]:
        print("\nBlocks 1 and 2 match. This demonstrates the ECB pattern weakness.")

    try:
        with socket.create_connection((HOST, PORT), timeout=10) as connection:
            header = len(ciphertext).to_bytes(4, "big") + len(plaintext).to_bytes(4, "big")
            connection.sendall(header + ciphertext)
        print("\nEncrypted transaction sent to the server.")
    except OSError as error:
        print("Connection failed. Start server.py first.")
        print("Details:", error)


if __name__ == "__main__":
    main()
