import socket
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run_client(message):
    result = subprocess.run(
        [sys.executable, "client.py"], cwd=HERE,
        input=message + "\n", capture_output=True, text=True, timeout=15,
    )
    if result.returncode or "Encrypted transaction sent" not in result.stdout:
        raise AssertionError("Client failed:\n" + result.stdout + result.stderr)
    return result.stdout


def main():
    server = subprocess.Popen(
        [sys.executable, "-u", "server.py"], cwd=HERE,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    try:
        first_line = server.stdout.readline().strip()
        if "server listening" not in first_line:
            raise RuntimeError("Server did not start: " + first_line)

        single = run_client("TRANSFER")
        assert "Padding bytes added: 0" in single
        assert "Block 1: 8B754C60E09223F2" in single
        assert "Block 2:" not in single
        print("Single-block transaction with zero padding: PASS")

        repeated = run_client("TRANSFERTRANSFER")
        assert "Padding bytes added: 0" in repeated
        assert "Blocks 1 and 2 match" in repeated
        assert "Block 3:" not in repeated
        print("Repeated-block ECB demonstration without padding: PASS")

        numeric = run_client("PAY:2500.50")
        assert "Padding bytes added: 5" in numeric
        print("Numeric financial transaction with padding: PASS")

        corrected = subprocess.run(
            [sys.executable, "client.py"], cwd=HERE,
            input="\nTRANSFER\n", capture_output=True, text=True, timeout=15,
        )
        assert "The transaction cannot be empty" in corrected.stdout
        assert "Encrypted transaction sent" in corrected.stdout
        print("Invalid input prompts for correction: PASS")

        with socket.create_connection(("127.0.0.1", 5000), timeout=3) as stalled:
            stalled.sendall(b"\x00\x00")
            stalled.settimeout(8)
            try:
                closed = stalled.recv(1) == b""
            except ConnectionResetError:
                closed = True
            assert closed, "Stalled client was not disconnected"
        print("Stalled client timeout: PASS")

        with socket.create_connection(("127.0.0.1", 5000), timeout=3) as stalled:
            stalled.sendall((16).to_bytes(4, "big") + (16).to_bytes(4, "big") + b"\x11" * 8)
            stalled.settimeout(8)
            try:
                closed = stalled.recv(1) == b""
            except ConnectionResetError:
                closed = True
            assert closed, "Incomplete ciphertext was not disconnected"
        print("Incomplete ciphertext timeout: PASS")

        recovered = run_client("PAY100")
        assert "Padding bytes added: 2" in recovered
        print("Server recovery after timeout: PASS")

        time.sleep(0.2)
    finally:
        server.terminate()
        try:
            output, _ = server.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            server.kill()
            output, _ = server.communicate()

    assert output.count("Decrypted transaction: TRANSFER\n") == 2, output
    assert "Decrypted transaction: TRANSFERTRANSFER" in output, output
    assert "Decrypted transaction: PAY:2500.50" in output, output
    assert "Decrypted transaction: PAY100" in output, output
    assert output.count("client timed out after 5 seconds") == 2, output
    print("Server decrypted all transactions: PASS")
    print("\nAll client-server tests passed.")


if __name__ == "__main__":
    main()
