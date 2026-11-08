INITIAL_PERMUTATION = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
]

FINAL_PERMUTATION = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
]

PERMUTED_CHOICE_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4,
]

PERMUTED_CHOICE_2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32,
]

LEFT_SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1,
]
#8 for 8 rounds
S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ],
]

P_PERMUTATION = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25,
]

BLOCK_SIZE = 8


def bytes_to_bits(data):
    return "".join(f"{byte:08b}" for byte in data)


def bits_to_bytes(bits):
    return bytes(int(bits[index:index + 8], 2) for index in range(0, len(bits), 8))


def permute(bits, table):
    return "".join(bits[position - 1] for position in table)


def xor_bits(a, b):
    return "".join("0" if x == y else "1" for x, y in zip(a, b))


def rotate_left(bits, amount):
    return bits[amount:] + bits[:amount]


def generate_round_keys(key):

    if not isinstance(key, bytes) or len(key) != BLOCK_SIZE:
        raise ValueError("DES requires a key of exactly 8 bytes (64 bits).")

    key_56 = permute(bytes_to_bits(key), PERMUTED_CHOICE_1)
    left, right = key_56[:28], key_56[28:]
    round_keys = []

    for shift in LEFT_SHIFTS:
        left = rotate_left(left, shift)
        right = rotate_left(right, shift)
        round_keys.append(permute(left + right, PERMUTED_CHOICE_2))

    return round_keys


def feistel_function(right, round_key):

    expanded = permute(right, EXPANSION_TABLE)
    mixed = xor_bits(expanded, round_key)
    sbox_output = ""

    for box_index in range(8):
        group = mixed[box_index * 6:(box_index + 1) * 6]
        row = int(group[0] + group[5], 2)
        column = int(group[1:5], 2)
        number = S_BOXES[box_index][row][column]
        sbox_output += f"{number:04b}"

    return permute(sbox_output, P_PERMUTATION)


def _process_block_with_keys(block, round_keys):

    if not isinstance(block, bytes) or len(block) != BLOCK_SIZE:
        raise ValueError("Each DES block must contain exactly 8 bytes.")

    permuted = permute(bytes_to_bits(block), INITIAL_PERMUTATION)
    left, right = permuted[:32], permuted[32:]

    for round_key in round_keys:
        left, right = right, xor_bits(left, feistel_function(right, round_key))


    return bits_to_bytes(permute(right + left, FINAL_PERMUTATION))


def process_block(block, key, decrypt=False):

    round_keys = generate_round_keys(key)
    if decrypt:
        round_keys.reverse()
    return _process_block_with_keys(block, round_keys)


def encrypt_ecb(plaintext, key):

    if not plaintext or len(plaintext) % BLOCK_SIZE != 0:
        raise ValueError("Plaintext length must be a nonzero multiple of 8 bytes.")
    round_keys = generate_round_keys(key)
    return b"".join(
        _process_block_with_keys(plaintext[i:i + BLOCK_SIZE], round_keys)
        for i in range(0, len(plaintext), BLOCK_SIZE)
    )


def decrypt_ecb(ciphertext, key):

    if not ciphertext or len(ciphertext) % BLOCK_SIZE != 0:
        raise ValueError("Ciphertext length must be a nonzero multiple of 8 bytes.")
    round_keys = generate_round_keys(key)
    round_keys.reverse()
    return b"".join(
        _process_block_with_keys(ciphertext[i:i + BLOCK_SIZE], round_keys)
        for i in range(0, len(ciphertext), BLOCK_SIZE)
    )


def round_one_details(plaintext_block, key):

    if len(plaintext_block) != 8:
        raise ValueError("Appendix A example must be exactly 8 bytes.")
    ip = permute(bytes_to_bits(plaintext_block), INITIAL_PERMUTATION)
    left, right = ip[:32], ip[32:]
    first_key = generate_round_keys(key)[0]
    function_output = feistel_function(right, first_key)
    left1, right1 = right, xor_bits(left, function_output)
    return {"initial_permutation": ip, "left0": left, "right0": right,
            "key1": first_key, "feistel": function_output,
            "left1": left1, "right1": right1}


def pad_if_needed(plaintext):
    if not isinstance(plaintext, bytes):
        raise TypeError("Plaintext must be bytes.")
    if not plaintext:
        raise ValueError("The transaction cannot be empty.")
    missing = (-len(plaintext)) % BLOCK_SIZE
    return plaintext + bytes([missing]) * missing


def remove_padding(padded_plaintext, original_length):
    if not isinstance(padded_plaintext, bytes):
        raise TypeError("Plaintext must be bytes.")
    if not isinstance(original_length, int) or original_length <= 0:
        raise ValueError("Invalid original plaintext length.")
    if len(padded_plaintext) % BLOCK_SIZE:
        raise ValueError("Invalid decrypted data length.")
    missing = len(padded_plaintext) - original_length
    if missing < 0 or missing > 7:
        raise ValueError("Original length does not match the ciphertext.")
    if missing and padded_plaintext[-missing:] != bytes([missing]) * missing:
        raise ValueError("Invalid padding bytes.")
    return padded_plaintext[:original_length]


def encrypt_ecb_message(plaintext, key):
    return encrypt_ecb(pad_if_needed(plaintext), key)


def decrypt_ecb_message(ciphertext, key, original_length):
    if not isinstance(original_length, int) or original_length <= 0:
        raise ValueError("Invalid original plaintext length.")
    if len(ciphertext) != ((original_length + 7) // 8) * 8:
        raise ValueError("Ciphertext and original lengths do not match.")
    return remove_padding(decrypt_ecb(ciphertext, key), original_length)
