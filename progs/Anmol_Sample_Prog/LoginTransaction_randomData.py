import string
import random

def macaddress():

    mac = [ 0x00, 0x24, 0x81,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]

    return ':'.join(map(lambda x: "%02x" % x, mac))

def randon_string_generator(size, type=None):
    if type == "char":
        chars = chars = string.ascii_uppercase + string.ascii_lowercase
    # elif type == "string":
    #     chars = chars = string.ascii_uppercase + string.ascii_lowercase
    elif type == "number":
        chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))

for i in range(1):
    data = {}
    data['statecode'] = randon_string_generator(4, 'number')
    data['districtcode'] = randon_string_generator(4, 'number')
    data['blockcode'] = randon_string_generator(5, 'number')
    data['phccode'] = randon_string_generator(4, 'number')
    data['subcentercode'] = randon_string_generator(4, 'number')
    data['anmid'] = randon_string_generator(4, 'number')
    data['totalrecords'] = randon_string_generator(10, 'char').title()
    data['recordssentforsync'] = randon_string_generator(4, 'number')
    data['recordssentforsyncfailed'] = randon_string_generator(4, 'number')    
    data['lastlogintimestamp'] = randon_string_generator(8, 'char').title()    
    data['connectionstatusatlastlogin'] = randon_string_generator(10, 'char').title()
    data['IMEI1'] = randon_string_generator(10, 'char').title()
    data['MacAddress'] = macaddress()
    data['IMEI2'] = randon_string_generator(12, 'char').title()
    print data

