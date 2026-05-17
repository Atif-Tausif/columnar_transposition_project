def encrypt_columnar(plaintext, key):

    num_cols = len(key)

    while len(plaintext) % num_cols != 0:
        plaintext += 'X'

    num_rows = len(plaintext) // num_cols

    matrix = []

    index = 0

    for _ in range(num_rows):

        row = []

        for _ in range(num_cols):

            row.append(plaintext[index])

            index += 1

        matrix.append(row)

    sorted_key = sorted(
        list(enumerate(key)),
        key=lambda x: x[1].lower()
    )

    ciphertext = ""

    for col_index, _ in sorted_key:

        for row in matrix:

            ciphertext += row[col_index]

    return ciphertext



def decrypt_columnar(ciphertext, key):

    num_cols = len(key)

    num_rows = len(ciphertext) // num_cols

    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    sorted_key = sorted(
        list(enumerate(key)),
        key=lambda x: x[1].lower()
    )

    index = 0

    for col_index, _ in sorted_key:

        for row in range(num_rows):

            matrix[row][col_index] = ciphertext[index]

            index += 1

    plaintext = ""

    for row in matrix:

        plaintext += ''.join(row)

    return plaintext.rstrip('X')