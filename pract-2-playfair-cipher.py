# Name: Rishabhkumar Singh
# Roll no.: 30
# Practical 2 Playfair cipher

key = input("Enter key: ")
key = key.replace(" ", "")
key = key.upper()


def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]


result = list()
# Store the key
for c in key:
    if c not in result:
        if c == 'J':
            result.append('I')
        else:
            result.append(c)
flag = 0
# Store other characters
for i in range(65, 91):
    if chr(i) not in result:
        if i == 73 and chr(74) not in result:
            result.append("I")
            flag = 1
        elif flag == 0 and i == 73 or i == 74:
            pass
        else:
            result.append(chr(i))
k = 0
# Init the matrix
char_matrix = matrix(5, 5, 0)
# Store the matrix
for i in range(0, 5):
    for j in range(0, 5):
        char_matrix[i][j] = result[k]
        k += 1

# Return loc of the character in the matrix


def locindex(c):
    loc = list()
    if c == 'J':
        c = 'I'
    for i, j in enumerate(char_matrix):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
                return loc

# Encrypt using playfair cipher


def encrypt():
    msg = str(input("Enter your message: "))
    msg = msg.upper()
    msg = msg.replace(" ", "")
    i = 0
    for s in range(0, len(msg)+1, 2):
        if s < len(msg)-1:
            if msg[s] == msg[s+1]:
                msg = msg[:s+1]+'X'+msg[s+1:]
    if len(msg) % 2 != 0:
        msg = msg[:]+'X'
        print("\nCipher list: ", end=' ')
        cipher_text = ''
        while i < len(msg):
            loc = list()
            loc = locindex(msg[i])
            loc1 = list()
            loc1 = locindex(msg[i+1])
            if loc[1] == loc1[1]:
                c_text = "{}{}".format(
                    char_matrix[(loc[0]+1) % 5][loc[1]], char_matrix[(loc1[0]+1) % 5][loc1[1]])
                cipher_text += c_text
                print(c_text, end=' ')
            elif loc[0] == loc1[0]:
                c_text = "{}{}".format(char_matrix[loc[0]][(
                    loc[1]+1) % 5], char_matrix[loc1[0]][(loc1[1]+1) % 5])
                cipher_text += c_text
                print(c_text, end=' ')
            else:
                c_text = "{}{}".format(
                    char_matrix[loc[0]][loc1[1]], char_matrix[loc1[0]][loc[1]])
                cipher_text += c_text
                print(c_text, end=' ')
            i = i+2
        print("\nCipher text: ", cipher_text.lower())

# Decrypt using playfair cipher


def decrypt():
    msg = str(input("\nEnter cipher text: "))
    msg = msg.upper()
    msg = msg.replace(" ", "")
    print("\nDeciphered List", end=' ')
    i = 0
    deciphered_text = ''
    while i < len(msg):
        loc = list()
        loc = locindex(msg[i])
        loc1 = list()
        loc1 = locindex(msg[i+1])
        if loc[1] == loc1[1]:
            d_text = "{}{}".format(
                char_matrix[(loc[0]-1) % 5][loc[1]], char_matrix[(loc1[0]-1) % 5][loc1[1]])
            deciphered_text += d_text
            print(d_text, end=' ')
        elif loc[0] == loc1[0]:
            d_text = "{}{}".format(char_matrix[loc[0]][(
                loc[1]-1) % 5], char_matrix[loc1[0]][(loc1[1]-1) % 5])
            deciphered_text += d_text
            print(d_text, end=' ')
        else:
            d_text = "{}{}".format(
                char_matrix[loc[0]][loc1[1]], char_matrix[loc1[0]][loc[1]])
            deciphered_text += d_text
            print(d_text, end=' ')
        i = i+2
    print("\nDeciphered text: ", deciphered_text.lower())


# Menu driver
while (1):
    print("\n1.Encryption \n2.Decryption: \n3.EXIT\n")
    choice = input("Enter your choice: ")
    if choice[0] == "1":
        encrypt()
    elif choice[0] == "2":
        decrypt()
    elif choice[0] == "3":
        exit()
    else:
        print("\nChoose correct choice\n")
