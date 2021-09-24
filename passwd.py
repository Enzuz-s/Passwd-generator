import random as rand
import string

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def gen_rand_passwd():
    length = int(input("Enter password length: "))
    alphabets_count = int(input("Enter alphabets count in password: "))
    digits_count = int(input("Enter digits count in password: "))
    special_characters_count = int(input("Enter special characters count in password: "))
    characters_count = alphabets_count + digits_count + special_characters_count

    if characters_count > length:
        print("Characters total count is greater than the password length")
        return

    pwd = []

    for _ in range(alphabets_count):
        pwd.append(rand.choice(alphabets))

    for _ in range(digits_count):
        pwd.append(rand.choice(digits))

    for _ in range(special_characters_count):
        pwd.append(rand.choice(special_characters))

    if characters_count < length:
        rand.shuffle(characters)
        for _ in range(length - characters_count):
            pwd.append(rand.choice(characters))

    rand.shuffle(pwd)
    print("".join(pwd))


gen_rand_passwd()
