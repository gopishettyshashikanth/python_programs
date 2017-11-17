import string
import random
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from accounts.models import *
import time
import pprint
import datetime

def randon_string_generator(size, type=None):
    if type == "char":
        chars = chars = string.ascii_uppercase + string.ascii_lowercase
    elif type == "number":
        chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))

stName_list={'Andhra Pradesh':1,'Telangana':2}


hb_list = ["HB-%s"%item for item in range(1,6)]
hf_list = ["HF-%s"%item for item in range(1,6)]
sc_list = ["SC-%s"%item for item in range(1,6)]
vlg_list = ["VLG-%s"%item for item in range(1,6)]

def macaddress():

    mac = [ 0x00, 0x24, 0x81,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]

    return ':'.join(map(lambda x: "%02x" % x, mac))

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('no_anms', type=int)

    def handle(self, *args, **options):
        no_anms = options.get('no_anms')

        for i in range(no_anms):
            state_choice = random.choice(stName_list.keys())
            state_code = stName_list[state_choice]
            if state_choice == 'Andhra Pradesh':
                distNames={'vizag' :30 ,'krishna':40}
            elif state_choice == 'Telangana':     
                distNames={'Hyderabad' :10 ,'Medak':20}
            dist_choice = random.choice(distNames.keys())

            dist_code = distNames[dist_choice]
            provider_data = {}
            provider_data['aadharNumber'] = randon_string_generator(12, 'number')
            provider_data['anmName'] = randon_string_generator(12, 'char').title()
            provider_data['ashaName'] = randon_string_generator(5, 'char').title()
            provider_data['ashaid'] = randon_string_generator(4, 'number')
            anmidnum =randon_string_generator(4, 'number')
            provider_data['anmid'] = anmidnum
            provider_data['contactNumber'] = randon_string_generator(10, 'number')
            provider_data['districtCode'] = dist_code
            provider_data['districtName'] = dist_choice
            provider_data['healthBlockCode'] = randon_string_generator(1, 'number')
            provider_data['healthBlockName'] = random.choice(hb_list)
            provider_data['healthFacilityCode'] = randon_string_generator(1, 'number')
            provider_data['healthFacilityType'] = randon_string_generator(10, 'number')
            provider_data['healthSubFacilityCode'] = randon_string_generator(1, 'number')
            provider_data['healthSubFacilityName'] = randon_string_generator(12, 'char').title()
            provider_data['phcName'] = random.choice(sc_list)
            provider_data['ruralOrUrban'] = randon_string_generator(12, 'char').title()
            provider_data['stateCode'] = state_code
            provider_data['stateName'] = state_choice 
            provider_data['subPhcName'] = randon_string_generator(12, 'char').title()
            provider_data['talukaCode'] = randon_string_generator(4, 'number')
            provider_data['talukaName'] = randon_string_generator(12, 'char').title()
            provider_data['villageCode'] = randon_string_generator(1, 'number')
            provider_data['villageName'] = random.choice(vlg_list)
            provider_data['IMEI1'] = randon_string_generator(15, 'number')
            provider_data['MacAddress'] = macaddress()
            provider_data['IMEI2'] = randon_string_generator(15, 'number')
            #pp = pprint.PrettyPrinter(indent=4)
            #pp.pprint(provider_data)
            try:
                pm_obj = ProviderMaster.objects.create(**provider_data)
                for item in range(3):
                    login_trans_data = {}
                    login_trans_data['statecode'] = state_code
                    login_trans_data['districtcode'] = dist_code 
                    login_trans_data['blockcode'] = randon_string_generator(1, 'number')
                    login_trans_data['phccode'] = randon_string_generator(1, 'number')
                    login_trans_data['subcentercode'] = randon_string_generator(1, 'number')
                    login_trans_data['anmid'] =anmidnum
                    login_trans_data['totalrecords'] = randon_string_generator(10, 'char').title()
                    login_trans_data['recordssentforsync'] = randon_string_generator(4, 'number')
                    login_trans_data['recordssentforsyncfailed'] = randon_string_generator(4, 'number')
                    login_trans_data['connectionstatusatlastlogin'] = randon_string_generator(10, 'char').title()
                    login_trans_data['IMEI1'] = randon_string_generator(10, 'char').title()
                    login_trans_data['MacAddress'] = macaddress()
                    login_trans_data['IMEI2'] = randon_string_generator(12, 'char').title()
                    login_trans_data['lastlogintimestamp'] = datetime.date.today()
                    
                    try:
                        LoginTransaction.objects.create(**login_trans_data)
                    except Exception as e:
                        print (e)
                        pass
                    service_count_data = {}
                    service_count_data['anm_id'] = anmidnum
                    service_count_data['district_code'] = dist_code 
                    service_count_data['state_code'] = state_code

                    ec_service_success_num =randon_string_generator(2, 'number')
                    ec_service_failure_num =randon_string_generator(2, 'number')

                    service_count_data['ec_services_hits'] = ec_service_success_num + ec_service_failure_num
                    service_count_data['ec_services_success'] = ec_service_success_num
                    service_count_data['ec_services_fail'] = ec_service_failure_num

                    pw_registration_success_num =randon_string_generator(2, 'number')
                    pw_registration_failure_num =randon_string_generator(2, 'number')

                    service_count_data['pw_registration_hits'] = pw_registration_success_num + pw_registration_failure_num
                    service_count_data['pw_registration_success'] = pw_registration_success_num
                    service_count_data['pw_registration_fail'] = pw_registration_failure_num

                    mother_medical_success_num =randon_string_generator(2, 'number')
                    mother_medical_failure_num =randon_string_generator(2, 'number')

                    service_count_data['mother_medical_hits'] = mother_medical_success_num + mother_medical_failure_num
                    service_count_data['mother_medical_success'] = mother_medical_success_num
                    service_count_data['mother_medical_fail'] = mother_medical_failure_num

                    anc_services_success_num =randon_string_generator(2, 'number')
                    anc_services_failure_num =randon_string_generator(2, 'number')

                    service_count_data['anc_services_hits'] = anc_services_success_num + anc_services_failure_num
                    service_count_data['anc_services_success'] = anc_services_success_num
                    service_count_data['anc_services_fail'] = anc_services_failure_num

                    delivery_services_success_num =randon_string_generator(2, 'number')
                    delivery_services_failure_num =randon_string_generator(2, 'number')

                    service_count_data['delivery_services_hits'] = delivery_services_success_num + delivery_services_failure_num
                    service_count_data['delivery_services_success'] = delivery_services_success_num
                    service_count_data['delivery_services_fail'] = delivery_services_failure_num

                    infant_registration_success_num =randon_string_generator(2, 'number')
                    infant_registration_failure_num =randon_string_generator(2, 'number')                    

                    service_count_data['infant_registration_hits'] = infant_registration_success_num + infant_registration_failure_num
                    service_count_data['infant_registration_success'] = infant_registration_success_num
                    service_count_data['infant_registration_fail'] = infant_registration_failure_num

                    child_registration_success_num =randon_string_generator(2, 'number')
                    child_registration_failure_num =randon_string_generator(2, 'number')

                    service_count_data['child_registration_hits'] = child_registration_success_num + child_registration_failure_num
                    service_count_data['child_registration_success'] = child_registration_success_num
                    service_count_data['child_registration_fail'] = child_registration_failure_num

                    immunization_success_num =randon_string_generator(2, 'number')
                    immunization_failure_num =randon_string_generator(2, 'number')

                    service_count_data['immunization_hits'] = immunization_success_num + immunization_failure_num
                    service_count_data['immunization_success'] = immunization_success_num
                    service_count_data['immunization_fail'] = immunization_failure_num

                    child_medical_success_num =randon_string_generator(2, 'number')
                    child_medical_failure_num =randon_string_generator(2, 'number')

                    service_count_data['child_medical_hits'] = child_medical_success_num + child_medical_failure_num
                    service_count_data['child_medical_success'] = child_medical_success_num
                    service_count_data['child_medical_fail'] = child_medical_failure_num

                    child_pnc_success_num =randon_string_generator(2, 'number')
                    child_pnc_failure_num =randon_string_generator(2, 'number')

                    service_count_data['child_pnc_hits'] = child_pnc_success_num + child_pnc_failure_num
                    service_count_data['child_pnc_success'] = child_pnc_success_num
                    service_count_data['child_pnc_fail'] = child_pnc_failure_num

                    pnc_services_success_num =randon_string_generator(2, 'number')
                    pnc_services_failure_num =randon_string_generator(2, 'number')

                    service_count_data['pnc_services_hits'] = pnc_services_success_num + pnc_services_failure_num
                    service_count_data['pnc_services_success'] = pnc_services_success_num
                    service_count_data['pnc_services_fail'] = pnc_services_failure_num

                    service_count_data['IMEI1'] = randon_string_generator(10, 'char').title()
                    service_count_data['MacAddress'] = macaddress()
                    service_count_data['IMEI2'] = randon_string_generator(12, 'char').title()
                    service_count_data['date_synced'] = datetime.date.today()

                    try:
                        ServicesCountsTransactions.objects.create(**service_count_data)
                    except Exception as e:
                        print (e)
                        pass
            except Exception as e:
                print (e)
                pass