from django.core.management.base import BaseCommand, CommandError
from postform.models import ANMOL_WOMEN_DATA
from django.conf import settings
import os
import json
import traceback
import pprint


class Command(BaseCommand):

    def insert_ecpw_doc(self, **kwargs):
        pp = pprint.PrettyPrinter(depth=4)
        awd_obj = ANMOL_WOMEN_DATA(anm_id=kwargs.get('ANM_ID'))
        awd_obj.anm_id =  kwargs.get('ANM_ID')
        awd_obj.asha_id = kwargs.get('ASHA_ID')   
        awd_obj.save()
        pass

    def handle(self, *args, **options):
        all_ecpw_bucket_name = 'allecpw'
        all_ecpw_bucket_dir = os.path.join(settings.MEDIA_ROOT, all_ecpw_bucket_name)
        all_ecpw_bucket_files = [file for file in os.listdir(all_ecpw_bucket_dir) if file.endswith('.json')]
        for each_file in all_ecpw_bucket_files:
            try:
                input_file = os.path.join(settings.MEDIA_ROOT, all_ecpw_bucket_name, each_file)
                try:
                    all_ecpw_json_data = json.loads(open(input_file).read())
                    try:
                        for each_node in all_ecpw_json_data['data']:
                            try:
                                for each_node in each_node['value']:
                                    for each_doc in each_node:
                                        self.insert_ecpw_doc(**each_doc)                                        
                            except KeyError as e:
                                print(traceback.format_exc())
                            #break
                    except KeyError as e:
                        print(traceback.format_exc())
                except ValueError as e:
                    print(traceback.format_exc())
            except Exception as e:
                print(traceback.format_exc())
                pass
