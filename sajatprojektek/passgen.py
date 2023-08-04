import random
import string
from datetime import date

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    ma = date.today()

    return password + str(ma).replace('-', '')

print(generate_password())