from django.core.management.base import BaseCommand, CommandError
from postform.models import UserCsvData
import pandas as pd
import numpy as np

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('no_rec', type=int)

    def handle(self, *args, **options):
        no_rec = options.get('no_rec')

        form_data = {}
        table_data = []
        index_data=[]
        for i in range(no_rec):
           form_data['userid'] = i
           form_data['username'] = "A"+str(i)           
           
           table_data.append(form_data)
           form_data={}
           index_data.append(i)
        # print table_data   
        df = pd.DataFrame(table_data, columns = ['userid', 'username'],index=index_data)
        df.to_csv('data.csv',index=False)

        input_csv = pd.read_csv('data.csv')
        find_csv = pd.read_csv('find.csv')        
        #print(pd.merge(input_csv, find_csv, on='userid', how='inner'))

        # matchdata_csv =  pd.merge(input_csv, find_csv, on='userid', how='inner')
        # df = pd.DataFrame(matchdata_csv, columns = ['userid'])
        # df.to_csv('matching.csv',index=False)

        finder_list = find_csv.userid.tolist()
        matches_result_input_df = input_csv[input_csv['userid'].isin(finder_list)]
        matches_result_input_df.to_csv('matches_result.csv', index=False)
        matches_list = matches_result_input_df.userid.tolist()

        unmatches_list_df = input_csv[~input_csv['userid'].isin(finder_list)]
        unmatches_list_df.to_csv("unmatches_result.csv", index=False)
        unmatches_list = unmatches_list_df.userid.tolist()        
       
           


               