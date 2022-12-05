import secrets
import string

letters_l = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters_l + digits + special_chars

pwd_length = 50

pwd = ''
for i in range(pwd_length):
    pwd += "".join(secrets.choice(alphabet))

print(pwd)