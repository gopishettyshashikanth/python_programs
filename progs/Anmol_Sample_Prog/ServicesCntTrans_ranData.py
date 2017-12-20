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
    elif type == "number":
        chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))

for i in range(1):
    data = {}
    data['anm_id'] = randon_string_generator(4, 'number')
    data['district_code'] = randon_string_generator(4, 'number')
    data['state_code'] = randon_string_generator(5, 'number')
    #data['date_synced'] = randon_string_generator(4, 'number')
    data['ec_services_hits'] = randon_string_generator(4, 'number')
    data['ec_services_success'] = randon_string_generator(4, 'number')
    data['ec_services_fail'] = randon_string_generator(10, 'number')
    data['pw_registration_hits'] = randon_string_generator(4, 'number')
    data['pw_registration_success'] = randon_string_generator(4, 'number')    
    data['pw_registration_fail'] = randon_string_generator(4, 'number')    
    data['mother_medical_hits'] = randon_string_generator(4, 'number')
    data['mother_medical_success'] = randon_string_generator(4, 'number')   
    data['mother_medical_fail'] = randon_string_generator(4, 'number')
    data['anc_services_hits'] = randon_string_generator(4, 'number')
    data['anc_services_success'] = randon_string_generator(4, 'number')
    data['anc_services_fail'] = randon_string_generator(4, 'number')
    data['delivery_services_hits'] = randon_string_generator(4, 'number')
    data['delivery_services_success'] = randon_string_generator(4, 'number')
    data['delivery_services_fail'] = randon_string_generator(4, 'number')
    data['infant_registration_hits'] = randon_string_generator(4, 'number')
    data['infant_registration_success'] = randon_string_generator(4, 'number')
    data['infant_registration_fail'] = randon_string_generator(4, 'number')
    data['child_registration_hits'] = randon_string_generator(4, 'number')
    data['child_registration_success'] = randon_string_generator(4, 'number')
    data['child_registration_fail'] = randon_string_generator(4, 'number')
    data['immunization_hits'] = randon_string_generator(4, 'number')
    data['immunization_success'] = randon_string_generator(4, 'number')
    data['immunization_fail'] = randon_string_generator(4, 'number')
    data['child_medical_hits'] = randon_string_generator(4, 'number')
    data['child_medical_success'] = randon_string_generator(4, 'number')
    data['child_medical_fail'] = randon_string_generator(4, 'number')
    data['child_pnc_hits'] = randon_string_generator(4, 'number')
    data['child_pnc_success'] = randon_string_generator(4, 'number')
    data['child_pnc_fail'] = randon_string_generator(4, 'number')
    data['pnc_services_hits'] = randon_string_generator(4, 'number')
    data['pnc_services_success'] = randon_string_generator(4, 'number')
    data['pnc_services_fail'] = randon_string_generator(4, 'number')
    data['IMEI1'] = randon_string_generator(10, 'char').title()   
    data['MacAddress'] = macaddress()
    data['IMEI2'] = randon_string_generator(12, 'char').title()
    print data


   