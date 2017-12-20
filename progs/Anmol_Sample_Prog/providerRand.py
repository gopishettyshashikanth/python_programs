import string
import random

def randon_string_generator(size, type=None):
    if type == "char":
        chars = chars = string.ascii_uppercase + string.ascii_lowercase
    elif type == "number":
        chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))

#states = [23,28,87,95]
#statesRandomIndex = random.randint(0,len(states)-1)

stName=['Andhra Pradesh','Telangana']
stNameRandomIndex = random.randint(0,len(stName)-1)
#print(stName[stNameRandomIndex])

if stName[stNameRandomIndex] == 'Andhra Pradesh':
    stCode="28"
    distNames=['vizag','krishna']
    distNameRandomIndex = random.randint(0,len(distNames)-1)
    if distNames[distNameRandomIndex]== 'vizag':
        distCode="30"
    elif distNames[distNameRandomIndex]== 'krishna':
        distCode="40"
elif stName[stNameRandomIndex] == 'Telangana':     
    stCode="95"
    distNames=['Hyderabad','Medak']
    distNameRandomIndex = random.randint(0,len(distNames)-1)
    if distNames[distNameRandomIndex]== 'Hyderabad':
        distCode="10"
    elif distNames[distNameRandomIndex]== 'Medak':
        distCode="20"

def macaddress():

    mac = [ 0x00, 0x24, 0x81,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]

    return ':'.join(map(lambda x: "%02x" % x, mac))

p=input("No of records:")

for i in range(p):
    provider_data = {
    }
    provider_data['aadharNumber'] = randon_string_generator(12, 'number')
    provider_data['anmName'] = randon_string_generator(12, 'char').title()
    provider_data['ashaName'] = randon_string_generator(5, 'char').title()
    provider_data['ashaid'] = randon_string_generator(4, 'number')
    anmidnum =randon_string_generator(4, 'number')
    provider_data['anmid'] = anmidnum
    provider_data['contactNumber'] = randon_string_generator(10, 'number')
    #districtcodenum =randon_string_generator(4, 'number')
    provider_data['districtCode'] = distCode #districtcodenum
    provider_data['districtName'] = distNames[distNameRandomIndex] #randon_string_generator(10, 'char').title()
    provider_data['healthBlockCode'] = randon_string_generator(4, 'number')
    provider_data['healthBlockName'] = randon_string_generator(8, 'char').title()
    provider_data['healthFacilityCode'] = randon_string_generator(4, 'number')
    provider_data['healthFacilityType'] = randon_string_generator(10, 'number')
    provider_data['healthSubFacilityCode'] = randon_string_generator(4, 'number')
    provider_data['healthSubFacilityName'] = randon_string_generator(12, 'char').title()
    provider_data['phcName'] = randon_string_generator(12, 'char').title()
    provider_data['ruralOrUrban'] = randon_string_generator(12, 'char').title()
    statecodenum = randon_string_generator(2, 'number')
    provider_data['stateCode'] = stCode#states[statesRandomIndex]
    provider_data['stateName'] = stName[stNameRandomIndex]#randon_string_generator(12, 'char').title()  
    provider_data['subPhcName'] = randon_string_generator(12, 'char').title()
    provider_data['talukaCode'] = randon_string_generator(4, 'number')
    provider_data['talukaName'] = randon_string_generator(12, 'char').title()
    provider_data['villageCode'] = randon_string_generator(4, 'number')
    provider_data['villageName'] = randon_string_generator(12, 'char').title()
    provider_data['IMEI1'] = randon_string_generator(15, 'number')
    provider_data['MacAddress'] = macaddress()
    provider_data['IMEI2'] = randon_string_generator(15, 'number')
    print "provide master:",provider_data


    login_trans_data = {}

    login_trans_data['statecode'] = stCode#states[statesRandomIndex]
    login_trans_data['districtcode'] = distCode #districtcodenum
    login_trans_data['blockcode'] = randon_string_generator(5, 'number')
    login_trans_data['phccode'] = randon_string_generator(4, 'number')
    login_trans_data['subcentercode'] = randon_string_generator(4, 'number')
    login_trans_data['anmid'] =anmidnum
    login_trans_data['totalrecords'] = randon_string_generator(10, 'char').title()
    login_trans_data['recordssentforsync'] = randon_string_generator(4, 'number')
    login_trans_data['recordssentforsyncfailed'] = randon_string_generator(4, 'number')
    #login_trans_data['lastlogintimestamp'] = randon_string_generator(8, 'char').title()
    login_trans_data['connectionstatusatlastlogin'] = randon_string_generator(10, 'char').title()
    login_trans_data['IMEI1'] = randon_string_generator(10, 'char').title()
    login_trans_data['MacAddress'] = macaddress()
    login_trans_data['IMEI2'] = randon_string_generator(12, 'char').title()
    print "login transactions:",login_trans_data

    service_count_data = {}
    service_count_data['anm_id'] = anmidnum
    service_count_data['district_code'] = distCode #districtcodenum
    service_count_data['state_code'] = stCode

    # data['date_synced'] = randon_string_generator(4, 'number')
    service_count_data['ec_services_hits'] = randon_string_generator(4, 'number')
    service_count_data['ec_services_success'] = randon_string_generator(4, 'number')
    service_count_data['ec_services_fail'] = randon_string_generator(10, 'number')
    service_count_data['pw_registration_hits'] = randon_string_generator(4, 'number')
    service_count_data['pw_registration_success'] = randon_string_generator(4, 'number')
    service_count_data['pw_registration_fail'] = randon_string_generator(4, 'number')
    service_count_data['mother_medical_hits'] = randon_string_generator(4, 'number')
    service_count_data['mother_medical_success'] = randon_string_generator(4, 'number')
    service_count_data['mother_medical_fail'] = randon_string_generator(4, 'number')
    service_count_data['anc_services_hits'] = randon_string_generator(4, 'number')
    service_count_data['anc_services_success'] = randon_string_generator(4, 'number')
    service_count_data['anc_services_fail'] = randon_string_generator(4, 'number')
    service_count_data['delivery_services_hits'] = randon_string_generator(4, 'number')
    service_count_data['delivery_services_success'] = randon_string_generator(4, 'number')
    service_count_data['delivery_services_fail'] = randon_string_generator(4, 'number')
    service_count_data['infant_registration_hits'] = randon_string_generator(4, 'number')
    service_count_data['infant_registration_success'] = randon_string_generator(4, 'number')
    service_count_data['infant_registration_fail'] = randon_string_generator(4, 'number')
    service_count_data['child_registration_hits'] = randon_string_generator(4, 'number')
    service_count_data['child_registration_success'] = randon_string_generator(4, 'number')
    service_count_data['child_registration_fail'] = randon_string_generator(4, 'number')
    service_count_data['immunization_hits'] = randon_string_generator(4, 'number')
    service_count_data['immunization_success'] = randon_string_generator(4, 'number')
    service_count_data['immunization_fail'] = randon_string_generator(4, 'number')
    service_count_data['child_medical_hits'] = randon_string_generator(4, 'number')
    service_count_data['child_medical_success'] = randon_string_generator(4, 'number')
    service_count_data['child_medical_fail'] = randon_string_generator(4, 'number')
    service_count_data['child_pnc_hits'] = randon_string_generator(4, 'number')
    service_count_data['child_pnc_success'] = randon_string_generator(4, 'number')
    service_count_data['child_pnc_fail'] = randon_string_generator(4, 'number')
    service_count_data['pnc_services_hits'] = randon_string_generator(4, 'number')
    service_count_data['pnc_services_success'] = randon_string_generator(4, 'number')
    service_count_data['pnc_services_fail'] = randon_string_generator(4, 'number')
    service_count_data['IMEI1'] = randon_string_generator(10, 'char').title()
    service_count_data['MacAddress'] = macaddress()
    service_count_data['IMEI2'] = randon_string_generator(12, 'char').title()
    print "service count",service_count_data