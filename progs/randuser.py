import random
import string


def randon_string_generator(size, type=None):
    if type == "char":
        chars = chars = string.ascii_uppercase 
    elif type == "string":
        chars = chars = string.ascii_uppercase + string.ascii_lowercase
    elif type == "number":
        chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))


for i in range(5):
    a={}
    a['username'] = randon_string_generator(6,'char')
    a['password']= randon_string_generator(6,'number')
    print a
