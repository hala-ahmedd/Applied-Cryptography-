from des import (process_block, encrypt_ecb, decrypt_ecb, round_one_details,
                 encrypt_ecb_message, decrypt_ecb_message, pad_if_needed, remove_padding)


def main():
    plaintext = bytes.fromhex("0123456789ABCDEF")
    key = bytes.fromhex("133457799BBCDFF1")
    ciphertext = process_block(plaintext, key)
    assert ciphertext.hex().upper() == "85E813540F0AB405"
    assert process_block(ciphertext, key, decrypt=True) == plaintext
    print("Standard DES test vector: PASS")

    bank_key = b"BANKKEY!"
    details = round_one_details(b"TRANSFER", bank_key)
    assert details["initial_permutation"] == (
        "11111111100100110110100101010100"
        "00000000000000000000100010111010"
    )
    assert details["key1"] == "101000001001001000100010101010000111010000000001"
    assert details["feistel"] == "01001011110111011101110010011110"
    assert details["left1"] + details["right1"] == (
        "00000000000000000000100010111010"
        "10110100010011101011010111001010"
    )
    print("Appendix A first DES round: PASS")

    raw = encrypt_ecb(b"TRANSFER", bank_key)
    assert raw.hex().upper() == "8B754C60E09223F2"
    assert decrypt_ecb(raw, bank_key) == b"TRANSFER"
    print("Full 16-round encryption and decryption: PASS")

    assert pad_if_needed(b"TRANSFER") == b"TRANSFER"
    assert pad_if_needed(b"TRANSFERTRANSFER") == b"TRANSFERTRANSFER"
    assert pad_if_needed(b"PAY:2500.50") == b"PAY:2500.50" + b"\x05" * 5
    assert pad_if_needed(b"PAY100") == b"PAY100" + b"\x02" * 2
    assert remove_padding(b"TRANSFER", 8) == b"TRANSFER"
    assert remove_padding(b"PAY:2500.50" + b"\x05" * 5, 11) == b"PAY:2500.50"
    print("Conditional padding tests: PASS")

    for message in [b"A", b"PAY100", b"PAY:2500.50", b"TRANSFER", b"TRANSFERTRANSFER",
                    b"TRANSFER 2500.75", b"ABCDEF\x02\x02", b"A" * 4096]:
        encrypted = encrypt_ecb_message(message, bank_key)
        assert len(encrypted) == ((len(message) + 7) // 8) * 8
        assert decrypt_ecb_message(encrypted, bank_key, len(message)) == message
    assert len(encrypt_ecb_message(b"TRANSFER", bank_key)) == 8
    assert len(encrypt_ecb_message(b"TRANSFERTRANSFER", bank_key)) == 16
    print("Variable transaction lengths and numeric inputs: PASS")

    repeated = encrypt_ecb_message(b"TRANSFERTRANSFER", bank_key)
    assert repeated.hex().upper() == "8B754C60E09223F28B754C60E09223F2"
    print("Block 1 ciphertext:", repeated[:8].hex().upper())
    print("Block 2 ciphertext:", repeated[8:16].hex().upper())
    print("ECB repeated-block demonstration: PASS")

    try:
        remove_padding(b"PAY:2500.50" + b"\x04" * 5, 11)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid padding was accepted")
    try:
        decrypt_ecb_message(repeated, bank_key, 15)
    except ValueError:
        pass
    else:
        raise AssertionError("Mismatched message lengths were accepted")
    print("Invalid padding and message-length validation: PASS")


if __name__ == "__main__":
    main()
