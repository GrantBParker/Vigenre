def main():

    message = input("Enter a message to encrypt:")
    message = message.lower()

    key = input("Enter a key to use:")
    key = key.lower()

    vig_square = create_vig_square()

    coded_msg = encrypt(message, key, vig_square)

    print("Encoded: ", coded_msg)

    decoded_msg = decrypt(coded_msg, key, vig_square)

    print(decoded_msg.lower())

    print("Decoded: ", decoded_msg)


def encrypt(msg, key, vig_square):
    coded_msg = ""
    msg_len = len(msg)
    key_len = len(key)
    j = 0
    for i in range(msg_len):
        msg_char = msg[i]

        if msg_char.isalpha():
            if j == key_len:
                j = 0
            key_char = key[j]

            coded_char_row = get_row_index(key_char, vig_square)
            code_char_col = get_col_index(msg_char, vig_square)
            coded_char = vig_square[coded_char_row][code_char_col]
            coded_msg = coded_msg + coded_char

            j = j + 1
        else:

            coded_msg = coded_msg + msg_char

    return coded_msg


def decrypt(msg, key, vig_square):

    decoded_msg = ""
    msg_len = len(msg)
    key_len = len(key)
    j = 0
    for i in range(msg_len):
        msg_char = msg[i]

        if msg_char.isalpha():
            if j == key_len:
                j = 0
            key_char = key[j]

            decoded_msg += get_plain_text_char(msg_char, key_char, vig_square)

            j = j + 1
        else:

            decoded_msg = decoded_msg + msg_char

    return decoded_msg


def create_vig_square():
    vig_square = []
    for row in range(26):
        vig_row = []
        chr_code = ord('a') + row
        for col in range(26):
            letter = chr(chr_code)
            vig_row.append(letter)
            if chr_code == 122:
                chr_code = 97
            else:
                chr_code = chr_code + 1
        vig_square.append(vig_row)
    return vig_square


def get_col_index(msg_char, vig_square):
    col_index = 0

    for col in range(26):
        if vig_square[0][col] == msg_char:
            col_index = col
            break
    return col_index


def get_row_index(key_char, vig_square):
    row_index = 0

    for row in range(26):
        if vig_square[row][0] == key_char:
            row_index = row
            break
    return row_index


def get_plain_text_char(coded_char, key_char, vig_square):
    plain_text_char = ' '

    coded_char_row = get_row_index(key_char, vig_square)
    col = vig_square[coded_char_row].index(coded_char)
    plain_text_char = vig_square[0][col]

    return plain_text_char


main()
