from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from postform.models import details
import pandas as pd
import os
import json
import numpy as np
import traceback

bucket_name = 'locations'
media_root = settings.MEDIA_ROOT

class Command(BaseCommand):
    help = 'Insert test data'
    def handle(self, *args, **options):
        file_path = settings.MEDIA_ROOT + "/locations"
        dir_list = [name for name in os.listdir(file_path)]
        input_file_list = set([file for file in os.listdir(file_path) if file.endswith(".xlsx") and not file.startswith('processed')])
        user_data = {}
        
        for each_file in list(input_file_list):
            assembly_code = '0'+each_file.split('_')[0]

            file_name = file_path+'/'+each_file
            df = pd.read_excel(file_name)           
            print df.index

            for each_user in df.index:
                
                # user_data['district'] = df['DISTRICT'][i]
                user_data['name'] = df['name'][each_user]
                user_data['s_w_d_of'] = df['s_w_d_of'][each_user]
                user_data['mobile_number'] = df['mobile_number'][each_user]
                # print df['membership_id'][each_user].astype(np.int64)
                if type(df['membership_id'][each_user]) == "float":
                    user_data['membership_id'] = df['membership_id'][each_user].astype(np.int64)
                else:
                    user_data['membership_id'] = df['membership_id'][each_user]
                user_data['gender'] = df['gender'][each_user]
                user_data['email'] = df['email'][each_user]
                user_data['dno'] = df['door_number'][each_user]
                user_data['street'] = df['street'][each_user]
                user_data['pincode'] = df['pincode'][each_user]
                user_data['assembly_code'] = assembly_code
                # user_data['district_name'] = df['district_name'][each_user]
                # user_data['assembly_name'] = df['assembly_name'][each_user]
                user_data['mandal'] = df['mandal_name'][each_user]
                user_data['village'] = df['village_name'][each_user]
                # user_data['usercategory'] = df['usercategory'][each_user]
                user_data['active_membership_id'] = df['active_membership_id'][each_user]
                user_data['remark'] = df['remark'][each_user]
                user_data['amount'] = df['amount'][each_user]


                details.objects.create(**user_data) 
            self.rename_file(each_file)    

    def rename_file(self, file_name):
        try:
            input_file = os.path.join(media_root, bucket_name, file_name)
            processed_file = os.path.join(media_root, bucket_name,'processed_%s'%file_name)
            os.rename(input_file, processed_file)
        except Exception as e:
            print(traceback.format_exc())
            pass    